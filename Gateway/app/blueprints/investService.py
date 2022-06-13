import json

from flask import Blueprint, request

from app.RabbitMQClients.InvestRabbitMQ import BuyClient, SellClient

invest = Blueprint('invest', __name__)
buy = None
sell = None


@invest.route('/buy-invested', methods=['POST'])
def buy_invested():
    global buy
    if buy is None:
        buy = BuyClient()
    try:
        response = json.loads(buy.call(request.json))
        return response['message'], response['code']
    except Exception:
        try:
            buy = BuyClient()
            response = json.loads(buy.call(request.json))
            return response['message'], response['code']
        except Exception:
            return 'Buy server error', 500


@invest.route('/sell-invested', methods=['POST'])
def sell_invested():
    global sell
    if sell is None:
        sell = SellClient()
    try:
        response = json.loads(sell.call(request.json))
        return response['message'], response['code']
    except Exception:
        try:
            sell = SellClient()
            response = json.loads(sell.call(request.json))
            return response['message'], response['code']
        except Exception:
            return 'Sell server error', 500
