import requests
import yfinance
import threading

from app import db
from app.database.models import Stock


def addStockDAO(stock_symbol):
    new_stock = Stock(stock_symbol=stock_symbol)
    if new_stock.company_name is None:
        return False
    check_stock = Stock.check_if_exists(stock_symbol=stock_symbol)
    if check_stock is False:
        Stock.add_to_stock(new_stock)


def updateStockAsync(user):
    print(user.stock_symbol)
    search_stock = yfinance.Ticker(user.stock_symbol)
    user.company_name = search_stock.info['longName'] if 'longName' in search_stock.info.keys() else None
    user.logo = requests.get(search_stock.info['logo_url']).content if 'logo_url' in search_stock.info.keys() \
        else None
    user.employees = search_stock.info['fullTimeEmployees'] if 'fullTimeEmployees' in search_stock.info.keys() \
        else None
    user.sector = search_stock.info['sector'] if 'sector' in search_stock.info.keys() else None
    user.industry = search_stock.info['industry'] if 'sector' in search_stock.info.keys() else None
    user.market_name = search_stock.info['market'] if 'market' in search_stock.info.keys() else None
    user.currency = search_stock.info['financialCurrency'] if 'financialCurrency' in search_stock.info.keys() \
        else None
    user.isin = search_stock.isin


def updateStockDAO():
    users = Stock.query.all()
    list_threads = []
    for user in users:
        t = threading.Thread(target=updateStockAsync, args=(user,))
        list_threads.append(t)
        t.start()
    for t in list_threads:
        t.join()
    db.session.commit()
