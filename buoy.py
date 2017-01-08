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
        self.stdmet=[]
        #super(NDBCBuoy self).__init__()
        #self.arg = arg

    def __str__(self):
        return self.id + ' - Website: ' + self.station_url

    # Building in fucntionality to replace old names with the correct ones (as of 2014)
    def NDBCNames(self,oldname):
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
    def get_meta(self,dataframe):
        """
        """
        # TODO: Write function to parse out the meta data for stdmet and build it into a dictionary that can be appended the resulting buoy object.
        
    def fix_timestamp(self,dataframe):
        """
        this function takes the dataframe that results from reading NDBC text files and converts the columns containing datetime data to datetime objects and indexes dataframe by them.
        """
        if dataframe.iloc[0][0]=="#yr":
            dataframe=insertUnits(cursor,my_d)
        cols=list(dataframe.columns)
        if 'mm' in cols:
            cols=cols[0:cols.index('mm')+1]
            dataframe.set_index(keys=cols,inplace=True)
        else:
            cols=cols[0:cols.index('hh')+1]
            dataframe.set_index(keys=cols,inplace=True)
        my_dt=dataframe.index.values
        dtime=[]
        for i in my_dt:
            if len(str(i[0]))==2:
                Y=i[0]+1900
            else:
                Y=i[0]
            if len(cols)==5:
                strtime=dt(int(Y),int(i[1]),int(i[2]),int(i[3]),int(i[4])).isoformat()
            else:
                strtime=dt(Y,i[1],i[2],i[3]).isoformat()
            dtime.append(strtime)
        dataframe.index=dtime
        return dataframe

    def stdmet(self,start_year=0,stop_year=0):
        """
        Stdmet fetches all available stdmet files.

        If start and stop years are provided this function will gather all annual summaries between the start and stop years (inclusive).  If no years are provided it will crawl the basic station history page and download all available data.
        """
        import pandas as pd
        from datetime import datetime as dt
        import requests
        import bs4
        import re
        # Getting our base url for our file path
        file_url="http://www.ndbc.noaa.gov/view_text_file.php?"
        res=requests.get(self.info_url)
        soup=bs4.BeautifulSoup(res.text,'html.parser')
        urls=soup.find_all(href=re.compile('stdmet'))
        # This first attempt will go for all marbles
        if(start_year==0 and stop_year==0):
            for u in urls:
                text=u['href']
                start=re.search('filename',text).span()[0]
                fname=text[start:]
                target=file_url + fname
                data=pd.read_csv(target,header=0, engine='python',sep="\s+")
                # This will return dates and times split up between various columns.  Thankfully we've already written a function for this.
                data=self.fix_timestamp(data)
        return data
