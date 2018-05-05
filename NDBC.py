"""
 NDBC.py - this file contains classes pertaining to the acquisition and transformation of National Data Buoy Center (NDBC) oceanographic data.

 Classes:
   DataBuoy - An initial attempt at building out a class for reading and parsing NDBC buoy data.

"""

import requests
import json
from datetime import datetime as dt
import pandas as pd


class DataBuoy:
  """
   This class contains functions used to fetch and parse data from National Data Buoy Center stations.

  Attributes:
    station_id (str): The numeric identifier of the data buoy whose data is to be gathered for plotting.
    file_name (str): The name of the file to be generated when writing out data.

   Methods/Functions:
    stdmet_to_json: This function gathers (via HTTP GET request) the most recent standard meteorological summary from NDBC data buoy and converts the text file into a python dictionary which is then stringified into a JSON file.
  """

  __BASEURL__ = 'http://www.ndbc.noaa.gov/data/stdmet/{month}/{station}.txt'

  def __init__(self, station_id='46042', file_name='stdmet.json'):
     """
     An initializing function to set our default data.
     """
     self.station_id = station_id
     self.file_name = file_name

  def set_ndbc(self, station_id):
     """
     Allows interactive setting of NDBC station id.

     Args:
         station_id (str): The numeric station id for a specific data
         buoy.
     Returns:
         None
     """
     self.station_id = station_id

  def set_outfile(self, filename):
     """
     Allows interactive setting of output file name.

     Args:
         filename: The name of the file to be returned by the
         stdmet_to_json function.
     Returns:
         None
     """
     self.file_name = filename


  def stdmet_to_json(self, orient='index', date_format='iso'):
     """
     This method uses the current date and the NDBC_DB value to collect
     the most recent standard meteorological summary from the National
     Data Buoy Center (NDBC).  It converts the text returned into a
     Python dictionary which is then saved as a JSON file.  The
     filename is set by the file_name property.

     Args:
       orient: the orientation of the JSON object produced from the Pandas DataFrame.  Default is index.
       date_format: The format of the datetime string that will be output to the JSON file.  Default is iso.

     Returns:
         None but file (identified by file_name) is saved to current directory.
     """

     month_num = dt.today().month

     url_is_valid = False
     # Looping through potentially available months.
     while month_num >=0 and not url_is_valid:
         month_abbrv = dt(dt.today().year, month_num, 1).strftime('%b')
         my_url = self.__BASEURL__.format(month=month_abbrv, station=self.station_id)
         res = requests.head(my_url)
         if res.status_code == 200:
             data_df = pd.read_csv(my_url, '\s+')
             url_is_valid = True
         month_num -= 1
    # Now we have our data in a pandas dataframe.  However, our first
    # row is actually units and our datetime components are broken out
    # into individual columns.  This is less than desirable as we might
    # like to do some time series operations that expect datetime
    # objects.

    # We check to make sure the first row is the units.
     if data_df.loc[0][0][0] == '#':
         units = data_df.loc[0]
         data_df = data_df.drop([0]) # We need to remove this so our vector operations can proceed.
     # Building a list of column names and a dictionary mapping them to
     # string formatting parameters.
     dt_index_cols = ['#YY', 'MM', 'DD', 'hh']
     dt_format_vals = {'#YY': '%Y', 'MM': '%m', 'DD': '%d', 'hh': '%H'}

     if 'mm' in list(data_df.columns):
         dt_index_cols.append('mm')
         dt_format_vals['mm'] = '%M'
     # Using our dictionary to build a formatting string for datetime
     dt_format_str = ' '.join([dt_format_vals[x] for x in dt_index_cols])

     # Setting the datetime component columns as our index
     data_df.set_index(dt_index_cols, inplace=True)
     # Converting tuples of date/time components from columns into Python datetime objects.
     dt_vals = [dt.strptime(' '.join(x), dt_format_str) for x in data_df.index.values]
     # Setting our index to our datetime list
     data_df.index = dt_vals
     data_df.to_json(self.file_name, date_format=date_format, orient=orient)
