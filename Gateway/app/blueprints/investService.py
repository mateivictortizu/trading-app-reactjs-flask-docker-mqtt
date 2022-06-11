import json

from flask import Blueprint, request

from app.RabbitMQClients.InvestRabbitMQ import BuyClient, SellClient

invest = Blueprint('invest', __name__)


@invest.route('/buy-invested', methods=['POST'])
def buy_invested():
    buy = BuyClient()
    response = json.loads(buy.call(request.json))
    return response['message'], response['code']


@invest.route('/sell-invested', methods=['POST'])
def sell_invested():
    sell = SellClient()
    response = json.loads(sell.call(request.json))
    return response['message'], response['code']
