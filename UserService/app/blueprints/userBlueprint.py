from datetime import datetime

from flask import Blueprint
from flask import request, jsonify, current_app
from flask_json_schema import JsonValidationError
from sqlalchemy.exc import DatabaseError

from app import db, schema, mail, executor
from app.DAO.userDAO import registerDAO, loginDAO, validate_accountDAO, resend_validate_accountDAO, validate_otpDAO, \
    resend_otpDAO, logoutDAO, change_passwordDAO, request_change_passwordDAO, reset_passDAO, set_new_passDAO
from app.utils.json_schema import register_schema, login_schema, validate_otp_schema, resend_validate_schema, \
    change_password_schema

userBP = Blueprint('userBlueprint', __name__)


@userBP.errorhandler(JsonValidationError)
def validator_error(e):
    return jsonify({'error': e.message, 'errors': [validation_error.message for validation_error in e.errors]}), 400


@userBP.errorhandler(DatabaseError)
def database_error():
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

    return registerDAO(executor, request, current_app, db, mail, username, password, email, name, surname, address,
                       nationality,
                       phone, date_of_birth, country)


@userBP.route('/login', methods=['POST'])
@schema.validate(login_schema)
def login():
    identifier = request.json['identifier']
    password = request.json['password']
    return loginDAO(executor, current_app, db, mail, password, identifier)


@userBP.route('/validate-account/<validation_code>', methods=['GET'])
def validate_account(validation_code):
    return validate_accountDAO(current_app, db, validation_code)


@userBP.route('/resend-validate-account', methods=['POST'])
@schema.validate(resend_validate_schema)
def resend_validate_account():
    identifier = request.json['identifier']
    return resend_validate_accountDAO(executor, request, current_app, db, mail, identifier)


@userBP.route('/validate-otp', methods=['POST'])
@schema.validate(validate_otp_schema)
def validate_otp():
    otp_jwt = request.headers.get('Authorization')
    code = request.json['code']
    return validate_otpDAO(current_app, db, otp_jwt, code)


@userBP.route('/resend-otp', methods=['POST'])
def resend_otp():
    otp_jwt = request.headers.get('Authorization')
    return resend_otpDAO(executor, current_app, db, mail, otp_jwt)


@userBP.route('/logout', methods=['DELETE'])
def logout():
    return logoutDAO(request, db)


@schema.validate(change_password_schema)
@userBP.route('/change-password', methods=['PUT'])
def change_password():
    identifier = request.json['identifier']
    password = request.json['password']
    new_password = request.json['new_password']
    return change_passwordDAO(identifier, db, password, new_password)


@userBP.route('/request-change-password', methods=['POST'])
def request_change_password():
    identifier = request.json['identifier']
    return request_change_passwordDAO(executor, current_app, mail, db, identifier)


@userBP.route('/reset-pass/<reset_code>', methods=['GET'])
def reset_pass(reset_code):
    return reset_passDAO(reset_code, current_app)


@userBP.route('/set-new-pass', methods=['POST'])
def set_new_pass():
    changePassToken = request.json['change_pass_token']
    password = request.json['password']
    return set_new_passDAO(changePassToken, password, current_app, db)
