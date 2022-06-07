from flask import Blueprint, jsonify, request
from flask_json_schema import JsonValidationError
from sqlalchemy.exc import DatabaseError

from app.DAO.investDAO import buy_investDAO

investBP = Blueprint('investBlueprint', __name__)


@investBP.errorhandler(JsonValidationError)
def validator_error(e):
    return jsonify({'error': e.message, 'errors': [validation_error.message for validation_error in e.errors]}), 400


@investBP.errorhandler(DatabaseError)
def database_error():
    return jsonify({'error': 'Database error'}), 500


@investBP.route('/buy-invested', methods=['POST'])
def buy_invested():
    user = request.json['user']
    stock_symbol = request.json['stock_symbol']
    cantitate = request.json['cantitate']
    price = request.json['price']
    try:
        buy_investDAO(user, stock_symbol, cantitate, price)
        return jsonify({'message': 'Buy completed'}), 200
    except Exception:
        return jsonify({'message': 'Buy fail'}), 400


@investBP.route('/sell-invested', methods=['POST'])
def sell_invested():
    pass
