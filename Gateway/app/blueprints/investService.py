from flask import Blueprint, request, jsonify, session

from app import socketio
from app.RabbitMQProcessor.FundsRabbitMQProcessor import get_funds_processor, add_money_after_sell_processor, \
    withdraw_money_after_buy_processor
from app.RabbitMQProcessor.InvestRabbitMQProcessor import buy_processor, sell_processor, \
    get_stock_invest_by_user_processor, get_invest_by_user_processor, get_history_stock_user_processor, \
    get_all_history_user_processor, get_value_of_account_processor, get_user_detailed_invests_processor
from app.RabbitMQProcessor.StockRabbitMQProcessor import get_list_stock_price_processor
from app.blueprints import get_funds_client, buy, sell, get_stock, get_invest, add_money_after_sell_client, \
    withdraw_money_after_buy_client, before_request_function, users_connections, get_list_stock_price_client, \
    get_history_stock_user_client, get_all_history_user_client, get_value_of_account_client, \
    get_user_detailed_invests_client

invest = Blueprint('invest', __name__)


@invest.route('/buy', methods=['POST'])
def buy_invested():
    before_checking_result = before_request_function(request)
    if before_checking_result[1] == 403:
        return before_checking_result
    value_initial = get_funds_processor(get_funds_client, {'user': users_connections[session['user_id']]['user']})
    if float(value_initial[0]['value']) >= float(request.json['cantitate']) * float(request.json['price']):
        result = withdraw_money_after_buy_processor(withdraw_money_after_buy_client,
                                                    {'user': users_connections[session['user_id']]['user'],
                                                     'value': float(request.json['cantitate']) * float(
                                                         request.json['price'])})
        if result[1] == 200:
            socketio.emit('get_funds', {
                'value': float(value_initial[0]['value']) - float(request.json['cantitate']) * float(
                    request.json['price'])})
        request_body = dict()
        request_body['stock_symbol'] = request.json['stock_symbol']
        request_body['cantitate'] = request.json['cantitate']
        request_body['price'] = request.json['price']
        request_body['user'] = users_connections[session['user_id']]['user']
        buy_result = buy_processor(buy, request_body)
        get_value_of_stock = get_stock_invest_by_user_processor(get_stock,
                                                                {'identifier': users_connections[session['user_id']][
                                                                    'user'],
                                                                 'stock_symbol': request.json['stock_symbol']})
        if get_value_of_stock == 200:
            socketio.emit('get_investment', {
                'cantitate': float(get_value_of_stock[0]['cantitate']), 'medie': float(get_value_of_stock[0]['medie'])})
        stock_invest = get_invest_by_user_processor(get_invest,
                                                    json_body={
                                                        'identifier': users_connections[session['user_id']]['user']})
        json_body = {"stock_list": stock_invest[0]['stock_list']}
        stock_invest_list = get_list_stock_price_processor(get_list_stock_price_client, json_body=json_body)
        socketio.emit('stock_invest', stock_invest_list[0])
        value_of_account = get_value_of_account_processor(get_value_of_account_client,
                                                          json_body={
                                                              'identifier': users_connections[session['user_id']][
                                                                  'user']})
        socketio.emit('get_invest_value_of_account', value_of_account[0]['message'])
        user_detailed_invests = get_user_detailed_invests_processor(get_user_detailed_invests_client,
                                                                    json_body={'identifier': 'matteovkt@gmail.com'})
        socketio.emit('detailed_user_invests', user_detailed_invests[0])
        return buy_result
    else:
        return jsonify({"message": "Not enough funds"}), 400


