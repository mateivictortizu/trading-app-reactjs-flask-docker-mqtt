from flask import Blueprint, jsonify, request
from flask_json_schema import JsonValidationError
from sqlalchemy.exc import DatabaseError

from app import db
from app.database.models import User

agentBP = Blueprint('adminBlueprint', __name__)


@agentBP.errorhandler(JsonValidationError)
def validator_error(e):
    return jsonify({'error': e.message, 'errors': [validation_error.message for validation_error in e.errors]}), 400


@agentBP.errorhandler(DatabaseError)
def database_error(e):
    return jsonify({'error': 'Database error'}), 500


# The entire investment goes to the company if the user violates the rules and is banned.
# Uninvested money will be returned.
@agentBP.route('/ban', methods=['DELETE'])
def ban():
    pass


# TODO check it
@agentBP.route('/verify-user', methods=['PUT'])
def verify_user():
    identifier = request.json['identifier']
    User.verify_user(identifier=identifier)
    pass
