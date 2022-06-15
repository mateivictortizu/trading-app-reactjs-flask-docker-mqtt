from urllib import parse

import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_session import Session
from flask_socketio import SocketIO, send, emit

from app.RabbitMQProcessor.StockRabbitMQProcessor import get_list_stock_price_processor

app = Flask(__name__)

app.config['CORS_EXPOSE_HEADERS'] = 'Authorization'
app.config['CORS_ALLOW_HEADERS'] = ['Content-Type', 'Authorization']
app.config['CORS_ORIGINS'] = ['http://localhost:3000', 'http://localhost:8000']
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
cors = CORS(app)
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


@app.before_request
def before_request():
    print(str(request.method) + str(request.path))


@socketio.on('connect')
def join_connect():
    print('Client connected')
    print('OK')
    get_list_stock_price_client = None
    json_body = {"stock_list": ["AAPL", "MSFT", "AMZN", "YUM", "NVDA", "F"]}
    stock_popular_list = get_list_stock_price_processor(get_list_stock_price_client, json_body=json_body)
    socketio.emit('stock_popular', stock_popular_list[0])
    json_body = {"stock_list": ["FB", "INTC", "AMD", "NIO"]}
    stock_wishlist = get_list_stock_price_processor(get_list_stock_price_client, json_body=json_body)
    socketio.emit('stock_wishlist', stock_wishlist[0])
    socketio.emit('get_funds', {'value': 50})


@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')
