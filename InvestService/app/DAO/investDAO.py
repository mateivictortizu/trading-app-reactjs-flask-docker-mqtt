from app.database.models import Invest


def buy_investDAO(user, stock_symbol, cantitate, price):
    Invest.buy_invest(user, stock_symbol, cantitate, price)


def sell_investDAO(user, stock_symbol, cantitate, price):
    Invest.sell_invest(user, stock_symbol, cantitate, price)
