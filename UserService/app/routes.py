from datetime import datetime
from flask import request, jsonify
from app import app, db, schema, mail
from app.models import User
from app.json_schema import register_schema, login_schema
from flask_json_schema import JsonValidationError
from flask_mail import Message

from app.otp import OTP


@app.errorhandler(JsonValidationError)
def validator_error(e):
    return jsonify({'error': e.message, 'errors': [validation_error.message for validation_error in e.errors]}), 400


@app.route("/register", methods=["POST"])
@schema.validate(register_schema)
def register():
    username = request.json['username']
    password = request.json['password']
    email = request.json['email']
    date_of_birth_str = request.json['date_of_birth']
    date_of_birth = datetime.strptime(date_of_birth_str, '%Y-%m-%d')
    country = request.json['country']
    if User.check_if_username_exists(username):
        return jsonify('User already exists'), 409
    if User.check_if_email_exists(email):
        return jsonify('Email already exists'), 409
    user = User(username=username, password=password, email=email, date_of_birth=date_of_birth, country=country)
    db.session.add(user)
    db.session.commit()
    return jsonify('User registration completed'), 201


@app.route("/login", methods=["POST"])
@schema.validate(login_schema)
def login():
    identifier = request.json['identifier']
    password = request.json['password']
    user_checked = User.check_user(password, identifier)
    if user_checked is False or user_checked is None:
        return jsonify({'message': 'User or password is wrong!'}), 401
    user = User.get_user_by_identifier(identifier)
    otp = OTP(destination=user.email)
    msg = Message('Hello', sender='tizu.licenta@gmail.com', recipients=['matteovkt@gmail.com'])
    msg.html = "<h3>Your OTP is:</h3> <h1>"+str(otp.code)+"</h1>"
    try:
        mail.send(msg)
        return jsonify({'message': 'OTP sent'}), 200
    except Exception as e:
        return jsonify({'error': e}), 400
