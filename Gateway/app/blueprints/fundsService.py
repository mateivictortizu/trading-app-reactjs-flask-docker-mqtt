from flask import Blueprint, request, session

from app import socketio
from app.RabbitMQProcessor.FundsRabbitMQProcessor import add_money_processor, withdraw_money_processor, \
    get_funds_processor, withdraw_money_after_buy_processor, add_money_after_sell_processor
from app.blueprints import add_money_client, withdraw_money_client, get_funds_client, \
    withdraw_money_after_buy_client, add_money_after_sell_client, before_request_function, users_connections

funds = Blueprint('funds', __name__)


@funds.route('/add-money', methods=['POST'])
def add_money():
    before_request_function(request)
    request_body = dict()
    request_body['value'] = request.json['value']
    request_body['user'] = users_connections[session['user_id']]['user']
    add_money_value = add_money_processor(add_money_client, request_body)
    value_after_add = get_funds_processor(get_funds_client, {'user': users_connections[session['user_id']]['user']})
    socketio.emit('get_funds', {'value': value_after_add[0]['value']})
    return add_money_value


@funds.route('/withdraw-money', methods=['POST'])
def withdraw_money():
    before_request_function(request)
    request_body = dict()
    request_body['value'] = request.json['value']
    request_body['user'] = users_connections[session['user_id']]['user']
    withdraw_money_value = withdraw_money_processor(withdraw_money_client, request_body)
    value_after_withdraw = get_funds_processor(get_funds_client,
                                               {'user': users_connections[session['user_id']]['user']})
    socketio.emit('get_funds', {'value': value_after_withdraw[0]['value']})
    return withdraw_money_value


@funds.route('/add-money-after-sell', methods=['POST'])
def add_money_after_sell():
    before_request_function(request)
    request_body = dict()
    request_body['value'] = request.json['value']
    request_body['cantitate'] = request.json['cantitate']
    request_body['price'] = request.json['price']
    request_body['user'] = users_connections[session['user_id']]['user']
    add_money_value = add_money_after_sell_processor(add_money_after_sell_client, request_body)
    value_after_add = get_funds_processor(get_funds_client, {'user': users_connections[session['user_id']]['user']})
    socketio.emit('get_funds', {'value': value_after_add[0]['value']})
    return add_money_value


@funds.route('/withdraw-money-after-buy', methods=['POST'])
def withdraw_money_after_buy():
    before_request_function(request)
    request_body = dict()
    request_body['value'] = request.json['value']
    request_body['cantitate'] = request.json['cantitate']
    request_body['price'] = request.json['price']
    request_body['user'] = users_connections[session['user_id']]['user']
    withdraw_money_value = withdraw_money_after_buy_processor(withdraw_money_after_buy_client, request_body)
    value_after_withdraw = get_funds_processor(get_funds_client,
                                               {'user': users_connections[session['user_id']]['user']})
    socketio.emit('get_funds', {'value': value_after_withdraw[0]['value']})
    return withdraw_money_value


@funds.route('/get-funds/<user>')
def get_funds(user):
    before_request_function(request)
    return get_funds_processor(get_funds_client, {'user': users_connections[session['user_id']]['user']})
