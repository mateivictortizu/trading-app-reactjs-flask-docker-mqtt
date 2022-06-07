import json
import threading
import time
from datetime import datetime, timedelta

import yfinance
from sqlalchemy.orm import sessionmaker

from app import engine
from app.database.models import Stock, Price, stock_data
import re


def getStockInfoDAO(stock_symbol):
    Session = sessionmaker(bind=engine)
    session = Session()
    stock = session.query(Stock).filter_by(stock_symbol=stock_symbol).first()
    session.close()
    return stock


def getStockPriceDAO(stock_symbol):
    Session = sessionmaker(bind=engine)
    session = Session()
    stock = session.query(Price).filter_by(stock_symbol=stock_symbol).first()
    session.close()
    return stock


def addStockDAO(stock_symbol):
    Session = sessionmaker(bind=engine)
    session = Session()
    stock_symbol = stock_symbol.upper()
    new_stock = None
    new_price = None
    if Stock.check_if_exists(stock_symbol, session) is False:
        new_stock = Stock(stock_symbol=stock_symbol)
        if new_stock.company_name is None:
            session.close()
            return False
    new_price = Price(stock_symbol=stock_symbol)
    if new_price.price is None:
        session.close()
        return False

    if Price.check_if_exists(stock_symbol=stock_symbol, session=session) is False:
        session.add(new_price)
    else:
        Price.update_price(new_price, session)
    if new_stock is not None:
        session.add(new_stock)
    session.commit()
    session.close()


def updateStockAsync(stock_symbol, date):
    Session = sessionmaker(bind=engine)
    session = Session()
    if datetime.utcnow() > date + timedelta(seconds=30):
        session.close()
        return
    bad_check = False
    stock_symbol = stock_symbol.upper()
    try:
        stock = session.query(Stock).filter_by(stock_symbol=stock_symbol).first()
        try:
            search_stock = yfinance.Ticker(stock_symbol)
        except:
            bad_check = True
            session.close()
            raise Exception('Cannot receive data from server')

        if 'longName' in search_stock.info.keys() and search_stock.info['longName'] is not None:
            stock.company_name = search_stock.info['longName']
        else:
            bad_check = True

        if 'logo_url' in search_stock.info.keys() and search_stock.info['logo_url'] is not None:
            stock.logo = search_stock.info['logo_url']
        else:
            bad_check = True

        if 'longBusinessSummary' in search_stock.info.keys() and search_stock.info['longBusinessSummary'] is not None:
            stock.longBuisnessSummary = search_stock.info['longBusinessSummary']
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

        stock.one_day = json.dumps(stock_data(search_stock, '1d', '30m', 'Close'))
        stock.one_month = json.dumps(stock_data(search_stock, '1mo', '1d', 'Close'))
        stock.three_month = json.dumps(stock_data(search_stock, '3mo', '1d', 'Close'))
        stock.six_month = json.dumps(stock_data(search_stock, '6mo', '5d', 'Close'))
        stock.max = json.dumps(stock_data(search_stock, 'max', '3mo', 'Close'))
        stock.isin = search_stock.isin
        if bad_check is False:
            session.commit()
    finally:
        session.close()


def updateStockDAO():
    Session = sessionmaker(bind=engine)
    session = Session()
    stocks = session.query(Stock).all()
    session.close()
    for stock in stocks:
        t = threading.Thread(target=updateStockAsync, args=(stock.stock_symbol, datetime.utcnow()))
        t.daemon = True
        t.start()
        # time.sleep(300)


def updatePriceAsync(stock_symbol, date):
    Session = sessionmaker(bind=engine)
    session = Session()
    if datetime.utcnow() > date + timedelta(seconds=7):
        session.close()
        return
    stock_symbol = stock_symbol.upper()
    try:
        price = session.query(Price).filter_by(stock_symbol=stock_symbol).first()
        bad_check = False
        try:
            search_price = yfinance.Ticker(price.stock_symbol)
        except:
            session.close()
            bad_check = True
            print("BAD")
            raise Exception('Cannot receive data from server')
        if 'shortName' in search_price.info.keys() and search_price.info['shortName'] is not None:
            price.company_name = re.split(' Corporation|,|Group ', search_price.info['shortName'])[0]
        else:
            bad_check = True

        if 'logo_url' in search_price.info.keys() and search_price.info['logo_url'] is not None:
            price.logo = search_price.info['logo_url']
        else:
            bad_check = True
        if bad_check is False:
            if 'currentPrice' in search_price.info.keys() and search_price.info['currentPrice'] is not None:
                if price.price > search_price.info['currentPrice']:
                    price.updown = False
                else:
                    price.updown = True
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

            if session.query(Price).filter_by(stock_symbol=stock_symbol).first().lastModify < date:
                price.lastModify = date
                if bad_check is False:
                    session.commit()
    except:
        print('EXCEPT')
        session.close()
    finally:
        session.close()


def updatePriceDAO():
    Session = sessionmaker(bind=engine)
    session = Session()
    prices = session.query(Price).all()
    session.close()
    for price in prices:
        if isinstance(price, Price):
            t = threading.Thread(target=updatePriceAsync, args=(price.stock_symbol, datetime.utcnow()))
            t.daemon = True
            t.start()
            time.sleep(0.1)


def get_all_stocksDAO():
    Session = sessionmaker(bind=engine)
    session = Session()
    stock = session.query(Price).all()
    session.close()
    return stock