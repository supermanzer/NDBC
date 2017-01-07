class NDBCBuoy:
    """
    Get NDBC Buoy Data.

    This class houses methods for gathering, processing, and retrieving oceanographic data from NDBC Data Buoys.
    """
    def __init__(self, station_id):
        NDBCBuoy.base_url="http://www.ndbc.noaa.gov/"
        self.id = station_id
        self.station_url=self.base_url + 'station_page.php?station=' + str(station_id)
        self.info_url=self.base_url + 'station_history.php?station=' + str(station_id)
        #super(NDBCBuoy self).__init__()
        #self.arg = arg

    def __str__(self):
        return self.id

    # Building in fucntionality to replace old names with the correct ones (as of 2014)
    def NDBCNames(oldname):
        namedict={  #old    #new
                    'YYYY':'YY',
                    '#YY':'YY',
                    'WD':'WDIR',
                    'DIR':'WDIR',
                    'SPD':'WSPD',
                    'GSP':'GST',
                    'GNM':'GTIME',
                    'BAR':'PRES',
                    'BARO':'PRES',
                    'H0':'WVHT',
                    'DOMPD':'DPD',
                    'AVP':'APD',
                    'SRAD':'SWRAD',
                    'SRAD2':'SWRAD',
                    'LRAD':'LWRAD',
                    'LRAD1':'LWRAD'
                    }
        if oldname in namedict:
            return namedict[oldname]
        else:
            return oldname

    def stdmet(self):
        import pandas as pd
        from datetime import datetime as dt
