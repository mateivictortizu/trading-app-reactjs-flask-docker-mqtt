import json

from flask import Blueprint, request, jsonify

from app.RabbitMQClients.FundsRabbitMQ import AddMoneyClient, WithdrawMoneyClient, GetFundsClient

from app import socketio

funds = Blueprint('funds', __name__)

add_money_client = None
withdraw_money_client = None
get_funds_client = None


@funds.route('/add-money', methods=['POST'])
def add_money():
    global add_money_client
    if add_money_client is None:
        add_money_client = AddMoneyClient()
    try:
        response = json.loads(add_money_client.call(request.json))
        return response, response['code']
    except Exception:
        try:
            add_money_client = AddMoneyClient()
            response = json.loads(add_money_client.call(request.json))
            return response, response['code']
        except Exception:
            return jsonify({'error': 'Add money server error', 'code': 500}), 500


@funds.route('/withdraw-money', methods=['POST'])
def withdraw_money():
    global withdraw_money_client
    if withdraw_money_client is None:
        withdraw_money_client = WithdrawMoneyClient()
    try:
        response = json.loads(withdraw_money_client.call(request.json))
        return response, response['code']
    except Exception:
        try:
            withdraw_money_client = WithdrawMoneyClient()
            response = json.loads(withdraw_money_client.call(request.json))
            return response, response['code']
        except Exception:
            return jsonify({'error': 'Withdraw money server error', 'code': 500}), 500


@funds.route('/get-funds/<user>')
def get_funds(user):
    global get_funds_client
    if get_funds_client is None:
        get_funds_client = GetFundsClient()
    try:
        response = json.loads(get_funds_client.call({'user': user}))
        return response, response['code']
    except Exception:
        try:
            get_funds_client = GetFundsClient()
            response = json.loads(get_funds_client.call({'user': user}))
            return response, response['code']
        except Exception:
            return jsonify({'error': 'Get Funds server error', 'code': 500}), 500
