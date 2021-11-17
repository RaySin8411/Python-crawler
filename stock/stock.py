from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import numpy as np
import pandas as pd
 
class Stock:
    def __init__(self, *stock_numbers):
        self.stock_numbers = stock_numbers
 
    def daily(self, year, month):
        browser = webdriver.Chrome()
        browser.get("https://www.twse.com.tw/zh/page/trading/exchange/STOCK_DAY_AVG.html")
     
        select_year = Select(browser.find_element_by_name("yy"))
        select_year.select_by_value(year)  # 選擇傳入的年份
     
        select_month = Select(browser.find_element_by_name("mm"))
        select_month.select_by_value(month)  # 選擇傳入的月份
     
        stockno = browser.find_element_by_name("stockNo")  # 定位股票代碼輸入框
            
        result = []
        for stock_number in self.stock_numbers:
            stockno.clear()  # 清空股票代碼輸入框
            stockno.send_keys(stock_number)
            stockno.submit()
         
            time.sleep(5)
         
            soup = BeautifulSoup(browser.page_source, "lxml")
         
            table = soup.find("table", {"id": "report-table"})
         
            elements = table.find_all(
                "td", {"class": "dt-head-center dt-body-center"})
                        
            data = (stock_number,) + tuple(element.getText() for element in elements)
                       
            result.append(np.array(data))
     
        print(pd.DataFrame(result))
        browser.close()