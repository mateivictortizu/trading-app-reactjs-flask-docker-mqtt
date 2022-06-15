import json

from flask import Blueprint, request, jsonify

from app import socketio
from app.RabbitMQClients.StocksRabbitMQ import GetStockInfoClient, GetStockPriceClient, \
    UpdatePriceClient, UpdateStockClient, GetAllStocksClient
from app.RabbitMQProcessor.StockRabbitMQProcessor import get_list_stock_price_processor, add_stock_processor, \
    get_stock_info_processor, get_stock_price_processor, update_price_processor, update_stock_processor, \
    get_all_stocks_processor

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
    return add_stock_processor(add_stock_client, request.json)


@stock.route('/get-stock-info/<stock_symbol>', methods=['GET'])
def get_stock_info(stock_symbol):
    global get_stock_info_client
    return get_stock_info_processor(get_stock_info_client, stock_symbol)


@stock.route('/get-stock-price/<stock_symbol>', methods=['GET'])
def get_stock_price(stock_symbol):
    global get_stock_price_client
    return get_stock_price_processor(get_stock_price_client, stock_symbol)


@stock.route('/get-list-stock-price', methods=['POST'])
def get_list_stock_price():
    global get_list_stock_price_client
    return get_list_stock_price_processor(get_list_stock_price_client, request.json)


@stock.route('/update-price', methods=['POST'])
def update_price():
    global update_price_client
    return update_price_processor(update_price_client, request.json)


@stock.route('/update-stock', methods=['POST'])
def update_stock():
    global update_stock_client
    return update_stock_processor(update_stock_client, request.json)


@stock.route('/get-all-stocks', methods=['GET'])
def get_all_stocks():
    global get_all_stocks_client
    return get_all_stocks_processor(get_all_stocks_client)
