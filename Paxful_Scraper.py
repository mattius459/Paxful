# -*- coding: utf-8 -*-
"""
Created on Sun Jul 08 10:52:32 2018

@author: Matt

File: Paxful_Scraper
"""

import urllib2
import json
import csv
import pandas as pd

hdr = {'User-Agent':'Mozilla/5.0'} #Create request header

#Variables
mainUrl = 'https://paxful.com/data/trades?since='
lastTx = '0'
fullUrl = mainUrl + lastTx
totalTx = 100
recordUpperBound = 21353150 #Upper bound represents the highest record id user wishes to collect
recordLowerBound = '21000151'
mainList = []
df = ()

#Fetching and storing data
def api_call(upperBound, lowerBound):
    print('You are in api_call!')
    print(upperBound)
    print(lowerBound)
    global totalTx
    global mainList
    global lastTx
    global mainUrl
    global fullUrl
    global recordUpperBound
    global recordLowerBound
    recordUpperBound = upperBound
    recordLowerBound = lowerBound
    request = urllib2.Request((mainUrl + recordLowerBound), headers = hdr) #Open a new web-request
    response = urllib2.urlopen(request) #Fetch the webpage data
    rawData = response.read() #Read raw data
    mainList = json.loads(rawData) #Convert raw data into JSON list of dicts
    for x in mainList: # find lastTx at end of list
        lastTx = x['id']
    lastTx = str(lastTx)
    fullUrl = mainUrl + lastTx
    lastTx = int(lastTx)   
    
    while (lastTx <= recordUpperBound):
        request = urllib2.Request(fullUrl, headers = hdr)
        response = urllib2.urlopen(request)
        newRawData = response.read()
        newTxList = json.loads(newRawData)
        for x in newTxList:
            lastTx = x['id']
        lastTx = str(lastTx)
        recordLowerBound = lastTx
        fullUrl = mainUrl + lastTx
        mainList = mainList + newTxList
        lastTx = int(lastTx)
        totalTx = totalTx + 100
        print(totalTx)
    print('last Tx =')
    print(recordLowerBound)
    number = int(recordLowerBound) + 1
    lowerBound = str(number)
    
    return lowerBound
    
        
#Transfering mainList into dataframe, converting fields to proper data types
def push_to_dataframe():
    
    global df
    global mainList
    
    print('You are in push_to_dataframe!')
    df = pd.DataFrame(mainList, columns = ['id', 'date', 'amount', 'price', 'payment_method', 'payment_method_group', 'currency', 'type'])
    df['amount'] = pd.to_numeric(df['amount'], errors = 'coerce') #Convert string prices into float prices
    df['price'] = pd.to_numeric(df['price'], errors = 'coerce') #Convert string prices into float prices
    df['date'] = pd.to_numeric(df['date'], errors = 'coerce') #Convert string prices into float prices

#Transferring dataframe into CSV file
def push_to_csv():
    
    global df
    
    print('You are in push_to_csv!')
    df.to_csv('C:/Users/Matt/Desktop/Python/Paxful.csv', index = False, encoding='utf-8')