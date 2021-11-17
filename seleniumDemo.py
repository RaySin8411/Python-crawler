import re
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 瀏覽器設置
chrome_options = Options()
chrome_options.add_argument('--incognito')
chrome_options.add_argument('--headless')  #規避google bug
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0')
browser = webdriver.Chrome(chrome_options=chrome_options)


# Query 設置
query = 'selenium' #搜尋的字元
browser.get("https://www.google.com/search?q={}".format(query))
next_page_times = 10


# 爬蟲
for _page in range(next_page_times):
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    content = soup.prettify()

    # Get titles and urls
    titles = re.findall('<h3 class="[\w\d]{6} [\w\d]{6}">\n\ +(.+)', content)
    urls = re.findall('<div class="r">\ *\n\ *<a href="(.+)" onmousedown', soup.prettify())
    for n in range(min(len(titles), len(urls))):
        print(titles[n], urls[n])

    # Wait
    time.sleep(5)

    # Turn to the next page
    try:
        browser.find_element_by_link_text('下一頁').click()
    except:
        print('Search Early Stopping.')
        browser.close()
        exit()


# 關閉瀏覽器
browser.close()
