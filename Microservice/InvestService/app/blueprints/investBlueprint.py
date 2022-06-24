from flask import Blueprint, jsonify, request
from flask_json_schema import JsonValidationError
from sqlalchemy.exc import DatabaseError

from app.DAO.investDAO import buy_investDAO, sell_investDAO, get_stock_invest_by_userDAO, get_invest_by_userDAO, \
    get_usersDAO, get_user_sumarryDAO
from app.database.models import Invest

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
    cantitate = json_body['cantitate']
    price = json_body['price']
    try:
        buy_investDAO(user, stock_symbol, cantitate, price)
        return jsonify({"message": "Buy Completed"}), 200
    except Exception as e:
        return jsonify({"message": "Buy Fail"}), 400


@investBP.route('/sell', methods=['POST'])
def sell():
    json_body = request.json
    user = json_body['user']
    stock_symbol = json_body['stock_symbol']
    cantitate = json_body['cantitate']
    price = json_body['price']
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
    stock_list = []
    for i in result:
        stock_list.append(i.stock_symbol)
    stock_list = list(dict.fromkeys(stock_list))
    if result is None:
        return jsonify({"message": "Userul nu are investitii pentru acest stock"}), 404
    else:

        return jsonify({"message": "Userul are investitii pentru acest stock", "stock_list": stock_list}), 200


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
    print(stock_invest)
    return jsonify({"message": stock_invest}), 200
