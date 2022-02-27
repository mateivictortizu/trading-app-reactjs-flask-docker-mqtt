from flask import Blueprint, jsonify
from flask_json_schema import JsonValidationError
from sqlalchemy.exc import DatabaseError

fundsBP = Blueprint('fundsBlueprint', __name__)


@fundsBP.errorhandler(JsonValidationError)
def validator_error(e):
    return jsonify({'error': e.message, 'errors': [validation_error.message for validation_error in e.errors]}), 400


@fundsBP.errorhandler(DatabaseError)
def database_error():
    return jsonify({'error': 'Database error'}), 500
