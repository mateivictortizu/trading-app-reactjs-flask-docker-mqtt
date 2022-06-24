import json
import math
import re
from datetime import datetime

import pandas as pd
import yfinance as yf
from sqlalchemy import CheckConstraint

from app import db, data_logo


def stock_data(ticker, period, interval, observation):
    ticker_history = ticker.history(period, interval)
    sf = ticker_history[observation]
    df = pd.DataFrame({'Date': sf.index, 'Values': sf.values})
    lista = []
    for i in range(0, len(df['Date'].tolist())):
        values = {"x": df['Date'].tolist()[i].strftime("%d-%m-%Y %H:%M"), "y": round(df['Values'].tolist()[i], 2)}
        if math.isnan(values['y']) is False:
            lista.append(values)
    return lista


class Stock(db.Model):
    __tablename__ = 'stocks'

    stock_symbol = db.Column(db.String(10), primary_key=True, unique=True)
    company_name = db.Column(db.String(100), nullable=False)
    logo = db.Column(db.String(255), nullable=False)
    employees = db.Column(db.Integer, nullable=True)
    sector = db.Column(db.String(40), nullable=False)
    industry = db.Column(db.String(40), nullable=False)
    market_name = db.Column(db.String(20), nullable=False)
    currency = db.Column(db.String(5), nullable=False)
    longBuisnessSummary = db.Column(db.Text(), nullable=False)
    isin = db.Column(db.String(50), nullable=False)
    one_day = db.Column(db.JSON, nullable=True)
    one_month = db.Column(db.JSON, nullable=True)
    three_month = db.Column(db.JSON, nullable=True)
    six_month = db.Column(db.JSON, nullable=True)
    max = db.Column(db.JSON, nullable=True)

    def __init__(self, stock_symbol):
        self.stock_symbol = stock_symbol.upper()
        search_stock = yf.Ticker(self.stock_symbol)
        if 'longName' in search_stock.info.keys() and search_stock.info['longName'] is not None:
            self.company_name = search_stock.info['longName']
        else:
            return
        if 'longBusinessSummary' in search_stock.info.keys() and search_stock.info['longBusinessSummary'] is not None:
            self.longBuisnessSummary = search_stock.info['longBusinessSummary']
        else:
            return
        if self.stock_symbol in data_logo:
            self.logo = data_logo[self.stock_symbol]
        else:
            if 'logo_url' in search_stock.info.keys() and search_stock.info['logo_url'] is not None:
                self.logo = search_stock.info['logo_url']
            else:
                return
        self.employees = search_stock.info['fullTimeEmployees'] if 'fullTimeEmployees' in search_stock.info.keys() \
            else None
        if 'sector' in search_stock.info.keys() and search_stock.info['sector'] is not None:
            self.sector = search_stock.info['sector']
        else:
            return
        if 'industry' in search_stock.info.keys() and search_stock.info['industry'] is not None:
            self.industry = search_stock.info['industry']
        else:
            return
        if 'market' in search_stock.info.keys() and search_stock.info['market'] is not None:
            self.market_name = search_stock.info['market']
        else:
            return
        if 'financialCurrency' in search_stock.info.keys() and search_stock.info['financialCurrency'] is not None:
            self.currency = search_stock.info['financialCurrency']
        else:
            return
        self.isin = search_stock.isin

        self.one_day = json.dumps(stock_data(search_stock, '1d', '30m', 'Close'))
        self.one_month = json.dumps(stock_data(search_stock, '1mo', '1d', 'Close'))
        self.three_month = json.dumps(stock_data(search_stock, '3mo', '1d', 'Close'))
        self.six_month = json.dumps(stock_data(search_stock, '6mo', '5d', 'Close'))
        self.max = json.dumps(stock_data(search_stock, 'max', '3mo', 'Close'))

    def to_json(self):
        return {'stock_symbol': self.stock_symbol, 'company_name': self.company_name, 'employees': self.employees,
                'sector': self.sector, 'industry': self.industry, 'isin': self.isin, 'market_name': self.market_name,
                'currency': self.currency, 'logo': self.logo, 'longBusinessSummary': self.longBuisnessSummary,
                'one_day': self.one_day, 'one_month': self.one_month, 'three_month': self.three_month,
                'six_month': self.six_month, 'maxim': self.max}

    @staticmethod
    def check_if_exists(stock_symbol, session):
        search_stock = session.query(Stock).filter_by(stock_symbol=stock_symbol).first()
        session.close()
        if search_stock is None:
            return False
        return True


