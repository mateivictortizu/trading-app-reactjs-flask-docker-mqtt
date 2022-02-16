from datetime import datetime
from flask import request, jsonify
from app import app, db, schema
from app.models import User
from app.json_schema import register_schema
from flask_json_schema import JsonValidationError


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
        return 'User already exists', 409
    if User.check_if_email_exists(email):
        return 'Email already exists', 409
    user = User(username=username, password=password, email=email, date_of_birth=date_of_birth, country=country)
    db.session.add(user)
    db.session.commit()

    return 'User registration completed', 201
