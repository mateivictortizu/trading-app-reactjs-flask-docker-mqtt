from flask import Blueprint, jsonify, request
from flask_json_schema import JsonValidationError
from sqlalchemy.exc import DatabaseError

from app import schema
from app.DAO.agentDAO import verify_userDAO, ban_userDAO
from app.json_schema import verify_user_schema, ban_user_schema

agentBP = Blueprint('adminBlueprint', __name__)


@agentBP.errorhandler(JsonValidationError)
def validator_error(e):
    return jsonify({'error': e.message, 'errors': [validation_error.message for validation_error in e.errors]}), 400


@agentBP.errorhandler(DatabaseError)
def database_error():
    return jsonify({'error': 'Database error'}), 500


# The entire investment goes to the company if the user violates the rules and is banned.
# Uninvested money will be returned.
# TODO Role validation checking before banning
@agentBP.route('/ban', methods=['DELETE'])
@schema.validate(ban_user_schema)
def ban_user():
    user_to_ban = request.json['user-to-ban']
    return ban_userDAO(user_to_ban)


@agentBP.route('/verify-user', methods=['PUT'])
@schema.validate(verify_user_schema)
def verify_user():
    identifier = request.json['identifier']
    return verify_userDAO(identifier)
