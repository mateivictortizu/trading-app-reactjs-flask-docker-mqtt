import uuid
from flask import session

users_connections = []

add_money_client = None
withdraw_money_client = None
get_funds_client = None
withdraw_money_after_buy_client = None
add_money_after_sell_client = None
buy = None
sell = None
get_stock = None
get_invest = None
add_stock_client = None
get_stock_info_client = None
get_stock_price_client = None
get_list_stock_price_client = None
update_price_client = None
update_stock_client = None
get_all_stocks_client = None


def add_session():
    if 'user_id' not in session:
        print('Works')
        session['user_id'] = str(uuid.uuid4())
