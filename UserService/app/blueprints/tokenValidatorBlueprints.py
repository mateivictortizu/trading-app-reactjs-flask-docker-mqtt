from flask import Blueprint, jsonify
from flask_json_schema import JsonValidationError
from sqlalchemy.exc import DatabaseError

tokenValidatorBP = Blueprint('tokenValidatorBlueprint', __name__)


@tokenValidatorBP.errorhandler(JsonValidationError)
def validator_error(e):
    return jsonify({'error': e.message, 'errors': [validation_error.message for validation_error in e.errors]}), 400


@tokenValidatorBP.errorhandler(DatabaseError)
def database_error():
    return jsonify({'error': 'Database error'}), 500


#TODO implementation of check token
@tokenValidatorBP.route('/check-token', methods=['GET'])
def check_token():
    pass
