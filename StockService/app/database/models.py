from datetime import datetime

import requests
import yfinance as yf
from sqlalchemy import CheckConstraint

from app import db


class Stock(db.Model):
    __tablename__ = 'stocks'

    stock_symbol = db.Column(db.String(10), primary_key=True, unique=True)
    company_name = db.Column(db.String(100), nullable=False)
    logo = db.Column(db.LargeBinary, nullable=False)
    employees = db.Column(db.Integer, nullable=True)
    sector = db.Column(db.String(40), nullable=False)
    industry = db.Column(db.String(40), nullable=False)
    market_name = db.Column(db.String(20), nullable=False)
    currency = db.Column(db.String(5), nullable=False)
    isin = db.Column(db.String(50), nullable=False)

    def __init__(self, stock_symbol):
        self.stock_symbol = stock_symbol.upper()
        search_stock = yf.Ticker(self.stock_symbol)
        if 'longName' in search_stock.info.keys() and search_stock.info['longName'] is not None:
            self.company_name = search_stock.info['longName']
        else:
            return
        if 'logo_url' in search_stock.info.keys() and search_stock.info['logo_url'] is not None:
            self.logo = requests.get(search_stock.info['logo_url']).content
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


class Price(db.Model):
    __tablename__ = 'prices'
    stock_symbol = db.Column(db.String(10), primary_key=True, unique=True)
    price = db.Column(db.Float, nullable=False)
    recommendation = db.Column(db.String(20), nullable=False)
    targetLow = db.Column(db.Float, nullable=False)
    targetMean = db.Column(db.Float, nullable=False)
    targetHigh = db.Column(db.Float, nullable=False)
    recommendationMean = db.Column(db.Float, nullable=False)
    lastModify = db.Column(db.DateTime)
    CheckConstraint('price >=0', name='priceChecking')

    def __init__(self, stock_symbol):
        self.stock_symbol = stock_symbol.upper()
        try:
            search_stock = yf.Ticker(self.stock_symbol)
        except Exception:
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

    @staticmethod
    def update_price(price_item):
        if isinstance(price_item, Price):
            search_price = db.session.query(Price).filter_by(stock_symbol=price_item.stock_symbol).first()
            if search_price is None:
                db.session.remove()
                return False
            else:
                search_price.price = price_item.price
                search_price.recommendation = price_item.recommendation
                search_price.targetLow = price_item.targetLow
                search_price.targetMean = price_item.targetMean
                search_price.targetHigh = price_item.targetHigh
                search_price.recommendationMean = price_item.recommendationMean
                search_price.lastModify = datetime.utcnow()
                db.session.commit()
                db.session.remove()
                return True
        else:
            db.session.remove()
            return False

    @staticmethod
    def check_if_exists(stock_symbol):
        search_price = db.session.query(Price).filter_by(stock_symbol=stock_symbol).first()
        db.session.remove()
        if search_price is None:
            return False
        return True