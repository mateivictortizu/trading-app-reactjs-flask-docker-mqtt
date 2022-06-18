import uuid

from flask import Flask, request, session
from flask_cors import CORS
from flask_session import Session
from flask_socketio import SocketIO

from app.RabbitMQProcessor.FundsRabbitMQProcessor import get_funds_processor
from app.RabbitMQProcessor.StockRabbitMQProcessor import get_list_stock_price_processor, get_all_stocks_processor
from app.blueprints import get_all_stocks_client

app = Flask(__name__)

app.config['CORS_EXPOSE_HEADERS'] = 'Authorization'
app.config['CORS_ALLOW_HEADERS'] = ['Content-Type', 'Authorization']
app.config['CORS_ORIGINS'] = ['http://localhost:3000', 'http://localhost:8000']
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
cors = CORS(app,supports_credentials=True)
socketio = SocketIO(app, cors_allowed_origins='*', engineio_logger=True)

from app.blueprints.fundsService import funds
from app.blueprints.stockService import stock
from app.blueprints.investService import invest
from app.blueprints.userService import user

app.register_blueprint(funds)
app.register_blueprint(stock)
app.register_blueprint(invest)
app.register_blueprint(user)

URL = "http://127.0.0.1:5000/"

get_list_stock_price_client = None
get_funds_client = None


@app.before_request
def before_request():
    print(str(request.method) + str(request.path))


@socketio.on('connect')
def join_connect():
    if 'user_id' not in session:
        session['user_id'] = str(uuid.uuid4())
    print(session['user_id'])

    json_body = {"stock_list": ["AAPL", "MSFT", "AMZN", "YUM", "NVDA", "F"]}
    stock_popular_list = get_list_stock_price_processor(get_list_stock_price_client, json_body=json_body)
    socketio.emit('stock_popular', stock_popular_list[0])
    json_body = {"stock_list": ["FB", "INTC", "AMD", "NIO", "F", "YUM", "AMZN", "MSFT", "FB", "NVDA"]}
    stock_wishlist = get_list_stock_price_processor(get_list_stock_price_client, json_body=json_body)
    socketio.emit('stock_wishlist', stock_wishlist[0])
    get_funds_value = get_funds_processor(get_funds_client, {'user': 'matteovkt@gmail.com'})
    socketio.emit('get_funds', {'value': get_funds_value[0]['value']})
    get_all_stock = get_all_stocks_processor(get_all_stocks_client)
    socketio.emit('get_all_stocks', {'value': get_all_stock[0]['message']})


@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')
