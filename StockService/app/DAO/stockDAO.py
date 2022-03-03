from datetime import datetime

import requests
import yfinance
import threading

from app import db
from app.database.models import Stock, Price


def addStockDAO(stock_symbol):
    stock_symbol = stock_symbol.upper()
    new_stock = Stock(stock_symbol=stock_symbol)
    if new_stock.company_name is None:
        return False
    db.session.add(new_stock)
    check_price = Price.check_if_exists(stock_symbol=stock_symbol)
    if check_price is False:
        new_price = Price(stock_symbol=stock_symbol)
        db.session.add(new_price)
    elif check_price is True:
        update_price = Price(stock_symbol=stock_symbol)
        Price.update_price(update_price)
    db.session.commit()


def updateStockAsync(stock):
    search_stock = yfinance.Ticker(stock.stock_symbol.upper())
    if 'longName' in search_stock.info.keys() and search_stock.info['longName'] is not None:
        stock.company_name = search_stock.info['longName']
    else:
        return

    if 'logo_url' in search_stock.info.keys() and search_stock.info['logo_url'] is not None:
        stock.logo = requests.get(search_stock.info['logo_url']).content
    else:
        return

    stock.employees = search_stock.info['fullTimeEmployees'] if 'fullTimeEmployees' in search_stock.info.keys() \
        else None

    if 'sector' in search_stock.info.keys() and search_stock.info['sector'] is not None:
        stock.sector = search_stock.info['sector']
    else:
        return

    if 'industry' in search_stock.info.keys() and search_stock.info['industry'] is not None:
        stock.industry = search_stock.info['industry']
    else:
        return
    if 'market' in search_stock.info.keys() and search_stock.info['market'] is not None:
        stock.market_name = search_stock.info['market']
    else:
        return
    if 'financialCurrency' in search_stock.info.keys() and search_stock.info['financialCurrency'] is not None:
        stock.currency = search_stock.info['financialCurrency']
    else:
        return
    stock.isin = search_stock.isin
    db.session.commit()


def updateStockDAO():
    stocks = Stock.query.all()
    list_threads = []
    for stock in stocks:
        t = threading.Thread(target=updateStockAsync, args=(stock,))
        list_threads.append(t)
        t.start()
    for t in list_threads:
        t.join()


def updatePriceAsync(stock_symbol, date):
    stock_symbol = stock_symbol.upper()
    price = Price.query.filter_by(stock_symbol=stock_symbol).first()
    search_price = yfinance.Ticker(price.stock_symbol)
    if 'currentPrice' in search_price.info.keys() and search_price.info['currentPrice'] is not None:
        price.price = search_price.info['currentPrice']
    else:
        return

    if 'recommendationKey' in search_price.info.keys() and search_price.info['recommendationKey'] is not None:
        price.recommendation = search_price.info['recommendationKey']
    else:
        return

    if 'targetLowPrice' in search_price.info.keys() and search_price.info['targetLowPrice'] is not None:
        price.targetLow = search_price.info['targetLowPrice']
    else:
        return

    if 'targetMeanPrice' in search_price.info.keys() and search_price.info['targetMeanPrice'] is not None:
        price.targetMean = search_price.info['targetMeanPrice']
    else:
        return

    if 'targetHighPrice' in search_price.info.keys() and search_price.info['targetHighPrice'] is not None:
        price.targetHigh = search_price.info['targetHighPrice']
    else:
        return
    if 'recommendationMean' in search_price.info.keys() and search_price.info['recommendationMean'] is not None:
        price.recommendationMean = search_price.info['recommendationMean']
    else:
        return

    if Price.query.filter_by(stock_symbol=stock_symbol).first().lastModify < date:
        price.lastModify = date
        db.session.commit()


def updatePriceDAO():
    prices = Price.query.all()
    db.session.close()
    list_threads = []
    for price in prices:
        if isinstance(price, Price):
            t = threading.Thread(target=updatePriceAsync, args=(price.stock_symbol, datetime.utcnow()))
            list_threads.append(t)
            t.start()
    for t in list_threads:
        t.join(4)
