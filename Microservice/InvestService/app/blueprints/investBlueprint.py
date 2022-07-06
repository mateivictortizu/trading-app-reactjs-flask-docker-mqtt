from flask import Blueprint, jsonify, request
from flask_json_schema import JsonValidationError
from sqlalchemy.exc import DatabaseError

from app.DAO.investDAO import buy_investDAO, sell_investDAO, get_stock_invest_by_userDAO, get_invest_by_userDAO, \
    get_usersDAO, get_user_sumarryDAO, sell_autoinvestDAO, buy_autoinvestDAO, delete_investDAO
from app.database.models import Invest, AutoInvest

investBP = Blueprint('investBlueprint', __name__)


@investBP.errorhandler(JsonValidationError)
def validator_error(e):
    return jsonify({'error': e.message, 'errors': [validation_error.message for validation_error in e.errors]}), 400


@investBP.errorhandler(DatabaseError)
def database_error():
    return jsonify({'error': 'Database error'}), 500


@investBP.route('/buy', methods=['POST'])
def buy():
    json_body = request.json
    user = json_body['user']
    stock_symbol = json_body['stock_symbol']
    cantitate = float(json_body['cantitate'])
    price = float(json_body['price'])
    try:
        buy_investDAO(user, stock_symbol, cantitate, price)
        return jsonify({"message": "Buy Completed"}), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "Buy Fail"}), 400


@investBP.route('/sell', methods=['POST'])
def sell():
    json_body = request.json
    user = json_body['user']
    stock_symbol = json_body['stock_symbol']
    cantitate = float(json_body['cantitate'])
    price = float(json_body['price'])
    try:
        sell_investDAO(user, stock_symbol, cantitate, price)
        return jsonify({"message": "Sell Completed"}), 200
    except Exception as e:
        return jsonify({"message": "Sell Fail"}), 400


@investBP.route('/get-stock-invest-by-user', methods=['POST'])
def get_stock_invest_by_user():
    user = request.json['identifier']
    stock_symbol = request.json['stock_symbol']
    result = get_stock_invest_by_userDAO(user, stock_symbol)
    if result is None:
        return jsonify({"message": "Userul nu are investitii pentru acest stock"}), 404
    else:

        return jsonify({"message": "Userul are investitii pentru acest stock", "medie": result[1],
                        "cantitate": result[0]}), 200


@investBP.route('/get-invest-by-user', methods=['POST'])
def get_invest_by_user():
    user = request.json['identifier']
    result = get_invest_by_userDAO(user)
    stock_list = {}
    for i in result:
        if i.action_type == 'BUY':
            if i.stock_symbol not in stock_list:
                stock_list[i.stock_symbol] = i.cantitate
            else:
                stock_list[i.stock_symbol] = stock_list[i.stock_symbol] + i.cantitate
        else:
            if i.stock_symbol not in stock_list:
                stock_list[i.stock_symbol] = i.cantitate
            else:
                stock_list[i.stock_symbol] = stock_list[i.stock_symbol] - i.cantitate

    invest_list = []
    for i in stock_list:
        if stock_list[i] != 0:
            invest_list.append(i)
    if result is None:
        return jsonify({"message": "Userul nu are investitii pentru acest stock"}), 404
    else:

        return jsonify({"message": "Userul are investitii pentru acest stock", "stock_list": invest_list}), 200


@investBP.route('/get-invest-summary-by-user', methods=['POST'])
def get_invest_summary():
    user = request.json['identifier']
    stock_dict = get_user_sumarryDAO(user)
    return jsonify({"message": 'ok', 'dict': stock_dict})


@investBP.route('/get-users-invest', methods=['GET'])
def get_users_invest():
    return get_usersDAO(), 200


@investBP.route('/get-history-stock-user', methods=['POST'])
def get_history_stock_user():
    user = request.json['identifier']
    stock_symbol = request.json['stock_symbol']
    x = Invest.get_stock_invest_by_user(user, stock_symbol)
    stock_invest = []
    for i in x:
        stock_invest.append(
            {"stock_symbol": i.stock_symbol, "price": i.price, "cantitate": i.cantitate, "action_type": i.action_type,
             "date_of_buy": i.date_of_buy})
    stock_invest = sorted(stock_invest, key=lambda i: i['date_of_buy'])
    return jsonify({"message": stock_invest}), 200


@investBP.route('/get-all-history-user', methods=['POST'])
def get_all_history_user():
    user = request.json['identifier']
    x = Invest.get_history_invest_by_user(user)
    stock_invest = []
    for i in x:
        stock_invest.append(
            {"stock_symbol": i.stock_symbol, "price": i.price, "cantitate": i.cantitate, "action_type": i.action_type,
             "date_of_buy": i.date_of_buy})
    stock_invest = sorted(stock_invest, key=lambda i: i['date_of_buy'])
    return jsonify({"message": stock_invest}), 200


