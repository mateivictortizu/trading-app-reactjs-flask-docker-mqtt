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
ban_client = None
verify_user_client = None
check_token_client = None
register_client = None
login_client = None
validate_account_client = None
resend_validate_account_client = None
validate_otp_client = None
resend_otp_client = None
logout_client = None
change_password_client = None
request_change_password_client = None
reset_pass_client = None
set_new_pass_client = None


def before_request_function(request_value):
    if 'user_id' not in session:
        value_jwt = request_value.cookies.get('jwt')
        # result_token = check_token_processor(check_token_client, request.json)
        user_id = str(uuid.uuid4())
        session['user_id'] = user_id
        users_connections.append({user_id: {'token': value_jwt}})
    print(users_connections)
    print(session['user_id'])
