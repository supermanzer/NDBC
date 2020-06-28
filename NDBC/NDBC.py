"""
 NDBC.py - this file contains classes pertaining to the acquisition and
 transformation of National Data Buoy Center (NDBC) oceanographic data.

 Classes:
   DataBuoy - An initial attempt at building out a class for reading and
   parsing NDBC buoy data.

"""

import requests
import pandas as pd
import json
import re
import numpy as np

from datetime import datetime as dt
from bs4 import BeautifulSoup


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
    LAT_PAT = r"\d+\.\d+\s+N"
    LON_PAT = r"\d+\.\d+\s+W"
    ATTR_PAT = r"<b>(.*):</b>\s*(.*)<br/>"
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
            self.station_id = str(station_id)
        self.data = {"stdmet": {}}

    def set_station_id(self, station_id):
        self.station_id = str(station_id).upper()

    def __str__(self):
        """
     Overriding the default __str__ method to be a bit more descriptive.
     """
        return "NDBC.DataBuoy Object for Station " + self.station_id

    @staticmethod
    def __check_urls__(urls):
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
    def __build_urls__(urls, format_kwargs):
        return [url.format(**format_kwargs) for url in urls]

    @staticmethod
    def _bad_data_func(x, n):
        """
        Check an individual value from NDBC data files to see if it meets the
        standard for NDBC bad data flag.
        :param x: The value being checked
        :param n: the max length of the values for a given metric.
        :return: Value if valid, None if not.
        """
        val = np.NaN if all([d == '9' for d in str(int(float(x)))]) and len(
            x) == n else x
        return val

    def _bad_data_check(self, df, datetime_index):
        """Replace NDBC bad data flag with NumPy NaN"""
        cols = df.columns.to_list()
        if not datetime_index:
            cols.remove('datetime')

        for col in cols:
            n = len(df[col].max())
            df[col] = df[col].apply(self._bad_data_func, n=n)
        return df

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
        if not hasattr(self, 'station_id'):
            raise LookupError("No station ID provided")
        response = requests.get(self.STATION_URL.format(self.station_id))
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
        data_df = pd.read_csv(url, r"\s+")
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
        # Replacing NDBC bad data flags with Numpy NaNs
        data_df = self._bad_data_check(data_df, datetime_index)
        # Append to existing stdmet dataframe if exists
        if "data" in self.data["stdmet"].keys():
            self.data["stdmet"]["data"] = self.data["stdmet"]["data"].append(
                data_df)
        # otherwise assign dataframe to stdment['data']
        else:
            self.data["stdmet"]["data"] = data_df

    def get_stdmet(self, years=[], months=[],
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
        try:
            if not years and not months:
                month_num = dt.today().month
                year_num = dt.today().year
                my_url = False
                # Looping through potentially available months.
                while not my_url:
                    month_abbrv = dt(year_num, month_num, 1).strftime("%b")
                    kws = {"month_abbrv": month_abbrv, "month_num": month_num,
                           "station": self.station_id, "year": year_num}
                    my_url = self.__check_urls__(
                        self.__build_urls__(self.stdmet_monthurls, kws)
                    )
                    if not my_url:
                        times_unavailable += f"{month_abbrv} {year_num} not " \
                                             f"available.\n "

                    month_num -= 1
                    # !st attempt to deal with January edge case
                    if month_num == 0:
                        year_num -= 1
                        month_num = 12
                if my_url:
                    self.load_stdmet(my_url, datetime_index)
            else:
                for year in years:
                    kws = {"year": year, "station": self.station_id}
                    my_url = self.__check_urls__(
                        self.__build_urls__(self.stdmet_yearurls, kws)
                    )
                    if my_url:
                        self.load_stdmet(my_url, datetime_index)
                    else:
                        times_unavailable += "Year " + \
                            str(year) + " not available.\n"

                for month in months:
                    month_abbrv = dt(dt.today().year, month, 1).strftime("%b")
                    year = dt.today().year
                    kws = {
                        "year": year,
                        "month_abbrv": month_abbrv,
                        "month_num": month,
                        "station": self.station_id,
                    }
                    my_url = self.__check_urls__(
                        self.__build_urls__(self.stdmet_monthurls, kws)
                    )
                    if my_url:
                        self.load_stdmet(my_url, datetime_index)
                    else:
                        times_unavailable += month_abbrv + " not available.\n"

            if len(times_unavailable) > 0:
                logger.warning(times_unavailable)

        except requests.exceptions.SSLError as e:
            logger.error(f'NDBC Server unavailable: {e}')

    # -------------------- STATION SEARCH METHODS ------------------------------
    # https: // www.ndbc.noaa.gov / radial_search.php?lat1 = 36.79 & lon1 = \
      #  -122.4 & uom = M & dist = 50 & ot = B & time = -1
    # URL generated for radial search lat = 36.79, lon = -122.4,
    # uom = Metric, distance = 50 km, observation type = moored buoy, time =
    # t - 1 hour

    # https: // www.ndbc.noaa.gov / radial_search.php?lat1 = 36.79 & lon1 =
    # -122.4 & uom = E & dist = 50 & ot = B & time = 1
    # URL generated for radial search with uom = English, distance = 50
    # miles, observation type = moored buoy, time = within the past 1 hour.

    # https://www.ndbc.noaa.gov/box_search.php?lat1=36.785+N&lat2=37.125+N&
    # lon1=-122.4&lon2=-121.4&uom=M&ot=A&time=1
    # URL box search with Metric measurements in the past hour
    SEARCH_TYPES = {
        'radial': 'radial_search.php',
        'box': 'box_search.php'
    }
    UOMS = {
        'metric': "M",
        'english': "E"
    }
    OBS_TYPES = {
        'buoy': "B",
        'ship': 'S',
        'all': 'A'
    }

    def _ss_args_check(self, search_type='radial', lat1=False,
                       lat2=False, lon1=False, lon2=False, uom='metric',
                       time=1, obs_type='buoy', distance=False):
        """Station Search arguments checking"""
        if search_type not in self.SEARCH_TYPES.keys():
            raise ValueError(f'Invalid search type. Please use one of the '
                             f'following: {", ".join(self.SEARCH_TYPES.keys())}')
        if uom not in self.UOMS.keys():
            msg = f'Invalid UOM. Please use one of the following: ' \
                  f'{", ".join(self.UOMS.keys())}'
            raise ValueError(msg)
        if obs_type not in self.OBS_TYPES.keys():
            msg = f'Invalid observation type.  Please use one of the ' \
                  f'following: {", ".join(self.OBS_TYPES.keys())}'
            raise ValueError(msg)
        if type(time) != int or abs(time) > 23:
            raise ValueError('Time arg must be an integer with an absolute '
                             'value of 23 or less.')
        # ASSIGNING LAT1 AND LON1
        lat1 = lat1 if lat1 else (self.station_info['lat'] if self.station_info[
            'lat'] else False)
        lon1 = lon1 if lon1 else (self.station_info['lon'] if self.station_info[
            'lon'] else False)

        # VALIDATING COORDINATES/ARGS FOR SEARCH TYPES
        if search_type == 'radial' and not all([lat1, lon1, distance]):
            raise ValueError('Radial search requires lat, lon, and distance.')
        if search_type == 'box' and not all([lat1, lat2, lon1, lon2]):
            raise ValueError('Box search requires two lat and lon pairs.')

        return lat1, lon1

    def _ss_build_url(
            self, search_type, lat1, lat2=False, lon1=False, lon2=False,
            uom='metric', time=1, obs_type='buoy', distance=False):

        search_url = f'{self.BASE_URL}{self.SEARCH_TYPES[search_type]}?'

        if search_type == 'radial':
            search_url += f'lat1={lat1}&lon1={lon1}&uom=' \
                          f'{self.UOMS[uom]}&dist={distance}&ot=' \
                          f'{self.OBS_TYPES[obs_type]}&time={time}'
        elif search_type == 'box':
            search_url += f'lat1={lat1}&lat2={lat2}&lon1={lon1}&lon2={lon2}'
            search_url += f'&uom={self.UOMS[uom]}&ot={self.OBS_TYPES[obs_type]}'
            search_url += f'&time={time}'

        return search_url

    def _ss_parse_response(self, url):
        """
        Make request using URL provided and parse the response for a list of
        unique station IDs.
        """
        response = requests.get(url)
        # Checking the validity of our response
        if response.status_code != 200:
            raise ValueError(f'The url generated \n {url} \n returned a '
                             f'status code of {response.status_code}')
        # Parsing the HTML returned
        soup = BeautifulSoup(response.content, 'html.parser')
        # The station IDs returned by this search are all contained within
        # <a> elements that include links to the station pages.  We can use
        # this to find them.
        station_anchors = soup.find_all(href=re.compile('station_page.php'))
        station_ids = set([a.text for a in station_anchors if int(a.text) !=
                           int(self.station_id)])
        return station_ids

    def station_search(self, search_type='radial', lat1=False,
                       lat2=False, lon1=False, lon2=False, uom='metric',
                       time=1, obs_type='buoy', distance=False):
        """
        Station search function.  Defaults to radial search.  Uses lat/lon
        coordinates if supplied, otherwise will default to the coordinates of
        the DataBuoy instance (if available).  UOM determines which distance
        unit is used (defaults to metric) and time determines the time offset
        in which measurements must have occurred for a station to be
        included.  Obs_type determines the type of stations to be included (
        buoy: moored buoy, ship: Ships and drifters, all: All station types).
        Distance determines how wide an area to include (only applies to
        radial search).
        """
        # CHECKING ARGS BEFORE WE START DOING ANYTHING FANCY
        lat1, lon1 = self._ss_args_check(search_type, lat1, lat2, lon1, lon2,
                                         uom, time, obs_type, distance)
        # OKAY, LET'S BEGIN
        url = self._ss_build_url(search_type, lat1, lat2, lon1, lon2, uom,
                                 time, obs_type, distance)
        ids = self._ss_parse_response(url)
        return ids

    # ------------------ DATA PERSISTENCE METHODS -----------------------------
    def stdmet_to_json(self, file_name, date_format="iso", orient="columns"):
        """
        A simple method for returning the existing stdmet data to a json file
        """
        self.data["stdmet"]['data'].to_json(
            file_name, date_format=date_format, orient=orient)

    def save(self, filename=False, orient='records', date_format='iso'):
        file_name = filename if filename else f"data_buoy_" \
                                              f"{self.station_id}.json"
        # Converting stdmet data attribute to JSON for object serialization
        if self.data['stdmet']:
            self.data['stdmet']['meta']['orient'] = orient
            self.data['stdmet']['meta']['date_format'] = date_format
            self.data['stdmet']['data'] = self.data['stdmet']['data'].to_json(
                orient=orient,
                date_format=date_format)
        # converting object attributes to a dictionary
        obj_vals = self.__dict__
        # Converting our dictionary to a valid JSON string
        obj_str = json.dumps(obj_vals)
        # Writing our data to the filename specified
        with open(file_name, 'w+') as f:
            f.write(obj_str)

    @classmethod
    def load(cls, filename):
        file_str = open(filename, 'r').read()
        obj = json.loads(file_str)
        if obj['data']['stdmet'].get('data', False):
            orient = obj['data']['stdmet']['meta']['orient']
            obj['data']['stdmet']['data'] = pd.read_json(
                obj['data']['stdmet']['data'],
                orient=orient)
        inst = cls()
        for k, v in obj.items():
            inst.__setattr__(k, v)
        return inst
