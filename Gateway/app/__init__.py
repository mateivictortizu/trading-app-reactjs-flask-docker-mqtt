from flask import Flask, request, session, make_response
from flask_cors import CORS
from flask_session import Session
from flask_socketio import SocketIO

from app.RabbitMQProcessor.FundsRabbitMQProcessor import get_funds_processor
from app.RabbitMQProcessor.InvestRabbitMQProcessor import get_invest_by_user_processor
from app.RabbitMQProcessor.StockRabbitMQProcessor import get_list_stock_price_processor, get_all_stocks_processor, \
    get_all_stocks_by_user_processor
from app.blueprints import get_all_stocks_client, before_request_function, get_all_stocks_by_user_client, \
    users_connections, get_invest

app = Flask(__name__)

app.config['CORS_EXPOSE_HEADERS'] = 'Authorization'
app.config['CORS_ALLOW_HEADERS'] = ['Content-Type', 'Access-Control-Allow-Credentials']
app.config['CORS_ORIGINS'] = ['http://localhost:3000', 'http://localhost:8000']
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = 'filesystem'
app.config['SESSION_COOKIE_SAMESITE'] = 'None'
app.config['SESSION_COOKIE_SECURE'] = True
Session(app)
cors = CORS(app, supports_credentials=True)
socketio = SocketIO(app, cors_allowed_origins='http://localhost:3000')

from app.blueprints.fundsService import funds
from app.blueprints.stockService import stock
from app.blueprints.investService import invest
from app.blueprints.userService import user
from app.blueprints.recommendationService import recommendations

app.register_blueprint(funds)
app.register_blueprint(stock)
app.register_blueprint(invest)
app.register_blueprint(user)
app.register_blueprint(recommendations)

get_list_stock_price_client = None
get_funds_client = None


@app.before_request
def before_request():
    print(str(request.method) + str(request.path))


@socketio.on('connect')
def join_connect():
    try:
        before_request_function(request)
        json_body = {"stock_list": ["AAPL", "MSFT", "AMZN", "YUM", "NVDA", "F"]}
        stock_popular_list = get_list_stock_price_processor(get_list_stock_price_client, json_body=json_body)
        socketio.emit('stock_popular', stock_popular_list[0])
        get_funds_value = get_funds_processor(get_funds_client, {'user': 'matteovkt@gmail.com'})
        socketio.emit('get_funds', {'value': get_funds_value[0]['value']})
        get_all_stock = get_all_stocks_by_user_processor(get_all_stocks_by_user_client,
                                                         {'user': 'matteovkt@gmail.com'})
        socketio.emit('get_all_stocks', {'value': get_all_stock[0]['list']})
        watchlist_list = []
        for i in get_all_stock[0]['list']:
            if i['watchlist'] is True:
                watchlist_list.append(i['stock_symbol'])
        json_body = {"stock_list": watchlist_list}
        stock_wishlist = get_list_stock_price_processor(get_list_stock_price_client, json_body=json_body)
        socketio.emit('stock_wishlist', stock_wishlist[0])
        stock_invest = get_invest_by_user_processor(get_invest, json_body={'identifier': 'matteovkt@gmail.com'})
        json_body = {"stock_list": stock_invest[0]['stock_list']}
        stock_invest_list = get_list_stock_price_processor(get_list_stock_price_client, json_body=json_body)
        socketio.emit('stock_invest', stock_invest_list[0])
    except Exception as e:
        print(e)


@socketio.on('disconnect')
def test_disconnect():
    session.pop('user_id', None)
    print('Client disconnected')
