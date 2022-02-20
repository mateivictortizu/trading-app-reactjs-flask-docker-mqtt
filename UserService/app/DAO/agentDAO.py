from flask import jsonify

from app.database.models import User


def verify_userDAO(identifier):
    result_of_verify = User.verify_user(identifier=identifier)
    if result_of_verify is False:
        return jsonify({'error': 'Validation failed'}), 400
    elif result_of_verify is True:
        return jsonify({'message': 'Validation successfully'}), 200


def ban_userDAO(user_to_ban):
    banned_check = User.ban_user(user_to_ban)
    if banned_check is True:
        return jsonify({'message': 'User was banned'}), 200
    elif banned_check is False:
        return jsonify({'error': 'Error or user was already banned'}), 400
