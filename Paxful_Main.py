# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 14:55:21 2018

@author: Matt

File: Paxful_Main
"""

from Paxful_Scraper import *
from Paxful_DB import *

create_BTC_price_table()

"""
upperBound = 21353150
lowerBound = '21000152'

while (upperBound <= 22753150):
    print("hello")
    lowerBound = api_call(upperBound, lowerBound)
    push_to_dataframe()
    push_to_csv()
    create_table()
    print('done!')
    upperBound += 50000
"""
    
"""

To-do:

    Importing:
        
        Import Bitcoin Price Data into Database for correct dates
        Import Economic data into Database
        
        
    
    Querying:

    
    Visualization:
        
        Do some basic visualization of queries
            Number of transactions over time
                
                Do I need to put day date as new column?
                
            
            histogram of currency types
            pie chart of payment methods within USD
            Get graph to show human-readable date, not unix
            
Tomorrow:
    
        Finish BTC price import, make sure dates are compatible (str, int) so that it visualizes correctly.
        Clean up files to make more generalized program
        Add BTC price import into DB
        Try a query using BTC price (USD value of transactions)
        Start importing economic data
"""

"""

"""