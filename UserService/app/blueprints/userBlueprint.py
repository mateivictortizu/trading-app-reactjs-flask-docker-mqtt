from flask import Blueprint
from datetime import datetime

import flask
from flask import request, jsonify, current_app
from app import db, schema, mail
from app.database.models import User, Token, OTP
from app.json_schema import register_schema, login_schema
from flask_json_schema import JsonValidationError
from flask_mail import Message
from app.myjwt import encode_auth_token

userBP = Blueprint('userBlueprint', __name__)


@userBP.errorhandler(JsonValidationError)
def validator_error(e):
    return jsonify({'error': e.message, 'errors': [validation_error.message for validation_error in e.errors]}), 400


@userBP.route("/register", methods=["POST"])
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
            # TODO Add random code in link to activate account
            msg.html = "<h3> Your activation link is <h3>" + request.base_url
            mail.send(msg)
            return jsonify({'message': 'User registration completed'}), 201
        except Exception as e:
            db.session.rollback()
            return ({'error': 'Confirmation mail send failed', 'errors': [e]}), 400
    except Exception as e:
        return jsonify({'error': 'Database error', 'errors': [e]}), 400


@userBP.route("/login", methods=["POST"])
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
        jwt_token = encode_auth_token(user_id=user.id, username=user.username, email=user.email, role=user.role,
                                      jwt_secret=current_app.config['JWT_SECRET_KEY'])
        token = Token(token=jwt_token)
        db.session.add(token)
        db.session.commit()
        response = flask.Response()
        response.headers["Authorization"] = jwt_token
        return {"jwt": jwt_token}, 200
