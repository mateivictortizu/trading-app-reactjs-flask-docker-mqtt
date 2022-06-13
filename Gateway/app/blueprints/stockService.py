import json

from flask import Blueprint, request, jsonify

from app.RabbitMQClients.StocksRabbitMQ import AddStockClient, GetStockInfoClient, GetStockPriceClient, \
    GetListStockPriceClient, UpdatePriceClient, UpdateStockClient, GetAllStocksClient

stock = Blueprint('stock', __name__)

add_stock_client = None
get_stock_info_client = None
get_stock_price_client = None
get_list_stock_price_client = None
update_price_client = None
update_stock_client = None
get_all_stocks_client = None


@stock.route('/add-stock', methods=['POST'])
def add_stock():
    global add_stock_client
    if add_stock_client is None:
        add_stock_client = AddStockClient()
    try:
        response = json.loads(add_stock_client.call(request.json))
        return response, response['code']
    except Exception:
        try:
            add_stock_client = AddStockClient()
            response = json.loads(add_stock_client.call(request.json))
            return response, response['code']
        except Exception:
            return jsonify({'error': 'Add stock server error', 'code': 500}), 500


@stock.route('/get-stock-info/<stock_symbol>', methods=['GET'])
def get_stock_info(stock_symbol):
    global get_stock_info_client
    if get_stock_info_client is None:
        get_stock_info_client = GetStockInfoClient()
    try:
        response = json.loads(get_stock_info_client.call({'stock_symbol': stock_symbol}))
        return response, response['code']
    except Exception:
        try:
            get_stock_info_client = GetStockInfoClient()
            response = json.loads(get_stock_info_client.call({'stock_symbol': stock_symbol}))
            return response, response['code']
        except Exception:
            return jsonify({'error': 'Get stock info server error', 'code': 500}), 500


@stock.route('/get-stock-price/<stock_symbol>', methods=['GET'])
def get_stock_price(stock_symbol):
    global get_stock_price_client
    if get_stock_price_client is None:
        get_stock_price_client = GetStockPriceClient()
    try:
        response = json.loads(get_stock_price_client.call({'stock_symbol': stock_symbol}))
        return response, response['code']
    except Exception:
        try:
            get_stock_price_client = GetStockPriceClient()
            response = json.loads(get_stock_price_client.call({'stock_symbol': stock_symbol}))
            return response, response['code']
        except Exception:
            return jsonify({'error': 'Get stock price server error', 'code': 500}), 500


@stock.route('/get-list-stock-price', methods=['POST'])
def get_list_stock_price():
    global get_list_stock_price_client
    if get_list_stock_price_client is None:
        get_list_stock_price_client = GetListStockPriceClient()
    try:
        response = json.loads(get_list_stock_price_client.call(request.json))
        return response, response['code']
    except Exception:
        try:
            get_list_stock_price_client = GetListStockPriceClient()
            response = json.loads(get_list_stock_price_client.call(request.json))
            return response, response['code']
        except Exception:
            return jsonify({'error': 'Get list stock price server error', 'code': 500}), 500


@stock.route('/update-price', methods=['POST'])
def update_price():
    global update_price_client
    if update_price_client is None:
        update_price_client = UpdatePriceClient()
    try:
        response = json.loads(update_price_client.call(request.json))
        return response, response['code']
    except Exception:
        try:
            update_price_client = UpdatePriceClient()
            response = json.loads(update_price_client.call(request.json))
            return response, response['code']
        except Exception:
            return jsonify({'error': 'Update price server error', 'code': 500}), 500


@stock.route('/update-stock', methods=['POST'])
def update_stock():
    global update_stock_client
    if update_stock_client is None:
        update_stock_client = UpdateStockClient()
    try:
        response = json.loads(update_stock_client.call(request.json))
        return response, response['code']
    except Exception:
        try:
            update_stock_client = UpdateStockClient()
            response = json.loads(update_stock_client.call(request.json))
            return response, response['code']
        except Exception:
            return jsonify({'error': 'Update stock server error', 'code': 500}), 500


@stock.route('/get-all-stocks', methods=['GET'])
def get_all_stocks():
    global get_all_stocks_client
    if get_all_stocks_client is None:
        get_all_stocks_client = GetAllStocksClient()
    try:
        response = json.loads(get_all_stocks_client.call(None))
        return response, response['code']
    except Exception:
        try:
            get_all_stocks_client = GetAllStocksClient()
            response = json.loads(get_all_stocks_client.call(None))
            return response, response['code']
        except Exception:
            return jsonify({'error': 'Get all stocks server error', 'code': 500}), 500
