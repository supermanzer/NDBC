"""
 NDBC.py - this file contains classes pertaining to the acquisition and
 transformation of National Data Buoy Center (NDBC) oceanographic data.

 Classes:
   DataBuoy - An initial attempt at building out a class for reading and
   parsing NDBC buoy data.

"""

import requests
import pandas as pd
import math
import re

from datetime import datetime as dt
from bs4 import BeautifulSoup
from typing import Union

from logging import getLogger

logger = getLogger(__name__)


class DataBuoy(object):
    """
   This class contains functions used to fetch and parse data from
   National Data Buoy Center stations.
  Example:
  ``
    >>>from NDBC.NDBC import DataBuoy
    >>>N42 = DataBuoy('46042')
    >>>N42.get_stdmet()
    'Jun not available.\n'
    >>>N42.data
    {'stdmet':       WDIR  WSPD   GST  WVHT  ...    WTMP   DEWP   VIS   TIDE
2018-04-30 23:50:00  309   9.6  11.6  2.84  ...    12.6  999.0  99.0  99.00
        ....
2018-05-31 22:50:00  304   9.3  11.4  2.02  ...    12.8  999.0  99.0  99.00
[742 rows x 13 columns]}
  ``
  """

    BASE_URL = "https://www.ndbc.noaa.gov/"
    STATION_URL = BASE_URL + "station_page.php?station={}"
    # REGEX PATTERNS FOR PARSING HTML STATION PAGES
    LAT_PAT = "\d+\.\d+\s+N"
    LON_PAT = "\d+\.\d+\s+W"
    ATTR_PAT = "<b>(.*):</b>\s*(.*)<br/>"
    # Defining some template strings as class variables that will be
    # used to define specific data URLS for each instance.
    stdmet_monthurls = [
        "https://www.ndbc.noaa.gov/data/stdmet/{month_abbrv}/{station}.txt",
        "https://www.ndbc.noaa.gov/view_text_file.php?filename={station}{"
        "month_num}{year}.txt.gz&dir=data/stdmet/{month_abbrv}/",
    ]

    stdmet_yearurls = [
        "https://www.ndbc.noaa.gov/view_text_file.php?filename={"
        "station}h{year}.txt.gz&dir=data/historical/stdmet/"
    ]

    def __init__(self, station_id=False) -> None:
        """
    Initialize object instance
    :param station_id: Station identifier <- required for data access
    """
        if station_id:
            self._station_id = str(station_id)
        self.data = {"stdmet": {}}

    def set_station_id(self, station_id):
        self._station_id = str(station_id).upper()

    def __str__(self):
        """
     Overriding the default __str__ method to be a bit more descriptive.
     """
        return "NDBC.DataBuoy Object for Station " + self._station_id

    def __checkurls__(self, urls):
        """
    Simple method to check list of urls, check if they return a 200 status
    code with a HEAD request, and return the first valid URL (if any).
    :param urls: The list of urls to check
    :return: The valid URL or False if none
    """
        url_check = [requests.head(url).status_code == 200 for url in urls]
        if any(url_check):
            return urls[url_check.index(True)]
        else:
            return False

    @staticmethod
    def __buildurls__(urls, format_kwargs):
        return [url.format(**format_kwargs) for url in urls]

    def _parse_metadata(self, element, station_metadata=None):
        """
        Parse out station meta data from the element containing it
        :param element: BeautifulSoup element containing station metadata
        :return: None: Meta data appended to DataBuoy object
        """
        if station_metadata is None:
            station_metadata = {}
        # There's probably a more elegant way to do this but trying to
        # optimize code before you write it is a fool's errand.
        for line in str(element).split("\n"):
            if re.search(self.LAT_PAT, line):
                station_metadata["lat"] = re.search(self.LAT_PAT, line).group()
            if re.search(self.LON_PAT, line):
                station_metadata["lon"] = re.search(self.LON_PAT, line).group()
            if re.search(self.ATTR_PAT, line):
                k, v = re.search(self.ATTR_PAT, line).groups()
                station_metadata[k] = v
        self.station_info = station_metadata

    def get_station_metadata(self) -> None:
        """
        Define method to capture and store station metadata
        :return: None
         """
        if not hasattr(self, '_station_id'):
            raise LookupError("No station ID provided")
        response = requests.get(self.STATION_URL.format(self._station_id))
        soup = BeautifulSoup(response.content, "html.parser")
        meta_div = soup.find("div", id="stn_metadata")
        if meta_div:
            for el in meta_div.find_all("p"):
                # Iterate over <p> tags.  One of these will have the station
                # details we are looking for.
                if (
                    re.search(self.LAT_PAT, str(el))
                    and re.search(self.LON_PAT, str(el))
                    and re.search(self.ATTR_PAT, str(el))
                ):
                    self._parse_metadata(el)
        else:
            raise ValueError("Station metadata not found")

    def __separate_units(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        If data DataFrame contains a row that corresponds to the units for
        the columns provided, separate them out and place them in stdmet
        metadata.
        :param data: pandas DataFrame result of reading in NDBC text file.
        :return: data DataFrame with units row removed, if present
        """
        # Check to see if the first row is the units - true after 2009.
        if data.loc[0][0][0] == "#":
            units = data.loc[0]
            columns = data.columns
            data = data.drop([0])
            if "meta" not in self.data["stdmet"].keys():
                self.data["stdmet"]["meta"] = {}
            self.data["stdmet"]["meta"]["units"] = {
                k: units[i] for i, k in enumerate(columns)
            }
        return data

    @staticmethod
    def _get_dt_parts(df: pd.DataFrame) -> dict:
        """
        Determine the date part columns and format string from df
        :param df: pandas DataFrame of stdmet data
        :return: dicitonary containing format string and list of columns
        """
        # Define columns and datetime string formats
        col_types = {
            'YYYY': '%Y',
            'YY': '%Y',
            'MM': '%m',
            'DD': '%d',
            'hh': '%H',
            'mm': '%M'
        }
        # Identifying the date part columns in the current dataframe
        dt_cols = [c for c in df.columns if c in col_types.keys()]
        # Building the formatting string used to construct datetime objects
        dt_format = ' '.join([col_types[c] for c in dt_cols])
        return {'columns': dt_cols, 'format_string': dt_format}

    @classmethod
    def _build_datetime(cls, data: pd.DataFrame) -> list:
        """
        Return datetime series constructed from extracted date parts
        :param data:Standard meteorological data
        :return: list of Python datetime instances.
        """
        dtdict = cls._get_dt_parts(data)
        # Addressing issues with 2 digit years (pre 1996 data)
        year_column = dtdict['columns'][0]
        if len(data[year_column].iloc[0]) == 2:
            data[year_column] = data[year_column] + 1900
        # Return a list of datetime objects for each row in dataframe
        return [
            dt.strptime(
                ' '.join([str(r.get(v))for v in dtdict['columns']]),
                dtdict['format_string'])
            for i, r in data.iterrows()
        ]

    @classmethod
    def _add_datetime(cls, data: pd.DataFrame, datetime_index=False) -> \
            pd.DataFrame:
        """
        Append datetime either as a column or record index
        :param data: pandas Dataframe of stdmet data
        :param datetime_index: Whether datetimes will be appended as column
        or dataframe index
        :return: dataframe with datetime appended and date part columns dopped
        """
        # Getting the list of dates to add
        dt_list = cls._build_datetime(data)
        # Get list of columns to drop
        dt_cols = cls._get_dt_parts(data)['columns']
        if datetime_index:
            data.index = dt_list
        else:
            data['datetime'] = dt_list

        return data.drop(columns=dt_cols)

    def load_stdmet(self, url, datetime_index=False) -> None:
        """
        Transform NDBC Standard Meteorological text data into pandas Dataframe
        and append to results
        :param url: Location of text data
        :return: None
        """
        data_df = pd.read_csv(url, "\s+")
        # The first column name often contains a # symbol.
        rename_cols = {c: c.replace('#', '')
                       for c in data_df.columns
                       if '#' in c}
        # Applying a basic fix for change in WDIR naming in earlier (<2000) data
        rename_cols['WD'] = 'WDIR'

        data_df.rename(columns=rename_cols, inplace=True)
        # Remove units row (if exists) and add to stdmet metadata
        data_df = self.__separate_units(data_df)
        # Building and appending datetimes from date parts
        data_df = self._add_datetime(data_df, datetime_index)
        # Append to existing stdmet dataframe if exists
        if "data" in self.data["stdmet"].keys():
            self.data["stdmet"]["data"] = self.data["stdmet"]["data"].append(
                                                                        data_df)
        # otherwise assign dataframe to stdment['data']
        else:
            self.data["stdmet"]["data"] = data_df

    def get_stdmet(self, years=False, months=False,
                   datetime_index=False) -> None:
        """
        Identify valid data files to append to stdmet data and call load_std()
        :param years: A list of years for which to gather data
        :param months: A list of months for which to gather data
        :return: None or string, if times are unavailable
        """
        times_unavailable = ""
        # If no time frame is specified we retrieve the most current complete
        # month for the given station.
        if not years and not months:
            month_num = dt.today().month
            year_num = dt.today().year
            my_url = False
            # Looping through potentially available months.
            while month_num > 0 and not my_url:
                month_abbrv = dt(year_num, month_num, 1).strftime("%b")
                kws = {"month_abbrv": month_abbrv, "month_num": month_num,
                       "station": self._station_id, "year": year_num}
                my_url = self.__checkurls__(
                    self.__buildurls__(self.stdmet_monthurls, kws)
                )
                if not my_url:
                    times_unavailable += month_abbrv + " not available.\n "

                month_num -= 1
            if my_url:
                self.load_stdmet(my_url, datetime_index)
        else:
            for year in years:
                kws = {"year": year, "station": self._station_id}
                my_url = self.__checkurls__(
                    self.__buildurls__(self.stdmet_yearurls, kws)
                )
                if my_url:
                    self.load_stdmet(my_url, datetime_index)
                else:
                    times_unavailable += "Year " + str(year) + " not available.\n"

            for month in months:
                month_abbrv = dt(dt.today().year, month, 1).strftime("%b")
                year = dt.today().year
                kws = {
                    "year": year,
                    "month_abbrv": month_abbrv,
                    "month_num": month,
                    "station": self._station_id,
                }
                my_url = self.__checkurls__(
                    self.__buildurls__(self.stdmet_monthurls, kws)
                )
                if my_url:
                    self.load_stdmet(my_url, datetime_index)
                else:
                    times_unavailable += month_abbrv + " not available.\n"

        if len(times_unavailable) > 0:
            logger.warning(times_unavailable)

    def stdmet_to_json(self, file_name, date_format="iso", orient="columns"):
        """
        A simple method for returning the existing stdmet data to a json file
        """
        self.data["stdmet"].to_json(file_name, date_format=date_format, orient=orient)

    # TODO (ryan@gensci.org): Build out function to look for values that are all '9' and replace them with None or NaN to indicate lack of valid data.
