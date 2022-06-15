import json

from flask import Blueprint, request

from app.RabbitMQClients.InvestRabbitMQ import BuyClient, SellClient, GetStockInvestByUserClient, \
    GetAllInvestByUserClient

invest = Blueprint('invest', __name__)
buy = None
sell = None
get_stock = None
get_invest = None


@invest.route('/buy', methods=['POST'])
def buy_invested():
    global buy
    if buy is None:
        buy = BuyClient()
    try:
        response = json.loads(buy.call(request.json))
        return response, response['code']
    except Exception:
        try:
            buy = BuyClient()
            response = json.loads(buy.call(request.json))
            return response, response['code']
        except Exception:
            return 'Buy server error', 500


@invest.route('/sell', methods=['POST'])
def sell_invested():
    global sell
    if sell is None:
        sell = SellClient()
    try:
        response = json.loads(sell.call(request.json))
        return response, response['code']
    except Exception:
        try:
            sell = SellClient()
            response = json.loads(sell.call(request.json))
            return response, response['code']
        except Exception:
            return 'Sell server error', 500


@invest.route('/get-stock-invest-by-user', methods=['POST'])
def get_stock_invest_by_user():
    global get_stock
    if get_stock is None:
        get_stock = GetStockInvestByUserClient()
    try:
        response = json.loads(get_stock.call(request.json))
        return response, response['code']
    except Exception:
        try:
            get_stock = GetStockInvestByUserClient()
            response = json.loads(get_stock.call(request.json))
            return response, response['code']
        except Exception:
            return 'Get Stock Invest By User server error', 500


@invest.route('/get-invest-by-user', methods=['POST'])
def get_invest_by_user():
    global get_invest
    if get_invest is None:
        get_invest = GetAllInvestByUserClient()
    try:
        response = json.loads(get_invest.call(request.json))
        return response, response['code']
    except Exception:
        try:
            get_invest = GetAllInvestByUserClient()
            response = json.loads(get_invest.call(request.json))
            return response, response['code']
        except Exception:
            return 'Get Invest By User server error', 500
