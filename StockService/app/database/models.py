import requests
import yfinance as yf

from app import db


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
    isin = db.Column(db.String(50), nullable=False)

    def __init__(self, stock_symbol):
        self.stock_symbol = stock_symbol
        search_stock = yf.Ticker(self.stock_symbol)
        self.company_name = search_stock.info['longName'] if 'longName' in search_stock.info.keys() else None
        self.logo = requests.get(search_stock.info['logo_url']).content if 'logo_url' in search_stock.info.keys() \
            else None
        self.employees = search_stock.info['fullTimeEmployees'] if 'fullTimeEmployees' in search_stock.info.keys() \
            else None
        self.sector = search_stock.info['sector'] if 'sector' in search_stock.info.keys() else None
        self.industry = search_stock.info['industry'] if 'industry' in search_stock.info.keys() else None
        self.market_name = search_stock.info['market'] if 'market' in search_stock.info.keys() else None
        self.currency = search_stock.info['financialCurrency'] if 'financialCurrency' in search_stock.info.keys() \
            else None
        self.isin = search_stock.isin

    @staticmethod
    def add_to_stock(stock_item):
        db.session.add(stock_item)
        db.session.commit()

    @staticmethod
    def check_if_exists(stock_symbol):
        search_stock = Stock.query.filter_by(stock_symbol=stock_symbol).first()
        if search_stock is None:
            return False
        return True
