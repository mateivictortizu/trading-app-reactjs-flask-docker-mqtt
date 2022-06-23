import json

from flask import jsonify

from app.RabbitMQClients.StocksRabbitMQ import GetListStockPriceClient, AddStockClient, GetStockInfoClient, \
    GetStockPriceClient, UpdatePriceClient, UpdateStockClient, GetAllStocksClient, GetAllStocksByUserClient, \
    RemoveWatchlistClient, AddWatchlistClient


def add_stock_processor(add_stock_client, json_body):
    if add_stock_client is None:
        add_stock_client = AddStockClient()
    try:
        response = json.loads(add_stock_client.call(json_body))
        return response, response['code']
    except Exception:
        try:
            add_stock_client = AddStockClient()
            response = json.loads(add_stock_client.call(json_body))
            return response, response['code']
        except Exception:
            return jsonify({'error': 'Add stock server error', 'code': 500}), 500


def get_stock_info_processor(get_stock_info_client, stock_symbol):
    if get_stock_info_client is None:
        get_stock_info_client = GetStockInfoClient()
    try:
        response = json.loads(get_stock_info_client.call({'stock_symbol': stock_symbol}))
        return response, response['code']
    except Exception:
        try:
            get_stock_info_client = GetStockInfoClient()
            response = json.loads(get_stock_info_client.call({'stock_symbol': stock_symbol}))
            return response, response['code']
        except Exception:
            return jsonify({'error': 'Get stock info server error', 'code': 500}), 500


def get_stock_price_processor(get_stock_price_client, stock_symbol):
    if get_stock_price_client is None:
        get_stock_price_client = GetStockPriceClient()
    try:
        response = json.loads(get_stock_price_client.call({'stock_symbol': stock_symbol}))
        return response, response['code']
    except Exception:
        try:
            get_stock_price_client = GetStockPriceClient()
            response = json.loads(get_stock_price_client.call({'stock_symbol': stock_symbol}))
            return response, response['code']
        except Exception:
            return jsonify({'error': 'Get stock price server error', 'code': 500}), 500


def get_list_stock_price_processor(get_list_stock_price_client, json_body):
    if get_list_stock_price_client is None:
        get_list_stock_price_client = GetListStockPriceClient()
    try:
        response = json.loads(get_list_stock_price_client.call(json_body))
        return response, response['code']
    except Exception as e:
        try:
            get_list_stock_price_client = GetListStockPriceClient()
            response = json.loads(get_list_stock_price_client.call(json_body))
            return response, response['code']
        except Exception:
            return jsonify({'error': 'Get list stock price server error', 'code': 500}), 500


def update_price_processor(update_price_client, json_body):
    if update_price_client is None:
        update_price_client = UpdatePriceClient()
    try:
        response = json.loads(update_price_client.call(json_body))
        return response, response['code']
    except Exception:
        try:
            update_price_client = UpdatePriceClient()
            response = json.loads(update_price_client.call(json_body))
            return response, response['code']
        except Exception:
            return jsonify({'error': 'Update price server error', 'code': 500}), 500


def update_stock_processor(update_stock_client, json_body):
    if update_stock_client is None:
        update_stock_client = UpdateStockClient()
    try:
        response = json.loads(update_stock_client.call(json_body))
        return response, response['code']
    except Exception:
        try:
            update_stock_client = UpdateStockClient()
            response = json.loads(update_stock_client.call(json_body))
            return response, response['code']
        except Exception:
            return jsonify({'error': 'Update stock server error', 'code': 500}), 500


def get_all_stocks_processor(get_all_stocks_client):
    if get_all_stocks_client is None:
        get_all_stocks_client = GetAllStocksClient()
    try:
        response = json.loads(get_all_stocks_client.call(None))
        return response, response['code']
    except Exception:
        try:
            get_all_stocks_client = GetAllStocksClient()
            response = json.loads(get_all_stocks_client.call(None))
            return response, response['code']
        except Exception:
            return jsonify({'error': 'Get all stocks server error', 'code': 500}), 500


def get_all_stocks_by_user_processor(get_all_stocks_by_user_client, request_body):
    if get_all_stocks_by_user_client is None:
        get_all_stocks_by_user_client = GetAllStocksByUserClient()
    try:
        response = json.loads(get_all_stocks_by_user_client.call(request_body))
        return response, response['code']
    except Exception:
        try:
            get_all_stocks_by_user_client = GetAllStocksByUserClient()
            response = json.loads(get_all_stocks_by_user_client.call(request_body))
            return response, response['code']
        except Exception:
            return jsonify({'error': 'Get all stocks by user server error', 'code': 500}), 500


def add_watchlist_processor(add_watchlist_client, request_body):
    if add_watchlist_client is None:
        add_watchlist_client = AddWatchlistClient()
    try:
        response = json.loads(add_watchlist_client.call(request_body))
        return response, response['code']
    except Exception:
        try:
            add_watchlist_client = AddWatchlistClient()
            response = json.loads(add_watchlist_client.call(request_body))
            return response, response['code']
        except Exception:
            return jsonify({'error': 'Add watchlist server error', 'code': 500}), 500


def remove_watchlist_processor(remove_watchlist_client, request_body):
    if remove_watchlist_client is None:
        remove_watchlist_client = RemoveWatchlistClient()
    try:
        response = json.loads(remove_watchlist_client.call(request_body))
        return response, response['code']
    except Exception:
        try:
            remove_watchlist_client = RemoveWatchlistClient()
            response = json.loads(remove_watchlist_client.call(request_body))
            return response, response['code']
        except Exception:
            return jsonify({'error': 'Remove watchlist server error', 'code': 500}), 500
