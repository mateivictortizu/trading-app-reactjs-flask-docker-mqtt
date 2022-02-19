import json

import flask
from flask import jsonify
from flask_mail import Message

from app.database.models import User, OTP, Token, BlacklistToken
from app.myconfirmation import MyConfirmation
from app.myjwt import MyJWT
from app.validator import Validator


def registerDAO(request, current_app, db, mail, username, password, email, name, surname, address, nationality,
                phone, date_of_birth, country):
    email = email.lower()
    username = username.lower()
    if Validator.email_check(email) is False:
        return jsonify({'error': 'Bad email format'}), 400

    if Validator.check_username(username) is False:
        return jsonify({'error': 'Bad username format'}), 400

    if Validator.password_check(password) is False:
        return jsonify({'error': 'Bad password format'}), 400

    if Validator.check_country(country) is False:
        return jsonify({'error': 'Bad country'}), 400

    if Validator.check_nationality(nationality) is False:
        return jsonify({'error': 'Bad nationality'}), 400

    if User.check_if_username_exists(username):
        return jsonify({'error': 'User already exists'}), 409

    if User.check_if_email_exists(email):
        return jsonify({'error': 'Email already exists'}), 409

    user = User(username=username, password=password, email=email, name=name, surname=surname, address=address,
                nationality=nationality, phone=phone, date_of_birth=date_of_birth, country=country)

    User.add_to_user(user)
    # TODO Use Flask-RQ2 to send mail in background
    try:
        msg = Message('Welcome {} {}'.format(user.name, user.surname), sender=current_app.config['MAIL_USERNAME'],
                      recipients=[user.email])
        msg.html = "<h3> Your activation link is <h3>" + request.host_url + 'validate-account/' + \
                   MyConfirmation.generate_confirmation_token(email=user.email,
                                                              secret=current_app.config['JWT_SECRET_KEY'],
                                                              security_pass=current_app.config['JWT_SECRET_KEY'])
        mail.send(msg)
        return jsonify({'message': 'User registration completed'}), 201
    except Exception:
        db.session.rollback()
        return jsonify({'error': 'Confirmation mail send failed'}), 500


def loginDAO(current_app, db, mail, password, identifier):
    identifier = identifier.lower()
    user_checked = User.check_user(password, identifier)
    if user_checked is False or user_checked is None:
        return jsonify({'message': 'User or password is wrong!'}), 401
    user = User.get_user_by_identifier(identifier)
    if user is None:
        return jsonify({'error': 'Unexpected error'}), 500
    if user.confirmed is False:
        return jsonify({'error': 'Please validate your account'}), 400
    if user.twoFA is True:
        otp = OTP(username=user.username, email=user.email)
        OTP.add_to_otp(otp)
        try:
            msg = Message('Hello {}'.format(otp.username), sender=current_app.config['MAIL_USERNAME'],
                          recipients=[otp.email])
            msg.html = "<h3>Your OTP is:</h3> <h1>" + str(otp.code) + "</h1>"
            mail.send(msg)
            return jsonify({'message': 'OTP sent'}), 200
        except Exception:
            db.session.rollback()
            return jsonify({'error': 'OTP mail send failed'}), 500
    elif user.twoFA is False:
        jwt_token = MyJWT.encode_auth_token(user_id=user.id, username=user.username, email=user.email, role=user.role,
                                            jwt_secret=current_app.config['JWT_SECRET_KEY'])
        token = Token(token=jwt_token)
        Token.add_to_token(token)
        response = flask.Response(content_type='application/json')
        response.data = json.dumps({'message': 'Login successfully'})
        response.headers["Authorization"] = jwt_token
        return response, 200


