# NDBC
![alt text](http://www.ndbc.noaa.gov/images/nws/noaaleft.jpg "NOAA") ![alt text](http://www.ndbc.noaa.gov/images/nws/ndbc_title.jpg "NDBC")

This repository represents my attempts to build out Python class(es)
to facilitate the acquisition, analysis, and visualization of National
Data Buoy Center (NDBC) data.  The goal is to build classes that can be
easily used in oceanographic science scripting as well as a web
framework like Django or Flask.

## NDBC.py
This file defines the DataBuoy class.  The purpose of this class is to
allow a user to define a specific data buoy they wish to gather data
from and provide the user with methods to collect and analyze this data.
 * Dependencies
   * requests
   * datetime
   * pandas
   * math (standard library)
