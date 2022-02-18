import json

from flask import Blueprint
from datetime import datetime

import flask
from flask import request, jsonify, current_app
from app import db, schema, mail
from app.database.models import User, Token, OTP, BlacklistToken
from app.json_schema import register_schema, login_schema, validate_otp_schema
from flask_json_schema import JsonValidationError
from flask_mail import Message
from app.myjwt import encode_auth_token
from app.myconfirmation import generate_confirmation_token, confirm_token

userBP = Blueprint('userBlueprint', __name__)


@userBP.errorhandler(JsonValidationError)
def validator_error(e):
    return jsonify({'error': e.message, 'errors': [validation_error.message for validation_error in e.errors]}), 400


@userBP.route('/register', methods=['POST'])
@schema.validate(register_schema)
def register():
    username = request.json['username']
    password = request.json['password']
    email = request.json['email']
    date_of_birth_str = request.json['date_of_birth']
    date_of_birth = datetime.strptime(date_of_birth_str, '%Y-%m-%d')
    country = request.json['country']
    if User.check_if_username_exists(username):
        return jsonify({'error': 'User already exists'}), 409
    if User.check_if_email_exists(email):
        return jsonify({'error': 'Email already exists'}), 409
    user = User(username=username, password=password, email=email, date_of_birth=date_of_birth, country=country)
    try:
        db.session.add(user)
        db.session.commit()
        try:
            msg = Message('Hello', sender=current_app.config['MAIL_USERNAME'], recipients=[user.email])
            msg.html = "<h3> Your activation link is <h3>" + request.host_url + 'validate-account/' + \
                       generate_confirmation_token(email=email, secret=current_app.config['JWT_SECRET_KEY'],
                                                   security_pass=current_app.config['JWT_SECRET_KEY'])
            mail.send(msg)
            return jsonify({'message': 'User registration completed'}), 201
        except Exception as e:
            db.session.rollback()
            return ({'error': 'Confirmation mail send failed', 'errors': [e]}), 400
    except Exception as e:
        return jsonify({'error': 'Database error', 'errors': [e]}), 400


@userBP.route('/login', methods=['POST'])
@schema.validate(login_schema)
def login():
    identifier = request.json['identifier']
    password = request.json['password']
    user_checked = User.check_user(password, identifier)
    if user_checked is False or user_checked is None:
        return jsonify({'message': 'User or password is wrong!'}), 401
    user = User.get_user_by_identifier(identifier)
    if user is None:
        return jsonify({'error': 'Unexpected error'}), 400
    if user.confirmed is False:
        return jsonify({'error': 'Please validate your account'}), 400
    if user.twoFA is True:
        otp = OTP(username=user.username, email=user.email)
        try:
            db.session.add(otp)
            db.session.commit()
            try:
                msg = Message('Hello {}'.format(otp.username), sender=current_app.config['MAIL_USERNAME'],
                              recipients=[otp.email])
                msg.html = "<h3>Your OTP is:</h3> <h1>" + str(otp.code) + "</h1>"
                mail.send(msg)
                return jsonify({'message': 'OTP sent'}), 200
            except Exception as e:
                db.session.rollback()
                return jsonify({'error': 'OTP mail send failed', 'errors': [e]}), 400
        except Exception as e:
            return jsonify({'error': 'Database error', 'errors': [e]}), 400
    else:
        try:
            jwt_token = encode_auth_token(user_id=user.id, username=user.username, email=user.email, role=user.role,
                                          jwt_secret=current_app.config['JWT_SECRET_KEY'])
            token = Token(token=jwt_token)
            db.session.add(token)
            db.session.commit()
            response = flask.Response(content_type='application/json')
            response.data = json.dumps({'message': 'Login successfully'})
            response.headers["Authorization"] = jwt_token
            return response, 200
        except Exception as e:
            return jsonify({'error': 'Generate token failed', 'errors': [e]})


@userBP.route('/validate-account/<validation_code>', methods=['GET'])
def validate_account(validation_code):
    validate = confirm_token(token=validation_code, secret=current_app.config['JWT_SECRET_KEY'],
                             security_pass=current_app.config['JWT_SECRET_KEY'])
    if validate is False:
        return jsonify({'error': 'Bad link!'}), 400
    search_user = User.get_user_by_identifier(validate)
    if search_user is None:
        return jsonify({'error': 'Unexpected error'}), 400
    if search_user.confirmed is True:
        return jsonify({'error': 'Account is already confirmed'}), 400
    search_user.confirmed = True
    try:
        db.session.commit()
        return jsonify({'message': 'Account was confirmed'}), 200
    except Exception as e:
        return jsonify({'error': 'Database error', 'errors': [e]})


@userBP.route('/validate-otp', methods=['POST'])
@schema.validate(validate_otp_schema)
def validate_otp():
    identifier = request.json['identifier']
    code = request.json['code']
    check_otp = OTP.check_otp(identifier=identifier, code=code)
    if check_otp is True:
        return jsonify({'message': 'OTP OK'}), 200
    elif check_otp is False:
        return jsonify({'error': 'OTP is not valid'}), 400


@userBP.route('/logout', methods=['DELETE'])
def logout():
    blacklist = BlacklistToken(token=request.headers['Authorization'])
    try:
        db.session.add(blacklist)
        db.session.commit()
        return {'message': 'Token was blacklisted!'}, 200
    except Exception as e:
        return jsonify({'error': 'Token blacklisting failed', 'errors': [e]}), 400
