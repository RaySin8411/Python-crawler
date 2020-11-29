from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import datetime
import time



def crawl_fund_TW_Stock(date,fund_class):
    
    browser=webdriver.Chrome()
	
    url='https://www.sitca.org.tw/ROC/Industry/IN2629.aspx?pid=IN22601_04'
    browser.get(url)
    time.sleep(5)
    
    #選擇日期
    selectDate=Select(browser.find_element_by_id('ctl00_ContentPlaceHolder1_ddlQ_YM'))
    datestr=date.strftime('%Y%m')
    selectDate.select_by_value(datestr)#選單項目定位
    time.sleep(5)
    
    #模擬勾選”類型o”
    guildlink=browser.find_element_by_id('ctl00_ContentPlaceHolder1_rbClass')
    guildlink.click()#模擬點擊
    time.sleep(5)
    
    #選擇類型
    selectDate=Select(browser.find_element_by_id('ctl00_ContentPlaceHolder1_ddlQ_Class'))#類型選單定位
    selectDate.select_by_value(fund_class)#選單項目定位
    time.sleep(5)
    
    #模擬按下送出查詢按鈕
    searchBtn=browser.find_element_by_id('ctl00_ContentPlaceHolder1_BtnQuery')#查詢按鈕定位
    searchBtn.click()#模擬點擊
    time.sleep(5)

    df=pd.read_html(browser.page_source)[0]
    df2=df.dropna(thresh=8)
    
    #資料處理
    df2=df2.astype(str)
    df2.columns=df2.iloc[0]
    df2=df2.iloc[1:]
    df2=df2[df2['基金名稱']!='合計']
    df2=df2.drop(columns=['擔保機構**','次順位債券**','受益權單位數***'])
    df2.iloc[:,-2:]=df2.iloc[:,-2:].apply(lambda s:pd.to_numeric(s, errors='coerce'))
    df2=df2.rename(columns={'標的代號 或BloombergIsin Code':'stock_id','金額':'基金投資金額',
    '占基金淨資產價值之比例(%)':'占基金淨資產價值之比例'})
    df2['stock_id']=df2['stock_id']+'_'+df2['基金名稱']
     
    #當月資訊在下個月第10個工作日才出現，日期要調整，預測是下個月15日，碰到12月會換年！
    next_month = datetime.date(date.year + int(date.month / 12), ((date.month % 12) + 1), 15)
    df2['date'] = pd.to_datetime(next_month)
    df2=df2.set_index(['stock_id','date'])
    #關掉瀏覽器
    browser.close()
    return df2
    