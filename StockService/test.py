import threading
from urllib import parse

import requests
import yfinance as yf
import time


def functionForTicker(stock):
    x = yf.Ticker(stock)
    print(x.info)


if __name__ == '__main__':
    from app.database.models import Price
    while True:
        functionForTicker("GMS")