# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 13:42:54 2018

@author: Matt

File: Paxful_Viz
"""
import sqlite3 # Import Python's sqlite package
import pandas as pd # Import pandas
from datetime import datetime # Import python's datetime packages
import seaborn as sns # Import pretty bar chart package
from matplotlib import pyplot as plt

sns.set(style = "whitegrid", rc = {'figure.figsize': (10, 10)})

# Establish a connection to the sqlite database file
cnx = sqlite3.connect('Paxful.db')

# Define a table name to query
tablename = 'paxfulData'

# Pull everything from the defined table name
df = pd.read_sql_query("select * from " + tablename, cnx)
df['date'] = pd.to_datetime(df['date'], unit = 's').dt.date

################################### Currency Total Bar Graph ###################################
startdate = datetime(2018, 1, 1).date() # Start date of interest
enddate = datetime(2018, 7, 1).date() # End date of interest
startenddata = df.query('date >= @startdate and date <= @enddate') # Filter data frame to only the dates of interest

currencytotals = pd.DataFrame(startenddata.groupby('currency')['amount'].sum()).reset_index() # Group by currency type
ax = sns.barplot(x = 'currency', y = 'amount', data = currencytotals) # Create barplot specifying x and y as column names in data argument
ax.set(xlabel = 'Currency Type', ylabel = 'Transacted Volume', title = 'Transacted Volume by Currency Type') # Add labels to chart
plt.setp(ax.get_xticklabels(), rotation=60, horizontalalignment='right')
plt.savefig('C:/Users/Matt/Desktop/Python/bargraph.png') # Save figure as png image
plt.show()

################################### Currency Transaction Time Series ###################################
bydayandcurrencydata = df.groupby(['date', 'currency'])['amount'].sum().reset_index() # Group data by date and currency and calc sum amount
for currencyofinterest in bydayandcurrencydata['currency'].unique(): # For every unique currency
    currencydata = bydayandcurrencydata.query('currency == @currencyofinterest') # Grab only this currency's data
    plt.plot(currencydata['date'], currencydata['amount'], label = currencyofinterest) # Plot this currency's line chart
plt.title('Transaction Amount by Day Per Currency') # Add title to chart
plt.xlabel('Day') # Add x label to chart
plt.ylabel('Transaction Amount') # Add y label to chart
plt.legend(loc = 'best') # Add legend to chart
#plt.savefig('C:/Users/aockenden/Desktop/linechart1.png') # Save figure as png image
plt.show()

################################### Payment Method Pie Chart ###################################
currencyofinterest = 'VEZ' # Currency of interest
currencydata = df.query('currency == @currencyofinterest') # Filter data frame to only the currency of interest

methodtotals = pd.DataFrame(currencydata.groupby('payment_method')['amount'].sum()).reset_index() # Group by currency type
methodtotals = methodtotals.sort_values('amount', ascending  = False) # Order by volume
toptypes = methodtotals.iloc[0:9] # Grab largest 10 categories
resttype = pd.DataFrame([['All Others', methodtotals.iloc[9:]['amount'].sum()]], columns = ['payment_method', 'amount']) # Sum all remaining categories
combtypes = toptypes.append(resttype) # Append summed remaining and top 10 categories
plt.pie(combtypes['amount'], 
        explode = [0.1] * len(combtypes), 
        labels = combtypes['payment_method'], 
        autopct = '%1.1f%%', 
        shadow = True, 
        startangle = 140) # Create pie chart
plt.title('Transacted Volume by Payment Method: NGN') #Add title to chart
#plt.savefig('') # Save figure as png image
plt.show()

################################### Currency Transaction Price Time Series ###################################
bydayandcurrencydata = df.groupby(['date', 'currency'])['price'].median().reset_index() # Group data by date and currency and calc median price
for currencyofinterest in bydayandcurrencydata['currency'].unique(): # For every unique currency
    currencydata = bydayandcurrencydata.query('currency == @currencyofinterest') # Grab only this currency's data
    plt.plot(currencydata['date'], currencydata['price'], label = currencyofinterest) # Plot this currency's line chart
plt.title('Median Price by Day Per Currency') # Add title to chart
plt.xlabel('Day') # Add x label to chart
plt.ylabel('Transaction Price') # Add y label to chart
plt.legend(loc = 'best') # Add legend to chart
#plt.savefig('C:/Users/aockenden/Desktop/linechart2.png') # Save figure as png image
plt.show()