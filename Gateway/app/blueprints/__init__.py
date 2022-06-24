import pickle
import uuid

from flask import session, jsonify

from app.RabbitMQProcessor.UserRabbitMQProcessor import check_token_processor

users_connections = {}

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
get_all_stocks_by_user_client = None
add_watchlist_client = None
remove_watchlist_client = None
recommendation_client = None
get_history_stock_user_client = None
get_all_history_user_client = None

def before_request_function(request_value):
    if 'user_id' not in session:
        if 'jwt' in request_value.cookies:
            jwt_value = request_value.cookies.get('jwt')
            value = check_token_processor(check_token_client, {'jwt': jwt_value})
            user_id = str(uuid.uuid4())
            session['user_id'] = user_id
            users_connections[user_id] = {'user': value[0]['user'], 'type_user': value[0]['type_user']}
        else:
            return jsonify({'error': 'JWT not in request'}), 403
    else:
        if session['user_id'] not in users_connections:
            if 'jwt' in request_value.cookies:
                jwt_value = request_value.cookies.get('jwt')
                value = check_token_processor(check_token_client, {'jwt': jwt_value})
                users_connections[session['user_id']] = {'user': value[0]['user'], 'type_user': value[0]['type_user']}
            else:
                session.pop('user_id', None)
    print(users_connections)
    return jsonify({'message': 'JWT Ok'}), 200
