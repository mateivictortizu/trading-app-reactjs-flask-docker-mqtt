import json
import random
import re
import threading
from datetime import datetime, timedelta

import yfinance
from sqlalchemy.orm import sessionmaker

from app import data_logo
from app import engine
from app.database.models import Stock, Price, stock_data, Watchlist


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
    if datetime.utcnow() > date + timedelta(seconds=10):
        return
    bad_check = False
    stock_symbol = stock_symbol.upper()
    try:
        if stock_symbol != "TUIASI":
            try:
                search_stock = yfinance.Ticker(stock_symbol)
                search_stock_info = search_stock.info
            except:
                bad_check = True
                raise Exception('Cannot receive data from server')
            Session = sessionmaker(bind=engine)
            session = Session()
            stock = session.query(Stock).filter_by(stock_symbol=stock_symbol).first()
            if 'longName' in search_stock_info.keys() and search_stock_info['longName'] is not None:
                stock.company_name = search_stock_info['longName']
            else:
                bad_check = True

            if stock.stock_symbol in data_logo:
                stock.logo = data_logo[stock.stock_symbol]
            else:
                if 'logo_url' in search_stock_info.keys() and search_stock_info['logo_url'] is not None:
                    stock.logo = search_stock_info['logo_url']
                else:
                    bad_check = True

            if 'longBusinessSummary' in search_stock_info.keys() and search_stock_info[
                'longBusinessSummary'] is not None:
                stock.longBuisnessSummary = search_stock_info['longBusinessSummary']
            else:
                bad_check = True

            stock.employees = search_stock_info['fullTimeEmployees'] if 'fullTimeEmployees' in search_stock_info.keys() \
                else None

            if 'sector' in search_stock_info.keys() and search_stock_info['sector'] is not None:
                stock.sector = search_stock_info['sector']
            else:
                bad_check = True

            if 'industry' in search_stock_info.keys() and search_stock_info['industry'] is not None:
                stock.industry = search_stock_info['industry']
            else:
                bad_check = True

            if 'market' in search_stock_info.keys() and search_stock_info['market'] is not None:
                stock.market_name = search_stock_info['market']
            else:
                bad_check = True

            if 'financialCurrency' in search_stock_info.keys() and search_stock_info['financialCurrency'] is not None:
                stock.currency = search_stock_info['financialCurrency']
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
            session.close()
    except Exception as e:
        print(e)


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
    if datetime.utcnow() > date + timedelta(seconds=7):
        return
    stock_symbol = stock_symbol.upper()
    try:
        bad_check = False
        if stock_symbol != 'TUIASI':
            try:
                search_price = yfinance.Ticker(stock_symbol)
                search_price = search_price.info
            except:
                bad_check = True
                raise Exception('Cannot receive data from server')
            Session = sessionmaker(bind=engine)
            session = Session()
            price = session.query(Price).filter_by(stock_symbol=stock_symbol).first()
            if 'shortName' in search_price.keys() and search_price['shortName'] is not None:
                price.company_name = re.split(' Corporation|,|Group ', search_price['shortName'])[0]
            else:
                bad_check = True

            if price.stock_symbol in data_logo:
                price.logo = data_logo[price.stock_symbol]
            else:
                if 'logo_url' in search_price.keys() and search_price['logo_url'] is not None:
                    price.logo = search_price['logo_url']
                else:
                    bad_check = True
            if bad_check is False:
                if 'currentPrice' in search_price.keys() and search_price['currentPrice'] is not None:
                    if price.price > search_price['currentPrice']:
                        price.updown = False
                    else:
                        price.updown = True
                    price.price = search_price['currentPrice']
                else:
                    bad_check = True

                if 'recommendationKey' in search_price.keys() and search_price['recommendationKey'] is not None:
                    price.recommendation = search_price['recommendationKey']
                else:
                    bad_check = True

                if 'targetLowPrice' in search_price.keys() and search_price['targetLowPrice'] is not None:
                    price.targetLow = search_price['targetLowPrice']
                else:
                    bad_check = True

                if 'targetMeanPrice' in search_price.keys() and search_price['targetMeanPrice'] is not None:
                    price.targetMean = search_price['targetMeanPrice']
                else:
                    bad_check = True

                if 'targetHighPrice' in search_price.keys() and search_price['targetHighPrice'] is not None:
                    price.targetHigh = search_price['targetHighPrice']
                else:
                    bad_check = True
                if 'recommendationMean' in search_price.keys() and search_price['recommendationMean'] is not None:
                    price.recommendationMean = search_price['recommendationMean']
                else:
                    bad_check = True

                if price.lastModify < date:
                    if bad_check is False:
                        price.lastModify = date
                        session.commit()
                session.close()
        else:
            Session = sessionmaker(bind=engine)
            session = Session()
            price = session.query(Price).filter_by(stock_symbol=stock_symbol).first()
            price.price = random.randrange(90, 100)
            session.commit()
            session.close()
    except Exception as e:
        print(e)


def updatePriceDAO():
    Session = sessionmaker(bind=engine)
    session = Session()
    prices = session.query(Price).all()
    session.close()
    for price in prices:
        if isinstance(price, Price):
            t = threading.Thread(target=updatePriceAsync, args=(price.stock_symbol, datetime.utcnow()))
            t.start()


def get_all_stocksDAO():
    Session = sessionmaker(bind=engine)
    session = Session()
    stock = session.query(Price).all()
    session.close()
    return stock


def addToWatchlistDAO(stock_symbol, user):
    Session = sessionmaker(bind=engine)
    session = Session()
    stock_symbol = stock_symbol.upper()
    if Watchlist.check_if_exists(stock_symbol, user, session) is False:
        new_watchlist = Watchlist(stock_symbol=stock_symbol, user=user)
        session.add(new_watchlist)
    session.commit()
    session.close()


def removeFromWatchlistDAO(stock_symbol, user):
    Session = sessionmaker(bind=engine)
    session = Session()
    stock_symbol = stock_symbol.upper()
    if Watchlist.check_if_exists(stock_symbol, user, session) is True:
        result = session.query(Watchlist).filter_by(stock_symbol=stock_symbol, user=user).first()
        session.delete(result)
    session.commit()
    session.close()


def join_watchlist(user):
    Session = sessionmaker(bind=engine)
    session = Session()
    stocks = get_all_stocksDAO()
    result_list = []
    if stocks is not None:
        for i in stocks:
            if Watchlist.check_if_exists(i.stock_symbol, user, session) is True:
                result = i.to_json()
                result['watchlist'] = True
            else:
                result = i.to_json()
                result['watchlist'] = False
            result_list.append(result)
    session.commit()
    session.close()
    return result_list
