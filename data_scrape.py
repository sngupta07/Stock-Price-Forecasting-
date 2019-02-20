import pandas as pd #for manipulation
import matplotlib.pyplot as plt #for plotting
import numpy as np #for computation
import pandas_datareader.data as web #used to read the past data or real time data
import os
import quandl

quandl.ApiConfig.api_key= *******************

tickers= pd.read_csv('C://Users//sngupta//Documents//minor projects//data_scrape//stock_data//EQUITY_L.csv', encoding= 'latin-1')

#to create dictionary to store the data of all the stocks
#stock_data= dict()
path= 'C://Users//sngupta//Documents//minor_project//euqity_data//'

#list_of_file= os.listdir(path).to_list()
#now, iterate the loop to all the tickers and read from the pandas datareader

for ticker in tickers['SYMBOL']:
    #stock_data['{}' .format(ticker)]= web.DataReader('NSE/{}' .format(ticker), 'quandl', start= '2008-01-01', end= '2018-09-30')
    #df= web.DataReader('NSE/{}' .format(ticker), 'quandl', start= '2008-01-01', end= '2018-09-30')
    #now, save the file in csv format
    #if ticker+'.csv' in list_of_file:
    try:
        df= quandl.get('NSE/{}' .format(ticker), start= '2008-01-01', end= '2018-09-30')
        df.to_csv(ticker+'.csv')
    except:
        continue
    
#for key in stock_data.keys():
#    stock_data[key].to_csv()
    
