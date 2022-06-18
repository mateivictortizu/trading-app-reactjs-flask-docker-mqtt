import json

from flask import jsonify

from app.RabbitMQClients.FundsRabbitMQ import AddMoneyClient, WithdrawMoneyClient, GetFundsClient, \
    AddMoneyAfterSellClient, WithdrawMoneyAfterBuyClient


def add_money_processor(add_money_client, json_body):
    if add_money_client is None:
        add_money_client = AddMoneyClient()
    try:
        response = json.loads(add_money_client.call(json_body))
        return response, response['code']
    except Exception:
        try:
            add_money_client = AddMoneyClient()
            response = json.loads(add_money_client.call(json_body))
            return response, response['code']
        except Exception:
            return jsonify({'error': 'Add money server error', 'code': 500}), 500


def add_money_after_sell_processor(add_money_after_sell_client, json_body):
    if add_money_after_sell_client is None:
        add_money_after_sell_client = AddMoneyAfterSellClient()
    try:
        response = json.loads(add_money_after_sell_client.call(json_body))
        return response, response['code']
    except Exception:
        try:
            add_money_after_sell_client = AddMoneyAfterSellClient()
            response = json.loads(add_money_after_sell_client.call(json_body))
            return response, response['code']
        except Exception:
            return jsonify({'error': 'Add money after sell server error', 'code': 500}), 500


def withdraw_money_processor(withdraw_money_client, json_body):
    if withdraw_money_client is None:
        withdraw_money_client = WithdrawMoneyClient()
    try:
        response = json.loads(withdraw_money_client.call(json_body))
        return response, response['code']
    except Exception:
        try:
            withdraw_money_client = WithdrawMoneyClient()
            response = json.loads(withdraw_money_client.call(json_body))
            return response, response['code']
        except Exception:
            return jsonify({'error': 'Withdraw money server error', 'code': 500}), 500


def withdraw_money_after_buy_processor(withdraw_money_after_buy_client, json_body):
    if withdraw_money_after_buy_client is None:
        withdraw_money_after_buy_client = WithdrawMoneyAfterBuyClient()
    try:
        response = json.loads(withdraw_money_after_buy_client.call(json_body))
        return response, response['code']
    except Exception:
        try:
            withdraw_money_after_buy_client = WithdrawMoneyAfterBuyClient()
            response = json.loads(withdraw_money_after_buy_client.call(json_body))
            return response, response['code']
        except Exception:
            return jsonify({'error': 'Withdraw money after buy server error', 'code': 500}), 500


def get_funds_processor(get_funds_client, json_body):
    if get_funds_client is None:
        get_funds_client = GetFundsClient()
    try:
        response = json.loads(get_funds_client.call(json_body))
        return response, response['code']
    except Exception:
        try:
            get_funds_client = GetFundsClient()
            response = json.loads(get_funds_client.call(json_body))
            return response, response['code']
        except Exception:
            return jsonify({'error': 'Get Funds server error', 'code': 500}), 500
