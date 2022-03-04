from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Blueprint, jsonify, request
from flask_json_schema import JsonValidationError
from sqlalchemy.exc import DatabaseError

from app import executor
from app.DAO.stockDAO import addStockDAO, updateStockDAO, updatePriceDAO

stockBP = Blueprint('stockBlueprint', __name__)


sched = BackgroundScheduler(daemon=True)
#sched.add_job(updateStockDAO, 'interval', seconds=30)
sched.add_job(updatePriceDAO, 'interval', seconds=5)
sched.start()


@stockBP.errorhandler(JsonValidationError)
def validator_error(e):
    return jsonify({'error': e.message, 'errors': [validation_error.message for validation_error in e.errors]}), 400


@stockBP.errorhandler(DatabaseError)
def database_error():
    return jsonify({'error': 'Database error'}), 500


@stockBP.route('/add-stock', methods=['POST'])
def add_stock():
    symbol_stock = request.json['stock_symbol']
    executor.submit(addStockDAO, symbol_stock)
    return jsonify({'message': 'Stock was added to db'}), 200
