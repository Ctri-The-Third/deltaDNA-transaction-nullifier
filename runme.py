
import json
import getpass
import csv

import Connect
from eventHelper import * 


# load Direct Access and Collect information
try:
    f = open("settings.json","r")
    keys = json.load(f)
    database = keys["db"]
    user = keys["user"]
    collectURL = keys["collectURL"]
    environmentKey = keys["environmentKey"]
except Exception as e:
    print("ERROR loading from settings.json \n%s\n" % (e,) )
    exit()



#confirm with the user & get password
print("This application is going to try to connect to the following Direct Access instance:\nDB:\t%s\nuser:\t%s\n" % (database,user))
print("This application is going to try to send events to the following URL & Key:\nDB:\t%s\nuser:\t%s" % (collectURL,environmentKey))
print("Ensure the details are correct before entering your password, there will be no further confirmations.")
password = getpass.getpass("Enter your deltaDNA password (It will not be displayed on screen)\n") 

#establish connection to Direct Access
try:
    conn = Connect.da_connect(user,password,database)
except Exception as e:
    print("ERROR connecting to Direct Access \n%s\n" % (e,) )
    exit()


#for each eventID in the CSV:
#1. Query Direct Access for its content
#2. Take the parameters returned and form them into a default Transaction event
#3. send that event JSON to the game specified in the settings
with open ('input.csv','r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        if len(row) > 0:
                 
            eventID = row[0]
            paramObj = getEvent(eventID,conn)
            invertedEvent  = invertEvent(paramObj)
            sendEvent(invertedEvent,collectURL,environmentKey)
        else:
            break
print("Events sent. You should now wait 15 minutes and check events have been received.")
