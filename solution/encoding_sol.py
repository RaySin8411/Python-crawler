import requests


# GET
def demo_get():
    url = "https://sea.cc.ntpu.edu.tw/pls/dev_stud/course_query_all.CHI_query_common"
    re = requests.get(url)
    re.encoding = 'big5'
    # re.encoding='cp950'
    # re.encoding='utf8'
    print(re.text)


# POST
def demo_post():
    url = "https://sea.cc.ntpu.edu.tw/pls/dev_stud/course_query_all.queryByAllConditions"
    data = {
        "qCollege": "法律學院".encode('big5'),  # 用big5編碼後傳輸
        "qdept": "LU31",
        "qYear": 105,
        "qTerm": 2,
        "seq1": "A",
        "seq2": "M"
    }
    re = requests.post(url, data=data)
    re.encoding = 'big5'

    # re.encoding='cp950'
    # re.encoding='utf8'
    print(re.text)


if __name__ == '__main__':
    demo_get()
    demo_post()
