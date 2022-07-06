import threading

from flask import Blueprint, jsonify, request
from flask_json_schema import JsonValidationError
from sqlalchemy.exc import DatabaseError

from app import executor
from app.DAO.stockDAO import addStockDAO, updateStockDAO, updatePriceDAO, getStockInfoDAO, getStockPriceDAO, \
    get_all_stocksDAO, addToWatchlistDAO, removeFromWatchlistDAO, join_watchlist

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
    addStockDAO(symbol_stock)
    #executor.submit(addStockDAO, symbol_stock)
    return jsonify({'message': 'Stock was added to db'}), 200


@stockBP.route('/get-stock-info/<stock>', methods=['GET'])
def get_stock_info(stock):
    stock_info = getStockInfoDAO(stock)
    return stock_info.to_json(), 200


@stockBP.route('/get-stock-price/<stock>', methods=['GET'])
def get_stock_price(stock):
    stock_price = getStockPriceDAO(stock)
    return stock_price.to_json(), 200


@stockBP.route('/get-list-stock-price', methods=['POST'])
def get_list_stock_price():
    stock_symbol_list = request.json['stock_list']
    stock_list = []
    for i in stock_symbol_list:
        new_stock = getStockPriceDAO(i)
        if new_stock is not None:
            stock_list.append(new_stock.to_json())
    return jsonify({'message': stock_list}), 200


@stockBP.route('/update-price', methods=['POST'])
def update_price():
    try:
        t = threading.Thread(target=updatePriceDAO)
        t.start()
        return jsonify({'message': 'Prices updated'}), 200
    except Exception as e:
        print(e)
        return jsonify({'error': 'Prices not updated'}), 400


@stockBP.route('/update-stock', methods=['POST'])
def update_stock():
    try:
        updateStockDAO()
        return jsonify({'message': 'Stocks updated'}), 200
    except Exception as e:
        print(e)
        return jsonify({'error': 'Stocks not updated'}), 400


@stockBP.route('/get-all-stocks', methods=['GET'])
def get_all_stocks():
    stocks_list = []
    stocks = get_all_stocksDAO()
    if stocks is not None:
        for i in stocks:
            stocks_list.append(i.to_json())
    return jsonify({'message': stocks_list}), 200


@stockBP.route('/add-watchlist', methods=['POST'])
def add_watchlist():
    try:
        addToWatchlistDAO(user=request.json['identifier'], stock_symbol=request.json['stock_symbol'])
        return jsonify({'message': 'ok'}), 200
    except Exception as e:
        return jsonify({'error': 'Remove fail'}), 400


@stockBP.route('/remove-watchlist', methods=['POST'])
def remove_watchlist():
    try:
        removeFromWatchlistDAO(user=request.json['identifier'], stock_symbol=request.json['stock_symbol'])
        return jsonify({'message': 'ok'}), 200
    except Exception as e:
        return jsonify({'error': 'Remove fail'}), 400


@stockBP.route('/get-all-stocks-by-user-watchlist', methods=['GET'])
def get_all_stocks_by_watchlist():
    result = join_watchlist(request.json['user'])
    return jsonify({'list': result}), 200


