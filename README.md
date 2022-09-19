# NDBC

![alt text](http://www.ndbc.noaa.gov/images/nws/noaaleft.jpg "NOAA") ![alt text](http://www.ndbc.noaa.gov/images/nws/ndbc_title.jpg "NDBC")

[Documentation](https://supermanzer.github.io/NDBC/html/index.html)

This repository represents my attempts to build out Python class(es)
to facilitate the acquisition, analysis, and visualization of National
Data Buoy Center (NDBC) data. The goal is to develop a set of APIs to
facilitate rapid discovery of data resources, exploratory data analysis,
and allow integration into automated data workflows.

## NDBC.py

This file defines the DataBuoy class. The purpose of this class is to
allow a user to define a specific data buoy they wish to gather data
from and provide the user with methods to collect and analyze this data.



## Usage

#### Installation

Install using pip from PyPI

```
pip install NDBC
```

Then you are ready to start using this module in exploratory data analyses and scripted workflows.

#### Methods of DataBuoy Class

`.set_station_id`

If a DataBuoy class has been instantiated without any `station_id` parameter, this method allows for setting a station id

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

- `.get_data(datetime_index=False)`

After importing, the DataBuoy class is instantiated with the ID of the
station from which historical data is sought. Then data may be gathered for
the years and months specified. If no time period is specified, the most recent
full month available is retrieved.

The default behavior is to append datetime values built from date part columns (YY, MM, DD, etc.) to a column 'datetime'. If value `True` is passed as the `datetime_index` argument, the datetime values will be used as index values for the returned dataframe. In some cases this is advantageous for time series analyses.

```
from NDBC.NDBC import DataBuoy

n42 = DataBuoy(46042)  # <- String or numeric station ids are valid

n42.get_data(datetime_index=True)  # <- no year, month argumets so latest full month is retrieved. Default data type is 'stdmet'

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

By default the `get_data()` function will fetch the most current month's data. However, the function can take lists of years & months ([int]) to specify a time-frame.

```
$ n42 = NDBC.DataBuoy('46042')
$ n42.get_data(months=[1,2], years=range(2019, 2020), datetime_index=True, data_type='swden)
Year 2019 not available.
Year 2020 not available.
 
$ n42.data
{'swden': {'data':                      .0200  .0325  .0375  .0425  .0475  .0525  .0575  .0625  .0675  .0725  .0775  .0825  .0875  ...  .3000  .3100  .3200  .3300  .3400  .3500  .3650  .3850  .4050  .4250  .4450  .4650  .4850
2021-01-01 00:40:00    0.0    0.0    0.0   0.00   1.17   9.11  24.25  24.95  15.84  20.44  26.48  20.63  12.72  ...   0.28   0.31   0.19   0.20   0.13   0.07   0.06   0.05   0.03   0.01   0.01   0.00    0.0
2021-01-01 01:40:00    0.0    0.0    0.0   0.00   0.00  13.76  26.55  22.40  24.12  30.09  23.41  15.74  14.95  ...   0.25   0.16   0.12   0.16   0.06   0.16   0.06   0.03   0.05   0.02   0.01   0.00    0.0
2021-01-01 02:40:00    0.0    0.0    0.0   0.00   0.93   4.40  16.03  33.95  41.48  38.02  31.47  18.88  14.59  ...   0.21   0.15   0.18   0.14   0.14   0.10   0.07   0.05   0.03   0.02   0.01   0.00    0.0
2021-01-01 03:40:00    0.0    0.0    0.0   0.07   1.14   6.95  27.94  45.68  41.92  30.11  25.03  19.52  10.93  ...   0.22   0.20   0.16   0.09   0.08   0.15   0.09   0.04   0.02   0.01   0.00   0.01    0.0
2021-01-01 04:40:00    0.0    0.0    0.0   0.00   0.76   3.64  11.23  18.23  29.84  27.19  12.85  11.20   9.77  ...   0.13   0.17   0.14   0.16   0.08   0.08   0.07   0.08   0.05   0.01   0.01   0.00    0.0
...                    ...    ...    ...    ...    ...    ...    ...    ...    ...    ...    ...    ...    ...  ...    ...    ...    ...    ...    ...    ...    ...    ...    ...    ...    ...    ...    ...
2021-02-28 19:40:00    0.0    0.0    0.0   0.00   0.00   0.00   0.06   0.25   1.42   2.50   9.48  11.48   8.46  ...   0.21   0.13   0.11   0.08   0.10   0.04   0.02   0.02   0.03   0.01   0.00   0.00    0.0
2021-02-28 20:40:00    0.0    0.0    0.0   0.02   0.05   0.08   0.24   1.02   3.97   4.97   4.99   8.31  10.09  ...   0.21   0.07   0.09   0.06   0.05   0.10   0.04   0.03   0.01   0.01   0.00   0.00    0.0
2021-02-28 21:40:00    0.0    0.0    0.0   0.00   0.00   0.15   0.30   0.36   1.63   4.18   6.85   7.82   7.98  ...   0.12   0.11   0.09   0.08   0.04   0.05   0.06   0.02   0.01   0.01   0.00   0.00    0.0
2021-02-28 22:40:00    0.0    0.0    0.0   0.00   0.01   0.09   0.10   0.32   2.84   3.82   3.91   4.92   5.17  ...   0.17   0.09   0.13   0.05   0.05   0.08   0.06   0.03   0.01   0.01   0.00   0.00    0.0
2021-02-28 23:40:00    0.0    0.0    0.0   0.00   0.00   0.00   0.18   0.25   1.78   3.97   5.08   4.98   5.40  ...   0.07   0.10   0.11   0.08   0.08   0.06   0.03   0.02   0.01   0.01   0.00   0.00    0.0

[1413 rows x 47 columns]}}

```

Likely due to my own biases in my research interests, the `get_data()`  function will default to fetching
standard meteorological data.  However, users can specify different data packages like so `get_data(data_type='cwind')`.  To view which data packages
are currently supported examine the `DataBuoy.DATA_PACKAGES` attribute:
```
{'cwind': {'name': 'Continous Wind Data', 'url_char': 'c'},
 'srad': {'name': 'Solar radiation data', 'url_char': 'r'},
 'stdmet': {'name': 'Standard meteoroligcal data', 'url_char': 'h'},
 'swden': {'name': 'Spectral Wave Density data', 'url_char': 'w'},
 'swdir': {'name': 'Spectral wave (alpha1) direction data', 'url_char': 'd'},
 'swdir2': {'name': 'Spectral wave (alpha2) direction data', 'url_char': 'i'},
 'swr1': {'name': 'Spectral wave (r1) direction data', 'url_char': 'j'},
 'swr2': {'name': 'Spectral wave (r2) direction data', 'url_char': 'k'}}

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
