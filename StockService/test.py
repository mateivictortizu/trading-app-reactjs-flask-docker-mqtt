import threading
from urllib import parse

import requests
import yfinance as yf
import time


def functionForTicker(stock):
    x = yf.Ticker(stock)
    print(x.info)


if __name__ == '__main__':
    start_time = time.time()
    tickers = yf.Tickers("MSFT TSLA AMD GOOGL AMZN")
    print(tickers.tickers["MSFT"].info)
    print(tickers.tickers["TSLA"].info)
    print(tickers.tickers["AMD"].info)
    print(tickers.tickers["GOOGL"].info)
    print(tickers.tickers["AMZN"].info)
    print("LIST--- %s seconds ---\n" % (time.time() - start_time))

    start_time = time.time()
    msft = yf.Ticker("MSFT")
    tsla = yf.Ticker("TSLA")
    amd = yf.Ticker("AMD")
    googl = yf.Ticker("GOOGL")
    amzn = yf.Ticker("AMZN")
    print(msft.info)
    print(tsla.info)
    print(amd.info)
    print(googl.info)
    print(amzn.info)
    print("ITEM BY ITEM--- %s seconds ---\n" % (time.time() - start_time))

    stock_list = ["MSFT", 'TSLA', 'AMD', 'GOOGL', 'AMZN']
    thread_list = []
    start_time = time.time()
    for stock in stock_list:
        t = threading.Thread(target=functionForTicker, args=(stock,))
        thread_list.append(t)
        t.start()
    for t in thread_list:
        t.join()
    print("THREADS:--- %s seconds ---" % (time.time() - start_time))
