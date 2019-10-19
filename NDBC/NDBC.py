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


class DataBuoy(object):
    """
    Define a class for accessing and analyzing NDBC data in Python.
    """
    BASE_URL = "https://www.ndbc.noaa.gov/"
    # Defining some template strings as class variables that will be
    # used to define specific data URLS for each instance.
    STDMET_MONTHURL = BASE_URL + '/data/stdmet/{month}/{station}.txt'

    STDMET_YEARURL = BASE_URL + 'view_text_file.php?filename={' \
                                'station}h{' \
                                'year}.txt.gz&dir=data/historical/stdmet/'
    STATION_URL = BASE_URL + "station_page.php?station={}"

    # REGEX PATTERNS FOR PARSING HTML STATION PAGES
    LAT_PAT = '\d+\.\d+\s+N'
    LON_PAT = '\d+\.\d+\s+W'
    ATTR_PAT = '<b>(.*):</b>\s*(.*)<br/>'

    def __init__(self, station_id=False) -> None:
        """
        Instantiate object
        :param station_id: Station identifier
        :return: None
        """
        self._station_id = str(station_id).upper() if station_id else False
        self.data = {'stdmet': {}}
        self.station_info = {}

    def __str__(self):
        """
     Overriding the default __str__ method to be a bit more descriptive.
     """
        return "NDBC.DataBuoy Object for Station " + self._station_id

    @staticmethod
    def __check_url__(url) -> bool:
        """
        Verify that the url passed in will return a valid response
        :param url: The url to be checked
        :return: Boolean value indicating whether response status code == 200 
        or not.
        """

        res = requests.head(url)
        return res.status_code == 200

    def set_station_id(self, station_id):
        self._station_id = str(station_id).upper()

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
        for line in str(element).split('\n'):
            if re.search(self.LAT_PAT, line):
                station_metadata['lat'] = re.search(self.LAT_PAT,
                                                line).group()
            if re.search(self.LON_PAT, line):
                station_metadata['lon'] = re.search(
                    self.LON_PAT, line).group()
            if re.search(self.ATTR_PAT, line):
                k, v = re.search(self.ATTR_PAT, line).groups()
                station_metadata[k] = v
        self.station_info = station_metadata

    def get_station_metadata(self) -> None:
        """
        Define method to capture and store station metadata
        :return: None
        """
        if not self._station_id:
            raise LookupError('No station ID provided')
        response = requests.get(self.STATION_URL.format(self._station_id))
        soup = BeautifulSoup(response.content, 'html.parser')
        meta_div = soup.find('div', id='stn_metadata')
        if meta_div:
            for el in meta_div.find_all('p'):
                # Iterate over <p> tags.  One of these will have the station
                # details we are looking for.
                if re.search(self.LAT_PAT, str(el)) \
                        and re.search(self.LON_PAT, str(el)) \
                        and re.search(self.ATTR_PAT, str(el)):
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
        if data.loc[0][0][0] == '#':
            units = data.loc[0]
            columns = data.columns
            data = data.drop([0])
            self.data['stdmet']['meta'] = {}
            self.data['stdmet']['meta']['units'] = {
                k: v for k in columns for v
                in units
            }
        return data

    @staticmethod
    def __format_dates(data: pd.DataFrame) -> pd.DataFrame:
        """
        Read in various datetime column values, strip columns, and return a
        date-tine index with valid Python datetime values.
        :param data: DataFrame containing datetime components in separate
        columns
        :return: DataFrame with datetime components removed and singe
        datetime index appended.
        """
        # Changes in file format over the decades of NDBC operation need to
        # be accounted for
        year_types = ['YY', 'YYYY', '#YY']
        # Next we need to identify the columns relating to our datetime values.
        dt_index_cols = ['#YY', 'MM', 'DD', 'hh']
        # Building a dictionary for datetime formatting options
        dt_format_vals = {'#YY': '%Y', 'MM': '%m', 'DD': '%d', 'hh': '%H'}
        # Earlier files (pre ~2008) didn't include the minute value
        if 'mm' in list(data.columns):
            dt_index_cols.append('mm')
            dt_format_vals['mm'] = '%M'
        # Finding which Year identifier was used in this file
        yt = [x for x in year_types if x in dt_index_cols][0]
        dt_index_cols[0] = yt
        # detecting a two digit year (this stopped around 1996)
        if int(math.floor(math.log(int(data[yt][1]), 10) + 1)) == 2:
            data[yt] = data[yt] + 1900

        # Using our dictionary to build a formatting string for datetime
        dt_format_str = ' '.join([dt_format_vals[x] for x in dt_index_cols])

        # Setting the datetime component columns as our index
        data.set_index(dt_index_cols, inplace=True)
        # Converting tuples of date/time components from columns into Python
        # datetime objects.
        dt_vals = [dt.strptime(' '.join(x), dt_format_str)
                   for x in data.index.values]
        # Setting our index to our datetime list
        data.index = dt_vals
        return data

    def load_stdmet(self, url) -> None:
        """
        Transform NDBC Standard Meterological text data into pandas Dataframe
        and append to results
        :param url: Location of text data
        :return: None
        """
        data_df = pd.read_csv(url, '\s+')
        data_df = self.__separate_units(data_df)
        if 'data' in self.data['stdmet'].keys():
            self.data['stdmet'] = self.data['stdmet']['data'].append(data_df)
        else:
            self.data['stdmet']['data'] = data_df

    def get_stdmet(self, years=[], months=[]) -> Union[None, str]:
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
            valid = False
            my_url = False
            # Looping through potentially available months.
            while month_num >= 0 and not valid:
                month_abbrv = dt(year_num, month_num, 1).strftime('%b')
                my_url = self.STDMET_MONTHURL.format(
                    month=month_abbrv, station=self._station_id)
                valid = self.__check_url__(my_url)
                if not valid:
                    times_unavailable += month_abbrv + " not available.\n "
                # Attempting to deal with January issue
                if month_num == 1:
                    year_num -= 1
                    month_num = 12
                else:
                    month_num -= 1
            if my_url:
                self.load_stdmet(my_url)

        else:
            for year in years:
                my_url = self.STDMET_YEARURL.format(station=self._station_id,
                                                    year=year)
                if self.__check_url__(my_url):
                    self.load_stdmet(my_url)
                else:
                    times_unavailable += 'Year ' + str(
                        year) + ' not available.\n'

            for month in months:
                month_abbrv = dt(dt.today().year, month, 1).strftime('%b')
                my_url = self.STDMET_MONTHURL.format(
                    month=month_abbrv, station=self._station_id)
                if self.__check_url__(my_url):
                    self.load_stdmet(my_url)
                else:
                    times_unavailable += month_abbrv + ' not available.\n'

        if len(times_unavailable) > 0:
            return times_unavailable

    def stdmet_to_json(self, file_name, date_format='iso', orient='columns'):
        """
        Provide method to output data to JSON file.
        :param file_name: name of file to output
        :param date_format: date format that should be applied when writing file
        :param orient: the orientation used to convert DataFrame to JSON
        :return: None
        """

        self.data['stdmet']['data'].to_json(
            file_name, date_format=date_format, orient=orient)

    # TODO (ryan@gensci.org): Build out function to look for values that are
    #  all '9' and replace them with None or NaN to indicate lack of valid data.