def validate_accountDAO(current_app, db, validation_code):
    validate = MyConfirmation.confirm_token(token=validation_code, secret=current_app.config['JWT_SECRET_KEY'],
                                            security_pass=current_app.config['JWT_SECRET_KEY'])
    if validate is False:
        return jsonify({'error': 'Bad link!'}), 400

    search_user = User.get_user_by_identifier(validate)

    if search_user is None:
        return jsonify({'error': 'Unexpected error'}), 500
    if search_user.confirmed is True:
        return jsonify({'error': 'Account is already confirmed'}), 400
    search_user.confirmed = True
    db.session.commit()
    return jsonify({'message': 'Account was confirmed'}), 200


def resend_validate_accountDAO(request, current_app, mail, identifier):
    identifier = identifier.lower()
    user = User.get_user_by_identifier(identifier=identifier)
    if user is not None:
        if user.confirmed is False:
            try:
                msg = Message('Hello', sender=current_app.config['MAIL_USERNAME'], recipients=[user.email])
                msg.html = "<h3> Your activation link is <h3>" + request.host_url + 'validate-account/' + \
                           MyConfirmation.generate_confirmation_token(email=user.email,
                                                                      secret=current_app.config['JWT_SECRET_KEY'],
                                                                      security_pass=current_app.config[
                                                                          'JWT_SECRET_KEY'])
                mail.send(msg)
                return jsonify({'message': 'User registration completed'}), 201
            except Exception:
                return jsonify({'error': 'Confirmation mail send failed'}), 500
        elif user.confirmed is True:
            return jsonify({'error': 'Account is already confirmed'}), 400
    elif user is None:
        return jsonify({'error': 'Unexpected error'}), 500


def validate_otpDAO(current_app, identifier, code):
    identifier = identifier.lower()
    check_otp = OTP.check_otp(identifier=identifier, code=code)
    if check_otp is True:
        try:
            user = User.get_user_by_identifier(identifier)
            jwt_token = MyJWT.encode_auth_token(user_id=user.id, username=user.username, email=user.email,
                                                role=user.role,
                                                jwt_secret=current_app.config['JWT_SECRET_KEY'])
            token = Token(token=jwt_token)
            Token.add_to_token(token)
            response = flask.Response(content_type='application/json')
            response.data = json.dumps({'message': 'Login successfully'})
            response.headers["Authorization"] = jwt_token
            return response, 200
        except Exception:
            return jsonify({'error': 'OTP OK. Generate token failed'}), 500
    elif check_otp is False:
        return jsonify({'error': 'OTP is not valid'}), 400


def resend_otpDAO(current_app, db, mail, identifier):
    identifier = identifier.lower()
    user = User.get_user_by_identifier(identifier=identifier)
    if user.confirmed is False:
        return jsonify({'error': 'Please validate your account'}), 400
    if user.twoFA is True:
        otp = OTP(username=user.username, email=user.email)
        OTP.add_to_otp(otp)
        try:
            msg = Message('Hello {}'.format(otp.username), sender=current_app.config['MAIL_USERNAME'],
                          recipients=[otp.email])
            msg.html = "<h3>Your OTP is:</h3> <h1>" + str(otp.code) + "</h1>"
            mail.send(msg)
            return jsonify({'message': 'OTP sent'}), 200
        except Exception:
            db.session.rollback()
            return jsonify({'error': 'OTP mail send failed'}), 500
    elif user.twoFA is False:
        return jsonify({'error': 'Unexpected error'}), 500


def logoutDAO(request):
    blacklist = BlacklistToken(token=request.headers['Authorization'])
    BlacklistToken.add_to_blacklist(blacklist=blacklist)
    return jsonify({'message': 'Token was blacklisted!'}), 200


def change_passwordDAO(identifier, password, new_password):
    identifier = identifier.lower()
    if Validator.password_check(new_password) is False:
        return jsonify({'error': 'Bad password format'}), 400
    change_user_pass = User.change_pass(identifier=identifier, password=password, new_password=new_password)
    if change_user_pass is False:
        return jsonify({'error': 'Bad password'}), 400
    elif change_user_pass is True:
        return jsonify({'message': 'Password was changed'}), 200
