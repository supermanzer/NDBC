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

    # Defining some template strings as class variables that will be
    # used to define specific data URLS for each instance.
    stdmet_monthurls = [
        "https://www.ndbc.noaa.gov/data/stdmet/{month_num}/{station}.txt",
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
            self.station_id = str(station_id)
        self.data = {"stdmet": pd.DataFrame([])}

    def __str__(self):
        """
     Overriding the default __str__ method to be a bit more descriptive.
     """
        return "NDBC.DataBuoy Object for Station " + self.station_id

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

    def load_stdmet(self, url):
        """
    The function that does the actual loading of the stdmet data into the
    instance data attribute.
    """
        year_types = ["YY", "YYYY", "#YY"]
        data_df = pd.read_csv(url, "\s+")
        # We check to see if the first row is the units - true after 2009.
        if "#" in str(data_df.loc[0][0]):
            units = data_df.loc[0]
            data_df = data_df.drop([0])
        # Next we need to identify the columns relating to our datetime values.
        dt_index_cols = ["#YY", "MM", "DD", "hh"]
        if "mm" in list(data_df.columns):
            dt_index_cols.append("mm")
        # Since we may be dealing with historical data files that were weird
        # in their definition of year values
        yt = [x for x in year_types if x in data_df.columns][0]
        dt_index_cols[0] = yt
        if "mm" in list(data_df.columns):
            dt_format_vals = {yt: "%Y", "MM": "%m", "DD": "%d", "hh": "%H", "mm": "%M"}
        else:
            dt_format_vals = {yt: "%Y", "MM": "%m", "DD": "%d", "hh": "%H"}
        # detecting a two digit year (this stopped around 1996)
        if int(math.floor(math.log(int(data_df[yt][1]), 10) + 1)) == 2:
            data_df[yt] = data_df[yt] + 1900
        # Using our dictionary to build a formatting string for datetime
        dt_format_str = " ".join([dt_format_vals[x] for x in dt_index_cols])
        # Setting the datetime component columns as our index
        data_df.set_index(dt_index_cols, inplace=True)
        # Converting tuples of date/time components from columns into Python
        # datetime objects.
        dt_vals = [
            dt.strptime(" ".join(str(v) for v in x), dt_format_str)
            for x in data_df.index.values
        ]
        # Setting our index to our datetime list
        data_df.index = dt_vals
        # For older data - rename wind direction column so it matches newer
        # data and will merge seemlessly
        if "WD" in data_df.columns:
            data_df.rename(columns={"WD": "WDIR"}, inplace=True)
        self.data["stdmet"] = self.data["stdmet"].append(data_df)

    def get_stdmet(self, years=[], months=[]):
        """
    Method for gathering the standard meteorological summary data from the
    NDBC station represented by an instance of this class.  The years and
    months arguments passed in define the years and months (of the current
    year) for which data will be gathered.  This data will assigned as a
    pandas dataframe to the instance attribute data['stdmet'].
    Args:
        year(list) - A list of years for which to collect data.
        months(list) - A list of months of the current year for which to
                       collect data.
    Returns:
        times_unavailable(str) - A string identifying the years/months for
                                 which no data was collected.

    If this function is called without either years or months, it is assumed
    the user wishes to retrieve the most current month's data.
    """
        times_unavailable = ""
        # If no timeframe is specified we retrieve the most current complete
        # month for the given station.
        if not years and not months:
            month_num = dt.today().month
            year = dt.today().year
            my_url = False
            # Looping through potentially available months.
            while month_num >= 0 and not my_url:
                month_abbrv = dt(dt.today().year, month_num, 1).strftime("%b")
                kws = {"month_abbrv": month_abbrv, "month_num": month_num,
                       "year": year, "station": self.station_id}
                my_url = self.__checkurls__(
                    self.__buildurls__(self.stdmet_monthurls, kws)
                )
                if not my_url:
                    times_unavailable += month_abbrv + " not available.\n "
                month_num -= 1

            self.load_stdmet(my_url)

        else:
            for year in years:
                kws = {"year": year, "station": self.station_id}
                my_url = self.__checkurls__(
                    self.__buildurls__(self.stdmet_yearurls, kws)
                )
                if my_url:
                    self.load_stdmet(my_url)
                else:
                    times_unavailable += "Year " + str(year) + " not available.\n"

            for month in months:
                month_abbrv = dt(dt.today().year, month, 1).strftime("%b")
                year = dt.today().year
                kws = {
                    "year": year,
                    "month_abbrv": month_abbrv,
                    "month_num": month,
                    "station": self.station_id,
                }
                my_url = self.__checkurls__(
                    self.__buildurls__(self.stdmet_monthurls, kws)
                )
                if my_url:
                    self.load_stdmet(my_url)
                else:
                    times_unavailable += month_abbrv + " not available.\n"

        if len(times_unavailable) > 0:
            logger.warning(times_unavailable)

    def stdmet_to_json(self, file_name, date_format="iso", orient="columns"):
        """
    A simple method for outputing the existing stdmet data to a json file
    """

        self.data["stdmet"].to_json(file_name, date_format=date_format, orient=orient)

    # TODO (ryan@gensci.org): Build out function to look for values that are all '9' and replace them with None or NaN to indicate lack of valid data.