@invest.route('/sell', methods=['POST'])
def sell_invested():
    before_checking_result = before_request_function(request)
    if before_checking_result[1] == 403:
        return before_checking_result
    value_initial = get_funds_processor(get_funds_client, {'user': users_connections[session['user_id']]['user']})
    result = add_money_after_sell_processor(add_money_after_sell_client,
                                            {'user': users_connections[session['user_id']]['user'], 'value': float(
                                                request.json['cantitate']) * float(request.json['price'])})
    if result[1] == 200:
        socketio.emit('get_funds', {
            'value': float(value_initial[0]['value']) + float(request.json['cantitate']) * float(
                request.json['price'])})
        request_body = dict()
        request_body['stock_symbol'] = request.json['stock_symbol']
        request_body['cantitate'] = request.json['cantitate']
        request_body['price'] = request.json['price']
        request_body['user'] = users_connections[session['user_id']]['user']
        sell_result = sell_processor(sell, request_body)
        get_value_of_stock = get_stock_invest_by_user_processor(get_stock,
                                                                {'identifier': users_connections[session['user_id']][
                                                                    'user'],
                                                                 'stock_symbol': request.json['stock_symbol']})
        if get_value_of_stock[1] == 200:
            socketio.emit('get_investment', {
                'cantitate': float(get_value_of_stock[0]['cantitate']), 'medie': float(get_value_of_stock[0]['medie'])})
            socketio.emit("invest_on", 1)
        else:
            socketio.emit('get_investment', {'cantitate': 0, 'medie': 0})
            socketio.emit("invest_on", 0)
        stock_invest = get_invest_by_user_processor(get_invest, json_body={
            'identifier': users_connections[session['user_id']]['user']})
        json_body = {"stock_list": stock_invest[0]['stock_list']}
        stock_invest_list = get_list_stock_price_processor(get_list_stock_price_client, json_body=json_body)
        socketio.emit('stock_invest', stock_invest_list[0])
        value_of_account = get_value_of_account_processor(get_value_of_account_client,
                                                          json_body={
                                                              'identifier': users_connections[session['user_id']][
                                                                  'user']})
        socketio.emit('get_invest_value_of_account', value_of_account[0]['message'])
        user_detailed_invests = get_user_detailed_invests_processor(get_user_detailed_invests_client,
                                                                    json_body={'identifier': 'matteovkt@gmail.com'})
        socketio.emit('detailed_user_invests', user_detailed_invests[0])
        return sell_result
    else:
        return jsonify({'message': 'Add money error'}), 400


@invest.route('/get-stock-invest-by-user', methods=['POST'])
def get_stock_invest_by_user():
    before_checking_result = before_request_function(request)
    if before_checking_result[1] == 403:
        return before_checking_result
    request_temp = dict()
    request_temp['stock_symbol'] = request.json['stock_symbol']
    request_temp['identifier'] = users_connections[session['user_id']]['user']
    value = get_stock_invest_by_user_processor(get_stock, request_temp)
    if value[1] == 200:
        socketio.emit("invest_on", 1)
        socketio.emit("statisticData", [value[0]['medie'], value[0]['cantitate']])
    else:
        socketio.emit("invest_on", 0)
        socketio.emit("statisticData", [0, 0])
    return value


@invest.route('/get-invest-by-user', methods=['POST'])
def get_invest_by_user():
    before_checking_result = before_request_function(request)
    if before_checking_result[1] == 403:
        return before_checking_result
    return get_invest_by_user_processor(get_invest, request.json)


@invest.route('/get-history-stock-user', methods=['POST'])
def get_history_stock_user():
    before_checking_result = before_request_function(request)
    if before_checking_result[1] == 403:
        return before_checking_result
    request_temp = dict()
    request_temp['stock_symbol'] = request.json['stock_symbol']
    request_temp['identifier'] = users_connections[session['user_id']]['user']
    return get_history_stock_user_processor(get_history_stock_user_client, request_temp)


@invest.route('/get-all-history-user', methods=['POST'])
def get_history_user():
    before_checking_result = before_request_function(request)
    if before_checking_result[1] == 403:
        return before_checking_result
    request_temp = dict()
    request_temp['identifier'] = users_connections[session['user_id']]['user']
    return get_all_history_user_processor(get_all_history_user_client, request_temp)


@invest.route('/get-value-of-user-account', methods=['GET'])
def get_value_of_user_account():
    before_checking_result = before_request_function(request)
    if before_checking_result[1] == 403:
        return before_checking_result
    request_temp = dict()
    request_temp['identifier'] = users_connections[session['user_id']]['user']
    return get_value_of_account_processor(get_value_of_account_client, request_temp)


@invest.route('/get-user-detailed-invests', methods=['GET'])
def get_user_detailed_invests():
    before_checking_result = before_request_function(request)
    if before_checking_result[1] == 403:
        return before_checking_result
    request_temp = dict()
    request_temp['identifier'] = users_connections[session['user_id']]['user']
    return get_user_detailed_invests_processor(get_user_detailed_invests_client, request_temp)
