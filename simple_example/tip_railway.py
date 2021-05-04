import requests
from bs4 import BeautifulSoup
import time

url = 'https://tip.railway.gov.tw/tra-tip-web/tip'
staDic = {}
today = time.strftime('%Y/%m/%d')
sTime = '06:00'
eTime = '12:00'


def getTrip():
    resp = requests.get(url)
    if resp.status_code != 200:
        print('URL發生錯誤: ' + url)
        return
    soup = BeautifulSoup(resp.text, 'html5lib')
    stations = soup.find(id='cityHot').ul.find_all('li')
    for station in stations:
        stationName = station.button.text
        stationId = station.button['title']
        staDic[stationName] = stationId

    csrf = soup.find(id='queryForm').find('input', {'name': '_csrf'})['value']
    formData = {
        'trainTypeList': 'ALL',
        'transfer': 'ONE',
        'startOrEndTime': 'true',
        'startStation': staDic['臺中'],
        'endStation': staDic['臺北'],
        'ridDate': today,
        'startTime': sTime,
        'endTime': eTime
    }
    queryUrl = soup.find(id='queryForm')['action']
    qResp = requests.post('https://tip.railway.gov.tw'+queryUrl, data=formData)
    # qSoup = BeautifulSoup(qResp.text, 'html5lib')
    # trs = qSoup.find_all('tr', 'trip-column')
    print(qResp)
    # for tr in trs:
    #     td = tr.find_all('td')
    #     print('%s : %s, %s' % (td[0].ul.li.a.text, td[1].text, td[2].text))


if __name__ == '__main__':
    getTrip()
