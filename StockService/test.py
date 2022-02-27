from urllib import parse

import requests
import yfinance as yf

if __name__ == '__main__':
    # msft = yf.Ticker("MSFT")
    # print(msft.info)
    file1 = open('stocks.txt', 'r')
    lines = file1.readlines()
    for i in lines:
        json = {'stock_symbol': i.rstrip()}
        x = requests.post('https://127.0.0.1:5000/add-stock', verify=False, json=json)
