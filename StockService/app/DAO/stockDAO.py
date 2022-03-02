from datetime import datetime

import requests
import yfinance
import threading

from app import db
from app.database.models import Stock, Price


def addStockDAO(stock_symbol):
    new_stock = Stock(stock_symbol=stock_symbol)
    db.session.add(new_stock)
    db.session.commit()
    if new_stock.company_name is None:
        return False
    check_stock = Stock.check_if_exists(stock_symbol=stock_symbol)
    if check_stock is False:
        check_price = Price.check_if_exists(stock_symbol=stock_symbol)
        if check_price is False:
            new_price = Price(stock_symbol=stock_symbol)
            Price.add_to_price(new_price)
        elif check_price is True:
            update_price = Price(stock_symbol=stock_symbol)
            Price.update_price(update_price)
        db.session.add(new_stock)
        db.session.commit()


def updateStockAsync(stock):
    search_stock = yfinance.Ticker(stock.stock_symbol)
    stock.company_name = search_stock.info['longName'] if 'longName' in search_stock.info.keys() else None
    stock.logo = requests.get(search_stock.info['logo_url']).content if 'logo_url' in search_stock.info.keys() \
        else None
    stock.employees = search_stock.info['fullTimeEmployees'] if 'fullTimeEmployees' in search_stock.info.keys() \
        else None
    stock.sector = search_stock.info['sector'] if 'sector' in search_stock.info.keys() else None
    stock.industry = search_stock.info['industry'] if 'sector' in search_stock.info.keys() else None
    stock.market_name = search_stock.info['market'] if 'market' in search_stock.info.keys() else None
    stock.currency = search_stock.info['financialCurrency'] if 'financialCurrency' in search_stock.info.keys() \
        else None
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
    price = Price.query.filter_by(stock_symbol=stock_symbol).first()
    search_price = yfinance.Ticker(price.stock_symbol)
    price.price = search_price.info['currentPrice'] if 'currentPrice' in search_price.info.keys() else None
    price.recommendation = search_price.info['recommendationKey'] if 'recommendationKey' in \
                                                                     search_price.info.keys() else None
    price.targetLow = search_price.info['targetLowPrice'] if 'targetLowPrice' in search_price.info.keys() \
        else None
    price.targetMean = search_price.info['targetMeanPrice'] if 'targetMeanPrice' in search_price.info.keys() \
        else None
    price.targetHigh = search_price.info['targetHighPrice'] if 'targetHighPrice' in search_price.info.keys() \
        else None
    price.recommendationMean = search_price.info['recommendationMean'] if 'recommendationMean' in \
                                                                          search_price.info.keys() else None

    if Price.query.filter_by(stock_symbol=stock_symbol).first().lastModify < date \
            and not (price.targetLow is None or price.targetMean is None or price.targetHigh is None
                     or price.recommendationMean is None):
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
