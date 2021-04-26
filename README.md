# Python crawler

## 反爬蟲策略以及解決方法
1. **通過headers反爬蟲**

    對於基本網頁的抓取可以自定義headers,新增headers的資料

2. **基於使用者行為的發爬蟲：(同一IP短時間內訪問的頻率)**

    使用多個代理ip進行抓取或者設定抓取的頻率降低一些

3. **動態網頁反爬蟲(通過ajax請求資料，或者通過JavaScript生成)**

    動態網頁的可以使用selenium phantomjs 進行抓取

4. **對部分資料進行加密處理的(資料是亂碼)**

    對部分資料進行加密的，可以使用selenium進行截圖，使用python自帶的pytesseract庫進行識別，但是比較慢最直接的方法是找到加密的方法進行逆向推理。

## selenium
* chromedriver.exe
	
	* 可直接下載chrome版號的對應版本
		* 網址 : https://chromedriver.chromium.org/downloads
	
	* 或是用chrome_helper.py & file_util.py

### seleniumDemo.py
* Google搜尋例子

## 撈股票程式

* stock.py
	* bs4
		* BeautifulSoup
	* selenium

* stock_pd.py
	* numpy
	* requests
	* pandas
	* datatime
	
## 非同步程式
* async/aiohttp_example.py
### Reference
* [整合asyncio與aiohttp打造Python非同步網頁爬蟲](https://www.learncodewithmike.com/2020/09/python-asynchronous-scraper-using-asyncio-and-aiohttp.html)
* [非同步網頁爬蟲使用GRequests套件提升爬取效率的實作技巧](https://www.learncodewithmike.com/2020/09/python-asynchronous-scraper-using-grequests.html)
