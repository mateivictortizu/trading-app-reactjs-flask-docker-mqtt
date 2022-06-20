from flask import Blueprint, jsonify, request, current_app
from flask_json_schema import JsonValidationError
from sqlalchemy.exc import DatabaseError

from app.DAO.tokenValidatorDAO import validate_Token

tokenValidatorBP = Blueprint('tokenValidatorBlueprint', __name__)


@tokenValidatorBP.errorhandler(JsonValidationError)
def validator_error(e):
    return jsonify({'error': e.message, 'errors': [validation_error.message for validation_error in e.errors]}), 400


@tokenValidatorBP.errorhandler(DatabaseError)
def database_error():
    return jsonify({'error': 'Database error'}), 500


@tokenValidatorBP.route('/check-token', methods=['GET'])
def check_token():
    try:
        token = request.cookies.get('jwt')
        if token is None:
            return jsonify({'error': 'JWT missing'}), 500
        return validate_Token(token, current_app)
    except Exception as e:
        return jsonify({'error': 'JWT check fail'}), 500
