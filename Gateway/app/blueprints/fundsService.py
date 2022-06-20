from flask import Blueprint, request

from app import socketio
from app.RabbitMQProcessor.FundsRabbitMQProcessor import add_money_processor, withdraw_money_processor, \
    get_funds_processor, withdraw_money_after_buy_processor, add_money_after_sell_processor
from app.blueprints import add_session, add_money_client, withdraw_money_client, get_funds_client, \
    withdraw_money_after_buy_client, add_money_after_sell_client

funds = Blueprint('funds', __name__)


@funds.before_request
def before_request():
    print(request.json)


@funds.route('/add-money', methods=['POST'])
def add_money():
    add_money_value = add_money_processor(add_money_client, request.json)
    value_after_add = get_funds_processor(get_funds_client, {'user': request.json['user']})
    print(request.json)
    socketio.emit('get_funds', {'value': value_after_add[0]['value']})
    return add_money_value


@funds.route('/withdraw-money', methods=['POST'])
def withdraw_money():
    withdraw_money_value = withdraw_money_processor(withdraw_money_client, request.json)
    value_after_withdraw = get_funds_processor(get_funds_client, {'user': request.json['user']})
    socketio.emit('get_funds', {'value': value_after_withdraw[0]['value']})
    return withdraw_money_value


@funds.route('/add-money-after-sell', methods=['POST'])
def add_money_after_sell():
    add_money_value = add_money_after_sell_processor(add_money_after_sell_client, request.json)
    value_after_add = get_funds_processor(get_funds_client, {'user': request.json['user']})
    socketio.emit('get_funds', {'value': value_after_add[0]['value']})
    return add_money_value


@funds.route('/withdraw-money-after-buy', methods=['POST'])
def withdraw_money_after_buy():
    withdraw_money_value = withdraw_money_after_buy_processor(withdraw_money_after_buy_client, request.json)
    value_after_withdraw = get_funds_processor(get_funds_client, {'user': request.json['user']})
    socketio.emit('get_funds', {'value': value_after_withdraw[0]['value']})
    return withdraw_money_value


@funds.route('/get-funds/<user>')
def get_funds(user):
    return get_funds_processor(get_funds_client, {'user': user})
