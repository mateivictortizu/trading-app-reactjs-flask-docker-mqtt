from flask import Blueprint, request, jsonify, session

from app import socketio
from app.RabbitMQProcessor.FundsRabbitMQProcessor import get_funds_processor, add_money_after_sell_processor, \
    withdraw_money_after_buy_processor
from app.RabbitMQProcessor.InvestRabbitMQProcessor import buy_processor, sell_processor, \
    get_stock_invest_by_user_processor, get_invest_by_user_processor
from app.blueprints import get_funds_client, buy, sell, get_stock, get_invest, add_money_after_sell_client, \
    withdraw_money_after_buy_client, before_request_function, users_connections

invest = Blueprint('invest', __name__)


@invest.route('/buy', methods=['POST'])
def buy_invested():
    before_request_function(request)
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
                                                                {'identifier': users_connections[session['user_id']]['user'],
                                                                 'stock_symbol': request.json['stock_symbol']})
        socketio.emit('get_investment', {
            'cantitate': float(get_value_of_stock[0]['cantitate']), 'medie': float(get_value_of_stock[0]['medie'])})
        return buy_result
    else:
        return jsonify({"message": "Not enough funds"}), 400


@invest.route('/sell', methods=['POST'])
def sell_invested():
    before_request_function(request)
    print(users_connections[session['user_id']]['user'])
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
                                                                {'identifier': users_connections[session['user_id']]['user'],
                                                                 'stock_symbol': request.json['stock_symbol']})
        socketio.emit('get_investment', {
            'cantitate': float(get_value_of_stock[0]['cantitate']), 'medie': float(get_value_of_stock[0]['medie'])})
        return sell_result
    else:
        return jsonify({'message': 'Add money error'}), 400


@invest.route('/get-stock-invest-by-user', methods=['POST'])
def get_stock_invest_by_user():
    before_request_function(request)
    request_temp = dict()
    request_temp['stock_symbol'] = request.json['stock_symbol']
    request_temp['identifier'] = users_connections[session['user_id']]['user']
    return get_stock_invest_by_user_processor(get_stock, request_temp)


@invest.route('/get-invest-by-user', methods=['POST'])
def get_invest_by_user():
    before_request_function(request)
    print(request.json)
    return get_invest_by_user_processor(get_invest, request.json)
