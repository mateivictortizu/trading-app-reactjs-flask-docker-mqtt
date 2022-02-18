from datetime import datetime

from flask import Blueprint
from flask import request, jsonify, current_app
from flask_json_schema import JsonValidationError
from sqlalchemy.exc import DatabaseError

from app import db, schema, mail
from app.DAO.userDAO import registerDAO, loginDAO, validate_accountDAO, resend_validate_accountDAO, validate_otpDAO, \
    resend_otpDAO, logoutDAO, change_passwordDAO
from app.json_schema import register_schema, login_schema, validate_otp_schema, resend_validate_schema, \
    resend_otp_schema

userBP = Blueprint('userBlueprint', __name__)


@userBP.errorhandler(JsonValidationError)
def validator_error(e):
    return jsonify({'error': e.message, 'errors': [validation_error.message for validation_error in e.errors]}), 400


@userBP.errorhandler(DatabaseError)
def database_error(e):
    return jsonify({'error': 'Database error'}), 500


@userBP.route('/register', methods=['POST'])
@schema.validate(register_schema)
def register():
    username = request.json['username']
    password = request.json['password']
    email = request.json['email']
    name = request.json['name']
    surname = request.json['surname']
    address = request.json['address']
    nationality = request.json['nationality']
    phone = request.json['phone']
    date_of_birth_str = request.json['date_of_birth']
    date_of_birth = datetime.strptime(date_of_birth_str, '%Y-%m-%d')
    country = request.json['country']

    return registerDAO(request, current_app, db, mail, username, password, email, name, surname, address, nationality,
                       phone, date_of_birth, country)


@userBP.route('/login', methods=['POST'])
@schema.validate(login_schema)
def login():
    identifier = request.json['identifier']
    password = request.json['password']
    return loginDAO(current_app, db, mail, password, identifier)


@userBP.route('/validate-account/<validation_code>', methods=['GET'])
def validate_account(validation_code):
    return validate_accountDAO(current_app, db, validation_code)


@userBP.route('/resend-validate-account', methods=['POST'])
@schema.validate(resend_validate_schema)
def resend_validate_account():
    identifier = request.json['identifier']
    return resend_validate_accountDAO(request, current_app, mail, identifier)


@userBP.route('/validate-otp', methods=['POST'])
@schema.validate(validate_otp_schema)
def validate_otp():
    identifier = request.json['identifier']
    code = request.json['code']
    return validate_otpDAO(current_app, identifier, code)


@userBP.route('/resend-otp', methods=['POST'])
@schema.validate(resend_otp_schema)
def resend_otp():
    identifier = request.json['identifier']
    return resend_otpDAO(current_app, db, mail, identifier)


@userBP.route('/logout', methods=['DELETE'])
def logout():
    return logoutDAO(request)


# TODO change pass schema
@userBP.route('/change-password', methods=['PUT'])
def change_password():
    identifier = request.json['identifier']
    password = request.json['password']
    new_password = request.json['new_password']
    return change_passwordDAO(identifier, password, new_password)
