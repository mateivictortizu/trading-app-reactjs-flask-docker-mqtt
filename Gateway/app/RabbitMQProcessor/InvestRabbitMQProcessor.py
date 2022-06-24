import json

from app.RabbitMQClients.InvestRabbitMQ import BuyClient, SellClient, GetStockInvestByUserClient, \
    GetAllInvestByUserClient, GetHistoryStockByUserClient


def buy_processor(buy, json_body):
    if buy is None:
        buy = BuyClient()
    try:
        response = json.loads(buy.call(json_body))
        return response, response['code']
    except Exception:
        try:
            buy = BuyClient()
            response = json.loads(buy.call(json_body))
            return response, response['code']
        except Exception:
            return 'Buy server error', 500


def sell_processor(sell, json_body):
    if sell is None:
        sell = SellClient()
    try:
        response = json.loads(sell.call(json_body))
        return response, response['code']
    except Exception:
        try:
            sell = SellClient()
            response = json.loads(sell.call(json_body))
            return response, response['code']
        except Exception:
            return 'Sell server error', 500


def get_stock_invest_by_user_processor(get_stock, json_body):
    if get_stock is None:
        get_stock = GetStockInvestByUserClient()
    try:
        response = json.loads(get_stock.call(json_body))
        return response, response['code']
    except Exception:
        try:
            get_stock = GetStockInvestByUserClient()
            response = json.loads(get_stock.call(json_body))
            return response, response['code']
        except Exception:
            return 'Get Stock Invest By User server error', 500


def get_invest_by_user_processor(get_invest, json_body):
    if get_invest is None:
        get_invest = GetAllInvestByUserClient()
    try:
        response = json.loads(get_invest.call(json_body))
        return response, response['code']
    except Exception:
        try:
            get_invest = GetAllInvestByUserClient()
            response = json.loads(get_invest.call(json_body))
            return response, response['code']
        except Exception:
            return 'Get Invest By User server error', 500


def get_history_stock_user_processor(get_history_stock_user_client, json_body):
    if get_history_stock_user_client is None:
        get_history_stock_user_client = GetHistoryStockByUserClient()
    try:
        response = json.loads(get_history_stock_user_client.call(json_body))
        return response, response['code']
    except Exception:
        try:
            get_history_stock_user_client = GetHistoryStockByUserClient()
            response = json.loads(get_history_stock_user_client.call(json_body))
            return response, response['code']
        except Exception:
            return 'Get History Stock By User server error', 500
