# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 16:18:34 2018

@author: Matt
"""
import sqlite3
import pandas as pd #Import Python's data-structure library (matrices, vectorized math etc.)

def Paxful_table():
    print('You are in create table!')
    conn = sqlite3.connect('test.db') #Connection Object
    conn.text_factory = str
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS paxfulData(
                id INTEGER, date INTEGER,
                amount REAL,
                price REAL,
                payment_method TEXT,
                payment_method_group TEXT,
                currency TEXT,
                type TEXT)""")
    df = pd.read_csv('C:/Users/Matt/Desktop/Python/Paxful.csv')
    df.to_sql('paxfulData', conn, if_exists='append', index=False)
    conn.commit()
    c.close()
    conn.close()
    
def create_BTC_price_table():
    print('You are in create_BTC_price_table()')
    conn = sqlite3.connect('Paxful.db') #Connection Object
    conn.text_factory = str
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS BTC_Price_Data(
               date TEXT,
               price REAL)""")
    df = pd.read_csv('C:/Users/Matt/Desktop/Python/bitcoindata.csv')
    df.to_sql('BTC_Price_Data', conn, if_exists='append', index=False)
    conn.commit()
    c.close()
    conn.close()