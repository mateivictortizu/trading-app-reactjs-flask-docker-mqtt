import time
from datetime import datetime, timedelta

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
    check_price = Price.check_if_exists(stock_symbol=stock_symbol)
    if check_price is False:
        new_price = Price(stock_symbol=stock_symbol)
        db.session.add(new_stock)
        db.session.add(new_price)
    elif check_price is True:
        update_price = Price(stock_symbol=stock_symbol)
        db.session.add(new_stock)
        Price.update_price(update_price)
    db.session.commit()
    db.session.close()


# TODO check update stock async and rework it in case of errors
def updateStockAsync(stock_symbol, date):
    if datetime.utcnow() > date + timedelta(seconds=30):
        db.session.close()
        return
    bad_check = False
    stock_symbol = stock_symbol.upper()
    try:
        stock = db.session.query(Stock).filter_by(stock_symbol=stock_symbol).first()
        try:
            search_stock = yfinance.Ticker(stock_symbol)
        except Exception:
            bad_check = True
            raise Exception('Cannot receive data from server')

        if 'longName' in search_stock.info.keys() and search_stock.info['longName'] is not None:
            stock.company_name = search_stock.info['longName']
        else:
            bad_check = True

        if 'logo_url' in search_stock.info.keys() and search_stock.info['logo_url'] is not None:
            stock.logo = requests.get(search_stock.info['logo_url']).content
        else:
            bad_check = True

        stock.employees = search_stock.info['fullTimeEmployees'] if 'fullTimeEmployees' in search_stock.info.keys() \
            else None

        if 'sector' in search_stock.info.keys() and search_stock.info['sector'] is not None:
            stock.sector = search_stock.info['sector']
        else:
            bad_check = True

        if 'industry' in search_stock.info.keys() and search_stock.info['industry'] is not None:
            stock.industry = search_stock.info['industry']
        else:
            bad_check = True

        if 'market' in search_stock.info.keys() and search_stock.info['market'] is not None:
            stock.market_name = search_stock.info['market']
        else:
            bad_check = True

        if 'financialCurrency' in search_stock.info.keys() and search_stock.info['financialCurrency'] is not None:
            stock.currency = search_stock.info['financialCurrency']
        else:
            bad_check = True
        stock.isin = search_stock.isin
        if bad_check is False:
            db.session.commit()
    finally:
        db.session.close()


def updateStockDAO():
    stocks = db.session.query(Stock).all()
    db.session.close()
    for stock in stocks:
        t = threading.Thread(target=updateStockAsync, args=(stock.stock_symbol, datetime.utcnow()))
        t.daemon = True
        print("Start")
        t.start()
        time.sleep(300)


def updatePriceAsync(stock_symbol, date):
    if datetime.utcnow() > date + timedelta(seconds=7):
        db.session.commit()
        db.session.close()
        return
    stock_symbol = stock_symbol.upper()
    try:
        price = db.session.query(Price).filter_by(stock_symbol=stock_symbol).first()
        bad_check = False
        try:
            search_price = yfinance.Ticker(price.stock_symbol)
        except Exception:
            bad_check = True
            raise Exception('Cannot receive data from server')
        if 'currentPrice' in search_price.info.keys() and search_price.info['currentPrice'] is not None:
            price.price = search_price.info['currentPrice']
        else:
            bad_check = True

        if 'recommendationKey' in search_price.info.keys() and search_price.info['recommendationKey'] is not None:
            price.recommendation = search_price.info['recommendationKey']
        else:
            bad_check = True

        if 'targetLowPrice' in search_price.info.keys() and search_price.info['targetLowPrice'] is not None:
            price.targetLow = search_price.info['targetLowPrice']
        else:
            bad_check = True

        if 'targetMeanPrice' in search_price.info.keys() and search_price.info['targetMeanPrice'] is not None:
            price.targetMean = search_price.info['targetMeanPrice']
        else:
            bad_check = True

        if 'targetHighPrice' in search_price.info.keys() and search_price.info['targetHighPrice'] is not None:
            price.targetHigh = search_price.info['targetHighPrice']
        else:
            bad_check = True
        if 'recommendationMean' in search_price.info.keys() and search_price.info['recommendationMean'] is not None:
            price.recommendationMean = search_price.info['recommendationMean']
        else:
            bad_check = True

        if db.session.query(Price).filter_by(stock_symbol=stock_symbol).first().lastModify < date:
            price.lastModify = date
            if bad_check is False:
                db.session.commit()
            else:
                price = None
                db.session.commit()
    finally:
        db.session.close()


def updatePriceDAO():
    prices = db.session.query(Price).all()
    db.session.close()
    for price in prices:
        if isinstance(price, Price):
            t = threading.Thread(target=updatePriceAsync, args=(price.stock_symbol, datetime.utcnow()))
            t.daemon = True
            t.start()