class Price(db.Model):
    __tablename__ = 'prices'
    stock_symbol = db.Column(db.String(10), primary_key=True, unique=True)
    company_name = db.Column(db.String(100), nullable=False)
    logo = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    recommendation = db.Column(db.String(20), nullable=False)
    targetLow = db.Column(db.Float, nullable=False)
    targetMean = db.Column(db.Float, nullable=False)
    targetHigh = db.Column(db.Float, nullable=False)
    recommendationMean = db.Column(db.Float, nullable=False)
    updown = db.Column(db.Boolean, default=True)
    lastModify = db.Column(db.DateTime)
    CheckConstraint('price >=0', name='priceChecking')

    def __init__(self, stock_symbol):
        self.stock_symbol = stock_symbol.upper()
        try:
            search_stock = yf.Ticker(self.stock_symbol)
        except Exception:
            return
        if 'shortName' in search_stock.info.keys() and search_stock.info['shortName'] is not None:
            self.company_name = re.split(' Corporation|,|Group ', search_stock.info['shortName'])[0]
        else:
            return
        if self.stock_symbol in data_logo:
            self.logo = data_logo[self.stock_symbol]
        else:
            if 'logo_url' in search_stock.info.keys() and search_stock.info['logo_url'] is not None:
                self.logo = search_stock.info['logo_url']
            else:
                return
        if 'currentPrice' in search_stock.info.keys() and search_stock.info['currentPrice'] is not None:
            self.price = search_stock.info['currentPrice']
        else:
            return
        if 'recommendationKey' in search_stock.info.keys() and search_stock.info['recommendationKey'] is not None:
            self.recommendation = search_stock.info['recommendationKey']
        if 'targetLowPrice' in search_stock.info.keys() and search_stock.info['targetLowPrice'] is not None:
            self.targetLow = search_stock.info['targetLowPrice']
        if 'targetMeanPrice' in search_stock.info.keys() and search_stock.info['targetMeanPrice'] is not None:
            self.targetMean = search_stock.info['targetMeanPrice']
        else:
            return
        if 'targetHighPrice' in search_stock.info.keys() and search_stock.info['targetHighPrice'] is not None:
            self.targetHigh = search_stock.info['targetHighPrice']
        else:
            return
        if 'recommendationMean' in search_stock.info.keys() and search_stock.info['recommendationMean'] is not None:
            self.recommendationMean = search_stock.info['recommendationMean']
        else:
            return
        self.lastModify = datetime.utcnow()

    def to_json(self):
        return {'stock_symbol': self.stock_symbol, 'company_name': self.company_name, 'price': self.price,
                'recommendation': self.recommendation, 'logo': self.logo,
                'targetLow': self.targetLow, 'targetMean': self.targetMean, 'targetHigh': self.targetHigh,
                'recommendationMean': self.recommendationMean, 'lastModify': self.lastModify}

    @staticmethod
    def update_price(price_item, session):
        if isinstance(price_item, Price):
            search_price = session.query(Price).filter_by(stock_symbol=price_item.stock_symbol).first()
            if search_price is None:
                session.close()
                return False
            else:
                search_price.price = price_item.price
                search_price.company_name = price_item.company_name
                search_price.logo = price_item.logo
                search_price.recommendation = price_item.recommendation
                search_price.targetLow = price_item.targetLow
                search_price.targetMean = price_item.targetMean
                search_price.targetHigh = price_item.targetHigh
                search_price.recommendationMean = price_item.recommendationMean
                search_price.lastModify = datetime.utcnow()
                session.commit()
                session.close()
                return True
        else:
            session.close()
            return False

    @staticmethod
    def check_if_exists(stock_symbol, session):
        search_price = session.query(Price).filter_by(stock_symbol=stock_symbol).first()
        session.close()
        if search_price is None:
            return False
        return True


class Watchlist(db.Model):
    __tablename__ = 'watchlist'

    wishlist_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user = db.Column(db.String(35), nullable=False)
    stock_symbol = db.Column(db.String(10), nullable=False)

    def __init__(self, user, stock_symbol):
        self.user = user
        self.stock_symbol = stock_symbol

    def to_json(self):
        return {'stock_symbol': self.stock_symbol, 'user': self.user}

    @staticmethod
    def check_if_exists(stock_symbol, user,  session):
        search_watchlist = session.query(Watchlist).filter_by(stock_symbol=stock_symbol, user=user).first()
        session.close()
        if search_watchlist is None:
            return False
        return True
