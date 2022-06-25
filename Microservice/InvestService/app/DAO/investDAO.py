from app.database.models import Invest


def buy_investDAO(user, stock_symbol, cantitate, price):
    Invest.buy_invest(user, stock_symbol, cantitate, price)


def sell_investDAO(user, stock_symbol, cantitate, price):
    Invest.sell_invest(user, stock_symbol, cantitate, price)


def get_stock_invest_by_userDAO(user, stock_symbol):
    list_of_invest = Invest.get_stock_invest_by_user(user, stock_symbol)
    average = 0.0
    no_of_buy = 0.0
    cantitate = 0.0
    for i in list_of_invest:
        if i.action_type == "BUY":
            average = average + i.cantitate * i.price
            no_of_buy = no_of_buy + i.cantitate
            cantitate = cantitate + i.cantitate
        else:
            cantitate = cantitate - i.cantitate

    if cantitate > 0:
        average = average / round(no_of_buy, 3)
        return [round(cantitate, 2), round(average, 2)]
    else:
        return None


def get_invest_by_userDAO(user):
    list_of_invest = Invest.get_invest_by_user(user)
    return list_of_invest


def get_user_sumarryDAO(user):
    result = get_invest_by_userDAO(user)
    stock_dict = dict()
    total_quantity = 0
    for i in result:
        if i.action_type == 'BUY':
            if i.stock_symbol not in stock_dict:
                stock_dict[i.stock_symbol] = i.cantitate * i.price
            else:
                stock_dict[i.stock_symbol] = stock_dict[i.stock_symbol] + i.cantitate * i.price
            total_quantity = total_quantity + i.cantitate * i.price
        else:
            if i.stock_symbol not in stock_dict:
                stock_dict[i.stock_symbol] = -i.cantitate * i.price
            else:
                stock_dict[i.stock_symbol] = stock_dict[i.stock_symbol] - i.cantitate * i.price
            total_quantity = total_quantity - i.cantitate * i.price
    for i in stock_dict:
        stock_dict[i] = round(stock_dict[i] / total_quantity * 100, 2)
    return stock_dict


def get_usersDAO():
    users = Invest.get_users_with_invest()
    users_invest = {}
    for i in users:
        users_invest[i[0]] = get_user_sumarryDAO(i[0])
    return users_invest
