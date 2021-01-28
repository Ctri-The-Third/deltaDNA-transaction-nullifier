import psycopg2
import requests
from datetime import datetime


def getEvent(eventID, conn):
    #Fetch the minimum number of fields from the platform to populate and send a transaction event to the platform    
    SQL = "select userID, eventTimestamp, eventName, sessionID, platform, realCurrencyAmount, realCurrencyType, transactionName, transactionType from events_live where mainEventID = %s and eventName = 'transaction' and convertedproductamount is not null"
    try:
        cursor = conn.cursor()
        cursor.execute(SQL,(eventID,))
        results = cursor.fetchall()
        event = {} 
        
        for result in results: 
            counter =  0 
            for column in result:
                columnName = cursor.description[counter].name
                event [columnName] = result[counter]
                counter = counter + 1 
    except Exception as e:
        print("Error getting the event: \n%s" % (e))
    return event

def invertEvent(paramObj):
    #take the flat structure of the returned "getEvent" object and turn it into a suitably structure object for upload.

    try:

        eventObj = {}
        
        eventObj["eventName"] = paramObj["eventName"]
        del paramObj["eventName"]
        eventObj["userID"] = paramObj["userID"]
        del paramObj["userID"]
        eventObj["sessionID"] = paramObj["sessionID"]
        del paramObj["sessionID"]
        eventObj["eventTimestamp"] = paramObj["eventTimestamp"].strftime(r'%Y-%m-%d %H:%M:%S')
        del paramObj["eventTimestamp"]
        paramObj["transactionName"] = "ManualCorrection"
        
        
        
        paramObj["productsReceived"] = {} 
        paramObj["productsSpent"] = {} 
        paramObj["productsSpent"]["realCurrency"] = {} 
        paramObj["productsSpent"]["realCurrency"]["realCurrencyAmount"] = -paramObj["realCurrencyAmount"]
        paramObj["productsSpent"]["realCurrency"]["realCurrencyType"] = paramObj["realCurrencyType"]
        del paramObj["realCurrencyAmount"] 
        del paramObj["realCurrencyType"] 
        
        eventObj["eventParams"] = paramObj
        
        
    except Exception as e: 
        print("Failed to invert event \n %s" % (e))
    return  eventObj

def sendEvent(eventObj,collectURL,collectKEY):

    URL = '%s/%s' % (collectURL,collectKEY)
    response = requests.post(url = URL, json = eventObj)
    try: 
        print("An event was sent with response code: %s" % (response.status_code))
    except Exception as e:
        print ("ERROR sending an event\n%s" % (e))
    return response.status_code