@investBP.route('/get-value-of-user-account', methods=['GET'])
def get_value_of_user_account():
    user = request.json['identifier']
    x = Invest.get_history_invest_by_user(user)
    price_invest = {}
    for i in x:
        if i.stock_symbol not in price_invest:
            price_invest[i.stock_symbol] = {}
            price_invest[i.stock_symbol]['price'] = i.price
            if i.action_type == 'BUY':
                price_invest[i.stock_symbol]['quantity'] = i.cantitate
            else:
                price_invest[i.stock_symbol]['quantity'] = -i.cantitate
        else:
            if i.action_type == 'BUY':
                price_invest[i.stock_symbol]['price'] = (price_invest[i.stock_symbol]['price'] *
                                                         price_invest[i.stock_symbol][
                                                             'quantity'] + i.price * i.cantitate) / (
                                                                i.cantitate + price_invest[i.stock_symbol]['quantity'])
                price_invest[i.stock_symbol]['quantity'] = price_invest[i.stock_symbol]['quantity'] + i.cantitate
            else:
                price_invest[i.stock_symbol]['quantity'] = price_invest[i.stock_symbol]['quantity'] - i.cantitate
    total_value = 0
    print(price_invest)
    for i in price_invest:
        if price_invest[i]['quantity'] > 0:
            total_value = total_value + price_invest[i]['quantity'] * price_invest[i]['price']
    return jsonify({"message": total_value}), 200


@investBP.route('/get-detailed-stock-invest', methods=['GET'])
def get_detailed_stock_invest():
    user = request.json['identifier']
    x = Invest.get_history_invest_by_user(user)
    price_invest = {}
    for i in x:
        if i.stock_symbol not in price_invest:
            price_invest[i.stock_symbol] = {}
            price_invest[i.stock_symbol]['price'] = i.price
            if i.action_type == 'BUY':
                price_invest[i.stock_symbol]['cantitate'] = i.cantitate
            else:
                price_invest[i.stock_symbol]['cantitate'] = -i.cantitate
        else:

            if i.action_type == 'BUY':
                price_invest[i.stock_symbol]['price'] = (price_invest[i.stock_symbol]['price'] *
                                                         price_invest[i.stock_symbol][
                                                             'cantitate'] + i.price * i.cantitate) / (
                                                                i.cantitate + price_invest[i.stock_symbol]['cantitate'])
                price_invest[i.stock_symbol]['cantitate'] = price_invest[i.stock_symbol]['cantitate'] + i.cantitate
            else:
                price_invest[i.stock_symbol]['cantitate'] = price_invest[i.stock_symbol]['cantitate'] - i.cantitate
    for i in list(price_invest):
        if price_invest[i]['cantitate'] <= 0:
            price_invest.pop(i)
    return price_invest, 200


@investBP.route('/autobuy', methods=['POST'])
def autobuy():
    json_body = request.json
    user = json_body['user']
    stock_symbol = json_body['stock_symbol']
    cantitate = float(json_body['cantitate'])
    price = float(json_body['price'])
    try:
        buy_autoinvestDAO(user, stock_symbol, cantitate, price)
        return jsonify({"message": "AutoBuy Completed"}), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "AutoBuy Fail"}), 400


@investBP.route('/autosell', methods=['POST'])
def autosell():
    json_body = request.json
    user = json_body['user']
    stock_symbol = json_body['stock_symbol']
    cantitate = float(json_body['cantitate'])
    price = float(json_body['price'])
    try:
        sell_autoinvestDAO(user, stock_symbol, cantitate, price)
        return jsonify({"message": "AutoSell Completed"}), 200
    except Exception as e:
        return jsonify({"message": "AutoSell Fail"}), 400


@investBP.route('/remove-autoinvest', methods=['DELETE'])
def remove_autoinvest():
    json_body = request.json
    id_invest = json_body['id_invest']
    try:
        delete_investDAO(id_invest)
        return jsonify({"message": "AutoInvest Removed"}), 200
    except Exception as e:
        return jsonify({"message": "AutoInvest Fail Removed"}), 400


@investBP.route('/get-autoinvest-stock-user', methods=['POST'])
def get_autoinvest_stock_user():
    user = request.json['identifier']
    stock_symbol = request.json['stock_symbol']
    x = AutoInvest.get_stock_invest_by_user(user, stock_symbol)
    stock_invest = []
    for i in x:
        stock_invest.append(
            {"id": i.id, "stock_symbol": i.stock_symbol, "price": i.price, "cantitate": i.cantitate,
             "action_type": i.action_type,
             "date_of_autobuy": i.date_of_autobuy})
    stock_invest = sorted(stock_invest, key=lambda i: i['date_of_autobuy'])
    return jsonify({"message": stock_invest}), 200


@investBP.route('/get-all-autoinvests')
def get_all_autoinvests():
    all_invest = AutoInvest.get_all()
    all_invest_list = {}
    for i in all_invest:
        if i.stock_symbol not in all_invest_list:
            all_invest_list[i.stock_symbol] = []
            all_invest_list[i.stock_symbol].append(
                {"id": i.id, "user": i.user, "action_type": i.action_type, "cantitate": i.cantitate, "price": i.price})
        else:
            all_invest_list[i.stock_symbol].append(
                {"id": i.id, "user": i.user, "action_type": i.action_type, "cantitate": i.cantitate, "price": i.price})
    return jsonify({"message": all_invest_list}), 200
