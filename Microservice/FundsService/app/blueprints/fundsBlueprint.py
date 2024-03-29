from flask import Blueprint, jsonify, request
from flask_json_schema import JsonValidationError
from sqlalchemy.exc import DatabaseError

from app.DAO.fundsDAO import addFundsDAO, withdrawFundsDAO, get_fundsDAO, withdrawFundsAfterBuyDAO, addFundsAfterSellDAO

fundsBP = Blueprint('fundsBlueprint', __name__)


@fundsBP.errorhandler(JsonValidationError)
def validator_error(e):
    return jsonify({'error': e.message, 'errors': [validation_error.message for validation_error in e.errors]}), 400


@fundsBP.errorhandler(DatabaseError)
def database_error():
    return jsonify({'error': 'Database error'}), 500


@fundsBP.route('/add-money', methods=['POST'])
def add_money():
    try:
        user = request.json['user']
        value = request.json['value']
        addFundsDAO(user, value)
        return jsonify({"message": "Funds added"}), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "Funds did not added"}), 400


@fundsBP.route('/withdraw-money', methods=['POST'])
def withdraw_money():
    try:
        user = request.json['user']
        value = request.json['value']
        result_code = withdrawFundsDAO(user, value)
        if result_code == 1:
            return jsonify({'message': 'Funds withdraw'}), 200
        else:
            return jsonify({'message': 'Funds not withdraw'}), 401
    except Exception as e:
        print(e)
        return jsonify({'message': 'Funds did not added'}), 500


@fundsBP.route('/get-funds/<user>')
def get_funds(user):
    try:
        value = get_fundsDAO(user)
        if value is False:
            return jsonify({'message': 'User did not exists'}), 400
        else:
            return jsonify({'message': 'Works', 'value': value}), 200
    except Exception as e:
        return jsonify({'message': 'Internal error'}), 500


@fundsBP.route('/add-money-after-sell', methods=['POST'])
def add_money_after_sell():
    try:
        user = request.json['user']
        value = request.json['value']
        addFundsAfterSellDAO(user, value)
        return jsonify({"message": "Funds modified after sell"}), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "Funds did not modified after sell"}), 400


@fundsBP.route('/withdraw-money-after-buy', methods=['POST'])
def withdraw_money_after_buy():
    try:
        user = request.json['user']
        value = request.json['value']
        result_code = withdrawFundsAfterBuyDAO(user, value)
        if result_code == 1:
            return jsonify({'message': 'Funds modified after buy'}), 200
        else:
            return jsonify({'message': 'Funds not modified after buy'}), 401
    except Exception as e:
        print(e)
        return jsonify({'message': 'Funds did not modified after buy'}), 500
