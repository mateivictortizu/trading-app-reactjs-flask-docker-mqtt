from flask import Flask
from flask_cors import CORS
from flask_session import Session

from app.blueprints.fundsService import funds
from app.blueprints.stockService import stock
from app.blueprints.investService import invest
from app.blueprints.userService import user

app = Flask(__name__)
app.register_blueprint(funds)
app.register_blueprint(stock)
app.register_blueprint(invest)
app.register_blueprint(user)
app.config['CORS_EXPOSE_HEADERS'] = 'Authorization'
app.config['CORS_ALLOW_HEADERS'] = ['Content-Type', 'Authorization']
app.config['CORS_ORIGINS'] = ['http://localhost:3000', 'http://localhost:8000']
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
cors = CORS(app)
