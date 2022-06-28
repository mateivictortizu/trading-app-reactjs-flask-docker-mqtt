from flask import Blueprint, request, session

from app import socketio
from app.RabbitMQProcessor.StockRabbitMQProcessor import get_list_stock_price_processor, add_stock_processor, \
    get_stock_info_processor, get_stock_price_processor, update_price_processor, update_stock_processor, \
    get_all_stocks_processor, get_all_stocks_by_user_processor, remove_watchlist_processor, add_watchlist_processor
from app.blueprints import add_stock_client, get_stock_info_client, get_stock_price_client, \
    get_list_stock_price_client, update_price_client, update_stock_client, get_all_stocks_client, \
    before_request_function, get_all_stocks_by_user_client, users_connections, add_watchlist_client, \
    remove_watchlist_client

stock = Blueprint('stock', __name__)


@stock.route('/add-stock', methods=['POST'])
def add_stock():
    before_checking_result = before_request_function(request)
    if before_checking_result[1] == 403:
        return before_checking_result
    return add_stock_processor(add_stock_client, request.json)


@stock.route('/get-stock-info/<stock_symbol>', methods=['GET'])
def get_stock_info(stock_symbol):
    before_checking_result = before_request_function(request)
    if before_checking_result[1] == 403:
        return before_checking_result
    return get_stock_info_processor(get_stock_info_client, stock_symbol)


@stock.route('/get-stock-price/<stock_symbol>', methods=['GET'])
def get_stock_price(stock_symbol):
    before_checking_result = before_request_function(request)
    if before_checking_result[1] == 403:
        return before_checking_result
    return get_stock_price_processor(get_stock_price_client, stock_symbol)


@stock.route('/get-list-stock-price', methods=['POST'])
def get_list_stock_price():
    before_checking_result = before_request_function(request)
    if before_checking_result[1] == 403:
        return before_checking_result
    return get_list_stock_price_processor(get_list_stock_price_client, request.json)


@stock.route('/update-price', methods=['POST'])
def update_price():
    before_checking_result = before_request_function(request)
    if before_checking_result[1] == 403:
        return before_checking_result
    return update_price_processor(update_price_client, request.json)


@stock.route('/update-stock', methods=['POST'])
def update_stock():
    before_checking_result = before_request_function(request)
    if before_checking_result[1] == 403:
        return before_checking_result
    return update_stock_processor(update_stock_client, request.json)


@stock.route('/get-all-stocks', methods=['GET'])
def get_all_stocks():
    before_checking_result = before_request_function(request)
    if before_checking_result[1] == 403:
        return before_checking_result
    return get_all_stocks_processor(get_all_stocks_client)


@stock.route('/get-all-stocks-by-user-watchlist', methods=['GET'])
def get_all_stocks_by_user():
    before_checking_result = before_request_function(request)
    if before_checking_result[1] == 403:
        return before_checking_result
    request_temp = dict()
    request_temp['identifier'] = users_connections[session['user_id']]['user']
    return get_all_stocks_by_user_processor(get_all_stocks_by_user_client, request_temp)


@stock.route('/add-watchlist', methods=['POST'])
def add_watchlist():
    before_checking_result = before_request_function(request)
    if before_checking_result[1] == 403:
        return before_checking_result
    request_temp = dict()
    request_temp['stock_symbol'] = request.json['stock_symbol']
    request_temp['identifier'] = users_connections[session['user_id']]['user']
    add_response = add_watchlist_processor(add_watchlist_client, request_temp)
    get_all_stock = get_all_stocks_by_user_processor(get_all_stocks_by_user_client,
                                                     {'user': users_connections[session['user_id']]['user']})
    socketio.emit('get_all_stocks', {'value': get_all_stock[0]['list']},
                  room=users_connections[session['user_id']]['socket'])

    watchlist_list = []
    for i in get_all_stock[0]['list']:
        if i['watchlist'] is True:
            watchlist_list.append(i['stock_symbol'])
    json_body = {"stock_list": watchlist_list}
    stock_wishlist = get_list_stock_price_processor(get_list_stock_price_client, json_body=json_body)
    socketio.emit('stock_wishlist', stock_wishlist[0], room=users_connections[session['user_id']]['socket'])
    return add_response


@stock.route('/remove-watchlist', methods=['POST'])
def remove_watchlist():
    before_checking_result = before_request_function(request)
    if before_checking_result[1] == 403:
        return before_checking_result
    request_temp = dict()
    request_temp['stock_symbol'] = request.json['stock_symbol']
    request_temp['identifier'] = users_connections[session['user_id']]['user']
    remove_response = remove_watchlist_processor(remove_watchlist_client, request_temp)
    get_all_stock = get_all_stocks_by_user_processor(get_all_stocks_by_user_client,
                                                     {'user': users_connections[session['user_id']]['user']})
    socketio.emit('get_all_stocks', {'value': get_all_stock[0]['list']},
                  room=users_connections[session['user_id']]['socket'])

    watchlist_list = []
    for i in get_all_stock[0]['list']:
        if i['watchlist'] is True:
            watchlist_list.append(i['stock_symbol'])
    json_body = {"stock_list": watchlist_list}
    stock_wishlist = get_list_stock_price_processor(get_list_stock_price_client, json_body=json_body)
    socketio.emit('stock_wishlist', stock_wishlist[0], room=users_connections[session['user_id']]['socket'])

    return remove_response
