import requests
import pandas as pd


def main():
    url = "https://isin.twse.com.tw/isin/class_main.jsp?owncode=&stockname=&isincode=&issuetype=1&industry_code=&Page=1&chklike=Y"
    res = requests.get(url)

    df = pd.read_html(res.text)[0]
    df = df.drop([0, 1, 5, 8, 9], axis=1)
    df.columns = df.iloc[0]
    df = df.set_index("有價證券代號")
    df = df.iloc[1:]
    df.to_csv("data/listed_company.csv")

if __name__ == "__main__":
    main()
