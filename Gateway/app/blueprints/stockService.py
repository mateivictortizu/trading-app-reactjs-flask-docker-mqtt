from flask import Blueprint, request

from app.RabbitMQProcessor.StockRabbitMQProcessor import get_list_stock_price_processor, add_stock_processor, \
    get_stock_info_processor, get_stock_price_processor, update_price_processor, update_stock_processor, \
    get_all_stocks_processor
from app.blueprints import add_session, add_stock_client, get_stock_info_client, get_stock_price_client, \
    get_list_stock_price_client, update_price_client, update_stock_client, get_all_stocks_client

stock = Blueprint('stock', __name__)
stock.before_request(add_session)


@stock.route('/add-stock', methods=['POST'])
def add_stock():
    return add_stock_processor(add_stock_client, request.json)


@stock.route('/get-stock-info/<stock_symbol>', methods=['GET'])
def get_stock_info(stock_symbol):
    return get_stock_info_processor(get_stock_info_client, stock_symbol)


@stock.route('/get-stock-price/<stock_symbol>', methods=['GET'])
def get_stock_price(stock_symbol):
    return get_stock_price_processor(get_stock_price_client, stock_symbol)


@stock.route('/get-list-stock-price', methods=['POST'])
def get_list_stock_price():
    return get_list_stock_price_processor(get_list_stock_price_client, request.json)


@stock.route('/update-price', methods=['POST'])
def update_price():
    return update_price_processor(update_price_client, request.json)


@stock.route('/update-stock', methods=['POST'])
def update_stock():
    return update_stock_processor(update_stock_client, request.json)


@stock.route('/get-all-stocks', methods=['GET'])
def get_all_stocks():
    return get_all_stocks_processor(get_all_stocks_client)
