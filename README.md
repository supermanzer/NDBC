# NDBC

![alt text](http://www.ndbc.noaa.gov/images/nws/noaaleft.jpg "NOAA") ![alt text](http://www.ndbc.noaa.gov/images/nws/ndbc_title.jpg "NDBC")

This repository represents my attempts to build out Python class(es)
to facilitate the acquisition, analysis, and visualization of National
Data Buoy Center (NDBC) data. The goal is to develop a set of APIs to
facilitate rapid discovery of data resources, exploratory data analysis,
and allow integration into automated data workflows.

## NDBC.py

This file defines the DataBuoy class. The purpose of this class is to
allow a user to define a specific data buoy they wish to gather data
from and provide the user with methods to collect and analyze this data.

Dependencies are listed in `requirements.txt`

## Usage

#### Installation

Install using pip from PyPI

```
pip install NDBC
```

Then you are ready to start using this module in exploratory data analyses and scripted workflows.

#### Methods of DataBuoy Class

`.set_station_id`

If a DataBuoy class has been instantiated without any `station_id` argument, this method allows for setting a station id

```
from NDBC.NDBC import DataBuoy
DB = DataBuoy()
DB.set_station_id('46042') # <- Either strings or numbers are acceptable
```

`.get_station_metadata()`

Perform a scrape of the public webpage for a specified data station and save a dictionary of available metadata to the `.station_info` property. This is only available if a DataBuoy has a valid `station_id` set (either during class instantiation or using
the `set_station_id` method).

```
from NDBC.NDBC import DataBuoy
DB = DataBuoy(46042)
DB.get_station_metadata()
DB.station_info
{   'Air temp height': '4 m above site elevation',
    'Anemometer height': '5 m above site elevation',
    'Barometer elevation': 'sea level',
    'Sea temp depth': '0.6 m below water line',
    'Site elevation': 'sea level',
    'Watch circle radius': '1789 yards',
    'Water depth': '1645.9 m',
    'lat': '36.785 N',
    'lon': '122.398 W'}
```

- `.get_stdmet(datetime_index=False)`

After importing, the DataBuoy class is instantiated with the ID of the
station from which historical data is sought. Then data may be gathered for
the years and months specified. If no time period is specified, the most recent
full month available is retrieved.

The default behavior is to append datetime values built from date part columns (YY, MM, DD, etc.) to a column 'datetime'. If value `True` is passed as the `datetime_index` argument, the datetime values will be used as index values for the returned dataframe. In some cases this is advantageous for time series analyses.

```
from NDBC.NDBC import DataBuoy

n42 = DataBuoy(46042)  # <- String or numeric station ids are valid

n42.get_stdmet(datetime_index=True)  # <- no year, month argumets so latest full month is retrieved.

Oct not available.   # <- Where data is missing, messages are returned to the terminal via a logger.warning() call
Sep not available.

n42.data  # <- anticipating additional data collection methods, the .data property returns a dictionary.  Indiviudual
               data products are returned as pandas DataFrame objects

# Datetime objects are compiled from individual year, month, day, hour, minute columns and used as the index to support
# slicing data by time frames.

{'stdmet':          WDIR WSPD  GST  WVHT    DPD   APD  MWD    PRES  ATMP  WTMP   DEWP   VIS   TIDE
2019-07-31 23:50:00  298  3.6  5.2  1.25   7.69  5.37  303  1015.1  13.4  15.2  999.0  99.0  99.00
2019-08-01 00:50:00  301  5.7  7.2  1.26   7.14  5.42  306  1014.8  13.4  15.3  999.0  99.0  99.00
2019-08-01 01:50:00  323  6.6  8.3  1.33   7.14  5.47  312  1014.5  13.2  15.1  999.0  99.0  99.00
2019-08-01 02:50:00  347  5.8  7.7  1.32   7.69  5.15  319  1014.5  12.7  15.1  999.0  99.0  99.00
2019-08-01 03:50:00  353  5.6  7.2  1.26   7.69  5.31  325  1014.9  12.6  15.0  999.0  99.0  99.00
...                  ...  ...  ...   ...    ...   ...  ...     ...   ...   ...    ...   ...    ...
2019-08-31 18:50:00  999  6.2  7.4  0.87  13.79  4.67  186  1014.6  17.0  17.2  999.0  99.0  99.00
2019-08-31 19:50:00  999  6.8  8.3  0.83  13.79  4.56  178  1014.2  17.2  17.3  999.0  99.0  99.00
2019-08-31 20:50:00  999  6.5  7.8  0.89  13.79  4.38  195  1013.8  17.5  17.4  999.0  99.0  99.00
2019-08-31 21:50:00  999  7.5  8.9  0.95  13.79  4.52  190  1013.1  17.5  17.3  999.0  99.0  99.00
2019-08-31 22:50:00  999  8.0  9.4  0.95  13.79  4.09  171  1012.7  17.7  17.1  999.0  99.0  99.00

[741 rows x 13 columns]}
```

By default the `get_stdmet` function will fetch the most current month's data. However, the function can take lists of years & months ([int]) to specify a timeframe.

```
n42 = NDBC.DataBuoy('46042')
n42.get_stdmet(years=range(2010, 20202), datetime_index=True)
n42.data['stdmet']['data']
                    WDIR WSPD  GST  WVHT    DPD   APD  MWD    PRES  ATMP  WTMP  DEWP  VIS  TIDE
2009-12-31 23:50:00  126  3.3  4.4  1.58  11.43  8.42  281  1026.3   NaN  13.1   NaN  NaN   NaN
2010-01-01 00:50:00  240  0.7  1.0  1.80  11.43  8.72  289  1026.8   NaN  13.1   NaN  NaN   NaN
2010-01-01 01:50:00  180  0.1  0.4  1.64  12.12  8.76  286  1027.2   NaN  13.0   NaN  NaN   NaN
2010-01-01 02:50:00   94  2.2  3.0  1.66  11.43  8.66  281  1027.4   NaN  13.0   NaN  NaN   NaN
2010-01-01 03:50:00   91  0.9  1.5  1.48  12.12  8.43  277  1028.1   NaN  13.0   NaN  NaN   NaN
...                  ...  ...  ...   ...    ...   ...  ...     ...   ...   ...   ...  ...   ...
2019-12-31 23:10:00  323  5.5  7.7   NaN    NaN   NaN  NaN  1020.5  13.5  13.7  11.8  NaN   NaN
2019-12-31 23:20:00  323  4.7  6.4   NaN    NaN   NaN  NaN  1020.3  13.6  13.7  11.9  NaN   NaN
2019-12-31 23:30:00  321  4.1  6.2   NaN    NaN   NaN  NaN  1020.2  13.6  13.7  11.9  NaN   NaN
2019-12-31 23:40:00  316  4.4  6.8  3.82  13.79  9.82  290  1020.1  13.6  13.7  11.8  NaN   NaN
2019-12-31 23:50:00  315  4.5  6.9   NaN    NaN   NaN  NaN  1020.2  13.6  13.7  11.9  NaN   NaN

[92354 rows x 13 columns]
```

Using the pandas DataFrame to store the returned data provides access to the wide array of methods the pandas package
provides.

- `.save(filename(optional))`

Saves an instantiated DataBuoy object as JSON to a file. If `filename` is not specified the file name will follow the
`databuoy_{station_id}.json` convention.

```
db = DataBuoy(46042)
db.save('/path/to/file/my_filename.json')
```

_classmethod_

- `.load(filename)`
  Instantiate a DataBuoy object from a file, generated by the `.save()` method.

```
db = DataBuoy.load('/path/to/file.json')
```
