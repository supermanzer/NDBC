# NDBC
Repository for housing Python code for fetching, parsing, and loading NDBC data into a database.  Additional development will move towards custom data objects that encapsulate data retrieval, processing, and analyses.  

## buoy.py
This represents my first real stab at a class definition. I am attempting to bundle many of the functions and attributes I have previously scripted in Matlab into a buoy object.  This object will use methods to gather all data associated with a particular NDBC buoy. I will start with standard meteoroloigcal summaries but will endeavor to branch out into other data as well.  I would like to add my own custom data cleaning and some rudimentary analyses functions but obviously the more I add the less useful it becomes beyond my own purposes.  This project is an attempt to both allow for easier oceanographic data exploration and to teach myself about writing quality applications.  Any help/suggestions would be greatly appreciated.


## getNDBC_stdMet.py
This is the first script I wrote to gather and load NDBC standard meteorological data into a database.  I intend to buidl this functionality into the buoy class.
