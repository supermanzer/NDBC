"""
 NDBC.py - this file contains classes pertaining to the acquisition and transformation of National Data Buoy Center (NDBC) oceanographic data.

 Classes:
   DataBuoy - An initial attempt at building out a class for reading and parsing NDBC buoy data.

"""

import requests
from datetime import datetime as dt
import pandas as pd
import numpy as np


class DataBuoy:
  """
   This class contains functions used to fetch and parse data from National Data Buoy Center stations.

  Attributes:
    station_id (str): The numeric identifier of the data buoy this class will
    represent.


   Methods/Functions:
    get_stdmet(years, months): Collects standard meteorological summary data
    for the time periods specified and stores it as a pandas dataframe in the
    data attribute.

  """

  # Defining some template strings as class variables that will be
  # used to define specific data URLS for each instance.
  STDMET_MONTHURL = 'https://www.ndbc.noaa.gov/data/stdmet/{month}/{station}.txt'

  STDMET_YEARURL = 'https://www.ndbc.noaa.gov/view_text_file.php?filename={station}h{year}.txt.gz&dir=data/historical/stdmet/'

  def __init__(self, station_id='46042'):
    """
    An initializing function to set our default data.
    """
    self.station_id = station_id
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
    url_is_valid = False
    res = requests.head(url)
    if res.status_code == 200:
      url_is_valid = True
    return url_is_valid

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
    if int(np.floor(np.log10(int(data_df[yt][1])) + 1)) == 2:
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
    import pdb; pdb.set_trace()
    recent = False
    times_unavailable = ""
    if not years and not months:
      recent = True

    if recent:
      month_num = dt.today().month
      valid = False
      # Looping through potentially available months.
      while month_num >= 0 and not valid:
        month_abbrv = dt(dt.today().year, month_num, 1).strftime('%b')
        my_url = self.STDMET_MONTHURL.format(
            month=month_abbrv, station=self.station_id)
        valid = self.__checkurl__(my_url)
        # TODO: Figure out how to deal with early January edge case without raising pontential for infinite loop.
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
