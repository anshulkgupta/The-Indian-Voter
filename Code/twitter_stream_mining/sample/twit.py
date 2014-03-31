import sqlite3 as lite
import tweetstream
import csv
import sys
from datetime import date
import time

twitterUsername = "USERNAME"
twitterPassword = "PASSWORD"

twitterWordFilter = [] #Defined the list
wordListCsv = csv.reader(open('wordstofilter.csv', 'rb'))
for row in wordListCsv:
    #Add the 0th column of the current row to the list
    twitterWordFilter.append(row[0])
    
print "Filtering the following words: ",', '.join(twitterWordFilter)

   

try:
    #Load the data base file (or make it if not found)
    #If dont set isolation level then we need to call
    #Db commit after every execute to save the transaction
    con = lite.connect('twitter.db',isolation_level=None)
    cur = con.cursor() #Use cursor for executing queries
    #Get the sourceid (will be useful when we use multiple data sources)
    cur.execute("SELECT sourceid FROM sources where sourcedesc='twitter'")
    sourceid = cur.fetchone() #Get the source id
    sourceid = sourceid[0]
       
    with tweetstream.FilterStream(twitterUsername, twitterPassword,track=twitterWordFilter) as stream:
        for tweet in stream:
            tweettimestamp =  time.mktime(time.strptime(tweet['created_at'],"%a %b %d %H:%M:%S +0000 %Y")) - time.timezone
           
            print stream.count,"(",stream.rate,"tweets/sec). ",tweet['user']['screen_name'],':', tweet['text'].encode('ascii','ignore')
            #print tweet #Use for raw output            
            try:
                cur.execute("INSERT INTO tweets(sourceid,username,tweet,timestamp) VALUES(?,?,?,?)",[sourceid,tweet['user']['screen_name'],tweet['text'].encode('ascii','ignore'),tweettimestamp])
            except:
                print "SQL Insert Error: Probably some encoding issue due to foreign languages"
            
          
                
except tweetstream.ConnectionError, e:
    print "Disconnected from twitter. Reason:", e.reason
except lite.Error, e:
    print "SQLite Error:",e
except:
    print "ERROR:",sys.exc_info()    
finally:
    if con:
        con.close()