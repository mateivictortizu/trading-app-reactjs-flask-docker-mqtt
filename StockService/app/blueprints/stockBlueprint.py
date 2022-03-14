from flask import Blueprint, jsonify, request
from flask_json_schema import JsonValidationError
from sqlalchemy.exc import DatabaseError

from app import executor
from app.DAO.stockDAO import addStockDAO, updateStockDAO, updatePriceDAO

stockBP = Blueprint('stockBlueprint', __name__)


@stockBP.errorhandler(ConnectionError)
def connection_error(e):
    return jsonify({'error': e.message, 'errors': [validation_error.message for validation_error in e.errors]}), 400


@stockBP.errorhandler(JsonValidationError)
def validator_error(e):
    return jsonify({'error': e.message, 'errors': [validation_error.message for validation_error in e.errors]}), 400


@stockBP.errorhandler(DatabaseError)
def database_error():
    return jsonify({'error': 'Database error'}), 500


@stockBP.errorhandler(Exception)
def general_exception_error(e):
    return jsonify({'error': e.message, 'errors': [validation_error.message for validation_error in e.errors]}), 400


@stockBP.route('/add-stock', methods=['POST'])
def add_stock():
    symbol_stock = request.json['stock_symbol']
    executor.submit(addStockDAO, symbol_stock)
    return jsonify({'message': 'Stock was added to db'}), 200


@stockBP.route('/update-price', methods=['POST'])
def update_price():
    try:
        updatePriceDAO()
        return jsonify({'message': 'Prices updated'}), 200
    except Exception:
        return jsonify({'error': 'Prices not updated'}), 400


@stockBP.route('/update-stock', methods=['POST'])
def update_stock():
    try:
        updateStockDAO()
        return jsonify({'message': 'Stocks updated'}), 200
    except Exception:
        return jsonify({'error': 'Stocks not updated'}), 400
