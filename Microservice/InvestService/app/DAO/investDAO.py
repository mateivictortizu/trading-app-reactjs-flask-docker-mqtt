from app.database.models import Invest


def buy_investDAO(user, stock_symbol, cantitate, price):
    Invest.buy_invest(user, stock_symbol, cantitate, price)


def sell_investDAO(user, stock_symbol, cantitate, price):
    Invest.sell_invest(user, stock_symbol, cantitate, price)


def get_stock_invest_by_userDAO(user, stock_symbol):
    list_of_invest = Invest.get_stock_invest_by_user(user, stock_symbol)
    average = 0
    no_of_buy = 0
    cantitate = 0
    for i in list_of_invest:
        if i.action_type == "BUY":
            average = average + i.cantitate * i.price
            no_of_buy = no_of_buy + i.cantitate
            print(no_of_buy)
            cantitate = cantitate + i.cantitate
        else:
            cantitate = cantitate - i.cantitate

    if cantitate > 0:
        average = average / round(no_of_buy, 3)
        return [cantitate, average]
    else:
        return None


def get_invest_by_userDAO(user):
    list_of_invest = Invest.get_invest_by_user(user)
    return list_of_invest
