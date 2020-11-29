import pandas as pd
import requests
from pandas_datareader import data as web
import yfinance as yf
import datetime as dt
import os
from io import StringIO


#爬取成分股清單
def US_StockList():
    
    #sp-500
    link = 'https://www.slickcharts.com/sp500'
    r = requests.get(link)
    lines = r.text.replace('r', '').split('\n')
    df = pd.read_html(StringIO("\n".join(lines[:])), header=None)[0]
    df=df.loc[:,['Company','Symbol']]
    df=df.rename(columns={'Company':'US_StockName','Symbol':'stock_id'})
    
    #Nasdaq-100
    link = 'https://www.nasdaq.com/market-activity/quotes/Nasdaq-100-Index-Components'
    r = requests.get(link)
    lines = r.text.replace('\r', '').split('\n')
    df2 = pd.read_html(StringIO("\n".join(lines[:])), header=None)[0]
    df2=df2.rename(columns={'COMPANY NAME':'US_StockName','SECURITY SYMBOL':'stock_id'})
    
    #合併並拿掉重複項
    df3=pd.concat([df,df2])
    df4=df3.set_index('stock_id')
    df4=df4[~df4.index.duplicated(keep='first')]#keep=’first保留重複的首項，另一種是last
    return df4

#美股股價爬蟲
def crawl_US_Stock(startDate):
    '''
    startDate : 引數決定資料起始日
    '''
    
    US_Stock_List=US_StockList()
    target=US_Stock_List.index
    data=[]
    for stock_id in target:
        try:
            df = web.get_data_yahoo(stock_id,startDate,dt.datetime.now())
            df['stock_id']=stock_id
            df=df.reset_index()
            print(stock_id)
            data.append(df)
        except:
            print('error',stock_id )
            pass
    data=pd.concat(data)
    data = data.rename(columns={'Date':'date'})
    data=data.set_index(['stock_id'])
    data['US_StockName']=US_Stock_List['US_StockName']
    data=data.reset_index()
    data=data.set_index(['stock_id','date'])       
    
    return data
    
    
    