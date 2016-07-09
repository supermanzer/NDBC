# -*- coding: utf-8 -*-
"""
Created on Fri May 20 19:55:41 2016
GET NDBC
@author: ryan
"""
import MySQLdb as mysql
import pandas as pd
import configparser
from datetime import datetime as dt
import dateutil.parser as par
import numpy as np
con=configparser.ConfigParser()
con.read('/home/ryan/Python_Scripts/NDBC/config.ini')
myyears=range(1987,2016) # The last number won't be generated
mymonths=range(1,6) # same thing here
td=dt.today()
this_year=td.year
# getting access to our local db
my_host=con['LOCALDB']['host']
my_port=int(con['LOCALDB']['port'])
my_user=con['LOCALDB']['user']
my_passwd=con['LOCALDB']['passwd']
my_db=con['LOCALDB']['db']
conn=mysql.connect(host=my_host,port=my_port,user=my_user,passwd=my_passwd,
                   db=my_db)
cur=conn.cursor()
# Now let's get our station ids
sql="SELECT station_id FROM ndbc_stations;" 
cur.execute(sql)
stations=cur.fetchone()
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

def getData(cursor,station,year,month):
    base_url = 'http://www.ndbc.noaa.gov/view_text_file.php?filename={}'.format(station)
    if month==0:
        target=base_url+'h'+str(year)+'.txt.gz&dir=data/historical/stdmet/'
    elif year==0:
        tm=dt(this_year,month,1)
        target=base_url+str(month)+str(this_year)+'.txt.gz&dir=data/stdmet/'+tm.strftime('%b')+'/'
    else:
        print('Not sure what you meant to do here but this is weird')
    # okay now that we have built our url that should point toward the text data file
    # let's grad that data file
        
    # we are trainwrecking in 2007 when (at least for station 46042)
    # NOAA started adding a second line to the header with the units
    # for each measurement.  It would be nice to capture this somewhere
    # in our DB but obviously it cannot be part of the numerical data.
    # Perhaps an additional table?
    try:
        my_d=pd.read_csv(target,header=0, engine='python',sep="\s+")
    except:
        if month==0:
            print("Year " +  str(year) + " is not available")
        elif year==0:
            print("Month " + str(month) + " is not available")
        return pd.DataFrame() # in order to properly evaluate the result we need to return an empty data frame...kind of wasteful memory wise but it works
    # Now let's get those pesky year, month, day, and
    # hour columns into a Timestamp
    # first we get the columns with our datetime info
    if my_d.iloc[0][0]=="#yr":
        my_d=insertUnits(cursor,my_d)
    cols=list(my_d.columns)
    if 'mm' in cols:
        cols=cols[0:cols.index('mm')+1]
        my_d.set_index(keys=cols,inplace=True)
    else:
        cols=cols[0:cols.index('hh')+1]
        my_d.set_index(keys=cols,inplace=True)
    my_dt=my_d.index.values
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
    my_d.index=dtime
    # Huzzah, we have our datetime strings as our index!  Since
    # it is ISO 8601 compliant this should be easily loaded into
    # a MySQL DB.  Now let's handle those bad data flags
    cols=list(my_d.columns) # we need to redo this to account for indexing
    # AFTER CAREFUL CONSIDERATION IT APPEARS TO ME THAT DEALING WITH BAD DATA
    # FLAGS WOULD BE EASIER DONE ONCE THE DATA HAS BEEN LOADED INTO THE DATABASE
    # THEREFORE I WILL SKIP THIS SECTION AND IMPLEMENT A BAD DATA FLAG PROTOCOL
    # LATER ON, AFTER INSERTING THE RECORDS.
    newcols=[];
    for col in cols:
        newcols.append(NDBCNames(col))
#        badFlag=True
#        if my_d[col].max()!=np.nan:
#            flagstr=str(int(my_d[col].max()))
#            flagval=my_d[col].max()
#            for ch in flagstr:
#                if int(ch) != 9:
#                    badFlag=False
#                    break
#            if badFlag:
#                # THIS IS SETTING ALL COLUMNS TO NAN!!!!!
#                # NEED TO FIX THIS
#                my_d[my_d[col]==flagval]=np.NaN
    my_d.columns=newcols
    my_d.fillna(999.0, inplace=True)
    return my_d
    
def insertStdMet(station,cursor,data):
    # This function takes in a station id, database cursor and an array of data.  At present
    # it assumes the data is a pandas dataaframe with the datetime value as the index
    # It may eventually be modified to be more flexible.  With the parameters
    # passed in, it goes row by row and builds an INSERT INTO SQL statement
    # that assumes each row in the data array represents a new record to be
    # added.
    fields=list(data.columns) # if our table has been constructed properly, these column names should map to the fields in the data table
    # Building the SQL string
    strSQL1='REPLACE INTO std_met (station_id,date_time,'
    strSQL2='VALUES (%s,%s,'
    for f in fields:
        strSQL1+=f+','
        strSQL2+='%s,'
    # trimming the last comma
    strSQL1=strSQL1[:-1]
    strSQL2=strSQL2[:-1]
    strSQL1+=") " + strSQL2 + ")"
    # Okay, now we have our SQL string.  Now we need to build the list of tuples
    # that will be passed along with it to the .executemany() function.
    tuplist=[]
    for i in range(len(data)):
        r=data.iloc[i][:]
        datatup=(station,r.name)
        for f in r:
            datatup+=(f,)
        tuplist.append(datatup)
    cursor.executemany(strSQL1,tuplist)
    conn.commit()
def insertUnits(cursor,data):
    # This function is designed to check whether or not the first line of the 
    # pandas data frame passed in contains additional string information, usually
    # the units for the parameters measured.  If so it will insert those units
    # into the units table in our database
    r=data.iloc[0][:]
    if isinstance(r[0],str): # if we have a string we assume r represents the units
        cols=list(data.columns) # getting our list of columns
        strSQL="REPLACE INTO units (parameter, unit) VALUES (%s,%s)"
        tuplist=[]
        if 'mm' in cols:
            start_index=cols.index('mm')+1
        else:
            start_index=cols.index('hh')+1
        for col in cols[start_index:]:
            datatup=(col,r[col])
            tuplist.append(datatup)
        cursor.executemany(strSQL,tuplist)
        data = data.iloc[1:][:]
    return data
        
# Rolling up both functions into a single function that can be executed using
# a multi-threading approach
def wholeShebang(station,year,month,cursor):
    stdmet=getData(station,year,month)
    insertStdMet(station,cursor,stdmet)
    
threads=[]
for station in stations:
#    for y in myyears:
#        stdmet=getData(cur,station,y,0)
#        insertStdMet(station,cur,stdmet)
    for m in mymonths:
        stdmet=getData(cur,station,0,m)
        if not stdmet.empty:
            insertStdMet(station,cur,stdmet)
print('Hooray!  You just loaded a crap ton of NDBC data!')