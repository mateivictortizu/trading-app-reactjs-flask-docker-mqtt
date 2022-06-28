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
    print(json_body)
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
    price = 0
    for i in x:
        if i.action_type == 'BUY':
            price = price + i.price * i.cantitate
        else:
            price = price - i.price * i.cantitate
    return jsonify({"message": price}), 200


@investBP.route('/get-detailed-stock-invest', methods=['GET'])
def get_detailed_stock_invest():
    user = request.json['identifier']
    x = Invest.get_history_invest_by_user(user)
    stock_dict = {}
    total_cty = {}
    for i in x:
        if i.action_type == 'BUY':
            if i.stock_symbol in stock_dict and "cantitate" in stock_dict[i.stock_symbol] and \
                    "price" in stock_dict[i.stock_symbol]:
                stock_dict[i.stock_symbol] = {"cantitate": stock_dict[i.stock_symbol]["cantitate"] + i.cantitate,
                                              "price": stock_dict[i.stock_symbol]["price"] + i.price * i.cantitate}
                total_cty[i.stock_symbol] = total_cty[i.stock_symbol] + i.cantitate
            else:
                stock_dict[i.stock_symbol] = {"cantitate": i.cantitate, "price": i.price * i.cantitate}
                total_cty[i.stock_symbol] = i.cantitate
        else:
            if i.stock_symbol in stock_dict and "cantitate" in stock_dict[i.stock_symbol] and \
                    "price" in stock_dict[i.stock_symbol]:
                stock_dict[i.stock_symbol] = {"cantitate": stock_dict[i.stock_symbol]["cantitate"] - i.cantitate,
                                              "price": stock_dict[i.stock_symbol]["price"]}

    list_to_pop = []
    for i in stock_dict:
        if stock_dict[i]['cantitate'] == 0:
            list_to_pop.append(i)
        else:
            stock_dict[i]['price'] = stock_dict[i]['price'] / total_cty[i]
    for i in list_to_pop:
        stock_dict.pop(i)
    print(stock_dict)
    return stock_dict, 200


@investBP.route('/autobuy', methods=['POST'])
def autobuy():
    json_body = request.json
    print(json_body)
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
