from flask import Flask
from flask_cors import CORS

from app.blueprints.fundsService import funds
from app.blueprints.stockService import stock
from app.blueprints.investService import invest

app = Flask(__name__)
app.register_blueprint(funds)
app.register_blueprint(stock)
app.register_blueprint(invest)
app.config['CORS_EXPOSE_HEADERS'] = 'Authorization'
app.config['CORS_ALLOW_HEADERS'] = ['Content-Type', 'Authorization']
app.config['CORS_ORIGINS'] = 'http://localhost:3000'

cors = CORS(app)
