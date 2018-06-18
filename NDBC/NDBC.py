"""
 NDBC.py - this file contains classes pertaining to the acquisition and transformation of National Data Buoy Center (NDBC) oceanographic data.

 Classes:
   DataBuoy - An initial attempt at building out a class for reading and parsing NDBC buoy data.

"""

import requests
from datetime import datetime as dt
import pandas as pd
import math


class DataBuoy:
  """
   This class contains functions used to fetch and parse data from National Data Buoy Center stations.

  Attributes:
    - station_id (str): The numeric identifier of the data buoy this class
      will represent.


  Methods/Functions:
    - load_stdmet(url):  Loads the data from the text file found with the
      given url into a pandas dataframe and appends in to the data['stdmet']
      dataframe.

    - get_stdmet(years, months): Collects standard meteorological summary data
      for the time periods specified and stores it as a pandas dataframe in
      the data attribute.

  Example:
  ``
    >>>from NDBC.NDBC import DataBuoy


    >>>N42 = DataBuoy('46042')
    >>>N42.get_stdmet()
    'Jun not available.\n'
    >>>N42.data
    {'stdmet':       WDIR  WSPD   GST  WVHT  ...    WTMP   DEWP   VIS   TIDE
2018-04-30 23:50:00  309   9.6  11.6  2.84  ...    12.6  999.0  99.0  99.00
2018-05-01 00:50:00  314  10.5  12.8  3.28  ...    12.8  999.0  99.0  99.00
2018-05-01 01:50:00  317  11.1  13.3  3.14  ...    12.8  999.0  99.0  99.00
2018-05-01 02:50:00  320  11.6  14.3  3.22  ...    12.8  999.0  99.0  99.00
2018-05-01 03:50:00  321  11.6  13.5  3.31  ...    12.8  999.0  99.0  99.00
2018-05-01 04:50:00  323  11.4  13.5  3.53  ...    12.7  999.0  99.0  99.00
2018-05-01 05:50:00  323  10.9  12.9  3.46  ...    12.5  999.0  99.0  99.00
2018-05-01 06:50:00  319  10.9  13.4  3.55  ...    12.5  999.0  99.0  99.00
2018-05-01 07:50:00  317   8.9  11.4  3.85  ...    12.5  999.0  99.0  99.00
2018-05-01 08:50:00  306   8.5  11.0  3.94  ...    12.6  999.0  99.0  99.00
2018-05-01 09:50:00  312   9.4  12.0  3.62  ...    12.6  999.0  99.0  99.00
2018-05-01 10:50:00  313   9.6  12.1  3.42  ...    12.6  999.0  99.0  99.00
2018-05-01 11:50:00  314  10.0  11.9  3.37  ...    12.6  999.0  99.0  99.00
2018-05-01 12:50:00  318   9.4  11.1  3.55  ...    12.6  999.0  99.0  99.00
2018-05-01 13:50:00  317   9.9  12.0  3.36  ...    12.6  999.0  99.0  99.00
2018-05-01 14:50:00  328   9.2  10.7  3.11  ...    12.5  999.0  99.0  99.00
2018-05-01 15:50:00  324   8.9  10.4  3.17  ...    12.5  999.0  99.0  99.00
2018-05-01 16:50:00  335   9.6  11.1  3.25  ...    12.5  999.0  99.0  99.00
2018-05-01 17:50:00  327   9.7  11.6  3.26  ...    12.5  999.0  99.0  99.00
2018-05-01 18:50:00  332   9.6  11.8  3.16  ...    12.5  999.0  99.0  99.00
2018-05-01 19:50:00  318   9.5  12.1  3.22  ...    12.6  999.0  99.0  99.00
2018-05-01 20:50:00  310   9.7  11.6  3.11  ...    12.6  999.0  99.0  99.00
2018-05-01 21:50:00  311   9.5  11.1  2.94  ...    12.6  999.0  99.0  99.00
2018-05-01 22:50:00  314   9.3  10.9  3.13  ...    12.7  999.0  99.0  99.00
2018-05-01 23:50:00  311   8.7  10.5  2.72  ...    12.7  999.0  99.0  99.00
2018-05-02 00:50:00  306   9.5  11.2  2.90  ...    12.7  999.0  99.0  99.00
2018-05-02 01:50:00  307   9.5  11.8  2.86  ...    12.7  999.0  99.0  99.00
2018-05-02 02:50:00  311   8.5  10.4  2.68  ...    12.6  999.0  99.0  99.00
2018-05-02 03:50:00  313   8.9  10.4  2.44  ...    12.6  999.0  99.0  99.00
2018-05-02 04:50:00  321   8.5  10.8  2.51  ...    12.6  999.0  99.0  99.00
...                  ...   ...   ...   ...  ...     ...    ...   ...    ...
2018-05-30 17:50:00  320   8.4  10.3  3.22  ...    11.5  999.0  99.0  99.00
2018-05-30 18:50:00  317   8.2   9.9  3.09  ...    11.5  999.0  99.0  99.00
2018-05-30 19:50:00  318   7.5   9.0  3.46  ...    11.7  999.0  99.0  99.00
2018-05-30 20:50:00  311   7.4   9.0  3.66  ...    12.0  999.0  99.0  99.00
2018-05-30 21:50:00  310   7.6   9.2  3.16  ...    12.1  999.0  99.0  99.00
2018-05-30 22:50:00  308   7.0   8.6  3.13  ...    12.3  999.0  99.0  99.00
2018-05-30 23:50:00  308   7.2   8.9  2.85  ...    12.4  999.0  99.0  99.00
2018-05-31 00:50:00  310   6.8   8.3  2.62  ...    12.5  999.0  99.0  99.00
2018-05-31 01:50:00  315   7.4   9.1  2.46  ...    12.6  999.0  99.0  99.00
2018-05-31 02:50:00  311   8.6  10.4  2.69  ...    12.6  999.0  99.0  99.00
2018-05-31 03:50:00  314   8.6  10.4  2.45  ...    12.6  999.0  99.0  99.00
2018-05-31 04:50:00  315   8.7  10.8  2.46  ...    12.5  999.0  99.0  99.00
2018-05-31 05:50:00  315   7.7   9.4  2.54  ...    12.5  999.0  99.0  99.00
2018-05-31 06:50:00  312   9.6  12.5  2.49  ...    12.5  999.0  99.0  99.00
2018-05-31 07:50:00  311   8.6  10.5  2.39  ...    12.5  999.0  99.0  99.00
2018-05-31 08:50:00  309   8.5  11.4  2.26  ...    12.5  999.0  99.0  99.00
2018-05-31 09:50:00  306   8.6  10.3  2.54  ...    12.4  999.0  99.0  99.00
2018-05-31 10:50:00  307   9.1  10.7  2.53  ...    12.4  999.0  99.0  99.00
2018-05-31 11:50:00  308   7.8   9.5  2.58  ...    12.4  999.0  99.0  99.00
2018-05-31 12:50:00  309   8.1   9.7  2.55  ...    12.4  999.0  99.0  99.00
2018-05-31 13:50:00  304   8.1  10.0  2.51  ...    12.3  999.0  99.0  99.00
2018-05-31 14:50:00  308   8.7  10.6  2.36  ...    12.4  999.0  99.0  99.00
2018-05-31 15:50:00  309   9.0  11.7  2.34  ...    12.4  999.0  99.0  99.00
2018-05-31 16:50:00  309   8.1   9.5  2.38  ...    12.4  999.0  99.0  99.00
2018-05-31 17:50:00  315   8.1   9.6  2.27  ...    12.5  999.0  99.0  99.00
2018-05-31 18:50:00  309   7.8   9.6  2.24  ...    12.5  999.0  99.0  99.00
2018-05-31 19:50:00  309   7.5   9.7  2.20  ...    12.6  999.0  99.0  99.00
2018-05-31 20:50:00  305   8.1   9.4  2.11  ...    12.7  999.0  99.0  99.00
2018-05-31 21:50:00  303   8.4   9.9  2.19  ...    12.7  999.0  99.0  99.00
2018-05-31 22:50:00  304   9.3  11.4  2.02  ...    12.8  999.0  99.0  99.00

[742 rows x 13 columns]}
  ``
  """

  # Defining some template strings as class variables that will be
  # used to define specific data URLS for each instance.
  STDMET_MONTHURL = 'https://www.ndbc.noaa.gov/data/stdmet/{month}/{station}.txt'

  STDMET_YEARURL = 'https://www.ndbc.noaa.gov/view_text_file.php?filename={station}h{year}.txt.gz&dir=data/historical/stdmet/'

  def __init__(self, station_id='46042'):
    """
    An initializing function to set our default data.
    """
    self.station_id = str(station_id)
    self.data = {'stdmet': pd.DataFrame([])}

  def __str__(self):
     """
     Overriding the default __str__ method to be a bit more descriptive.
     """
     return "NDBC.DataBuoy Object for Station " + self.station_id

  def __checkurl__(self, url):
    """
    A simple encapsulation of using a HEAD request to check the validity of a
    URL.
    Args:
       url(str) - the URL to checked
    Returns:
       url_is_valid(bool) - A boolean value indicating the validity of this URL
    """

    res = requests.head(url)
    return res.status_code == 200

  def load_stdmet(self, url):
    """
    The function that does the actual loading of the stdmet data into the
    instance data attribute.
    """
    year_types = ['YY', 'YYYY', '#YY']
    data_df = pd.read_csv(url, '\s+')
    # We check to see if the first row is the units - true after 2009.
    if data_df.loc[0][0][0] == '#':
      units = data_df.loc[0]
      data_df = data_df.drop([0])
    # Next we need to identify the columns relating to our datetime values.
    dt_index_cols = ['#YY', 'MM', 'DD', 'hh']
    dt_format_vals = {'#YY': '%Y', 'MM': '%m', 'DD': '%d', 'hh': '%H'}
    if 'mm' in list(data_df.columns):
      dt_index_cols.append('mm')
      dt_format_vals['mm'] = '%M'
    # Since we may be dealing with historical data files that were weird
    # in their definition of year values
    yt = [x for x in year_types if x in dt_index_cols][0]
    dt_index_cols[0] = yt
    # detecting a two digit year (this stopped around 1996)
    if int(math.floor(math.log(int(data_df[yt][1]),10) + 1)) == 2:
      data_df[yt] = data_df[yt] + 1900
    # Using our dictionary to build a formatting string for datetime
    dt_format_str = ' '.join([dt_format_vals[x] for x in dt_index_cols])
    # Setting the datetime component columns as our index
    data_df.set_index(dt_index_cols, inplace=True)
    # Converting tuples of date/time components from columns into Python datetime objects.
    dt_vals = [dt.strptime(' '.join(x), dt_format_str)
               for x in data_df.index.values]
    # Setting our index to our datetime list
    data_df.index = dt_vals

    self.data['stdmet'] = self.data['stdmet'].append(data_df)

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
    # If no timeframe is specified we retrieve the most current complete month for the given station.
    if not years and not months:
      month_num = dt.today().month
      valid = False
      # Looping through potentially available months.
      while month_num >= 0 and not valid:
        month_abbrv = dt(dt.today().year, month_num, 1).strftime('%b')
        my_url = self.STDMET_MONTHURL.format(
            month=month_abbrv, station=self.station_id)
        valid = self.__checkurl__(my_url)
        # TODO (ryan@gensci.org): Figure out how to deal with early January edge case without raising pontential for infinite loop.
        if not valid:
          times_unavailable += month_abbrv + " not available.\n "
        month_num -= 1

      self.load_stdmet(my_url)

    else:
      for year in years:
        my_url = self.STDMET_YEARURL.format(station=self.station_id, year=year)
        if self.__checkurl__(my_url):
          self.load_stdmet(my_url)
        else:
          times_unavailable += 'Year ' + str(year) + ' not available.\n'

      for month in months:
        month_abbrv = dt(dt.today().year, month, 1).strftime('%b')
        my_url = self.STDMET_MONTHURL.format(
            month=month_abbrv, station=self.station_id)
        if self.__checkurl__(my_url):
          self.load_stdmet(my_url)
        else:
          times_unavailable += month_abbrv + ' not available.\n'

    if len(times_unavailable) > 0:
        return times_unavailable

  def stdmet_to_json(self, file_name, date_format='iso', orient='columns'):
    """
    A simple method for outputing the existing stdmet data to a json file
    """

    self.data['stdmet'].to_json(
        file_name, date_format=date_format, orient=orient)

  # TODO (ryan@gensci.org): Build out function to look for values that are all '9' and replace them with None or NaN to indicate lack of valid data.
