# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 11:53:25 2018

@author: Matt

File: Paxful_Query
"""

import sqlite3
import pandas as pd
import datetime
import time
from matplotlib import pyplot as plt

#Database connection

conn = sqlite3.connect('Test.db')
c = conn.cursor()

#SQL query

c.execute("SELECT date, amount FROM paxfulData") 
data = c.fetchall()

#Dataframe creation

#df = pd.DataFrame(data, columns = ['id', 'date', 'amount', 'price', 'payment_method', 'payment_method_group', 'currency', 'type'])
df = pd.DataFrame(data, columns = ['date', 'amount'])
df['date'] = pd.to_datetime(df['date'], unit = 's') #Converting integer of unix time into datetime object
#df.set_index('date').groupby(pd.TimeGrouper('D')) 

print(df.head())


#Visualization

plt.plot(df['date'], df['amount'])
plt.show()

#Close connection
conn.close()