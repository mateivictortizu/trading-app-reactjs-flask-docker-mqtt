import json
import os
import flask
from flask import jsonify
from flask_mail import Message

from app.database.models import User, OTP, Token, OTPToken, ChangePassToken
from app.utils.myconfirmation import MyConfirmation
from app.utils.myjwt import MyJWT
from app.utils.validator import Validator


def send_email(current_app, mail, to, subject, message_html):
    msg = Message(subject, sender=current_app.config['MAIL_USERNAME'], recipients=to)
    msg.html = message_html
    mail.send(msg)


def registerDAO(executor, request, current_app, db, mail, username, password, email, name, surname, address,
                nationality, phone, date_of_birth, country, hostname, port):
    email = email.lower()
    username = username.lower()
    if Validator.email_check(email) is False:
        db.session.remove()
        return jsonify({'error': 'Bad email format'}), 400

    if Validator.check_username(username) is False:
        db.session.remove()
        return jsonify({'error': 'Bad username format'}), 400

    if Validator.password_check(password) is False:
        db.session.remove()
        return jsonify({'error': 'Bad password format'}), 400

    if Validator.check_country(country) is False:
        db.session.remove()
        return jsonify({'error': 'Bad country'}), 400

    if Validator.check_nationality(nationality) is False:
        db.session.remove()
        return jsonify({'error': 'Bad nationality'}), 400

    if User.check_if_username_exists(username):
        db.session.remove()
        print('Username exists')
        return jsonify({'error': 'User already exists'}), 409

    if User.check_if_email_exists(email):
        db.session.remove()
        print('Email exists')
        return jsonify({'error': 'Email already exists'}), 409

    if User.check_if_phone_exists(phone):
        db.session.remove()
        print('Phone exists')
        return jsonify({'error': 'Phone already exists'}), 409

    user = User(username=username, password=password, email=email, name=name, surname=surname, address=address,
                nationality=nationality, phone=phone, date_of_birth=date_of_birth, country=country)

    User.add_to_user(user)
    try:
        message_html = "<h3> Your activation link is <h3>" + hostname+':'+port+'/' + 'validate-account/' + \
                       MyConfirmation.generate_confirmation_token(email=user.email,
                                                                  secret=current_app.config['JWT_SECRET_KEY'],
                                                                  security_pass=current_app.config['JWT_SECRET_KEY'])
        executor.submit(send_email, current_app, mail, [user.email], 'Welcome {} {}'.format(user.name, user.surname),
                        message_html)
        db.session.remove()
        return jsonify({'message': 'User registration completed'}), 201
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify({'error': 'Confirmation mail send failed'}), 500


def loginDAO(executor, current_app, db, mail, password, identifier):
    identifier = identifier.lower()
    if User.check_if_banned(identifier):
        db.session.remove()
        return jsonify({'error': 'User is banned'}), 403
    user_checked = User.check_user(password, identifier)
    if user_checked is False or user_checked is None:
        db.session.remove()
        return jsonify({'message': 'User or password is wrong!'}), 401
    user = User.get_user_by_identifier(identifier)
    if user is None:
        db.session.remove()
        return jsonify({'error': 'Unexpected error'}), 500
    if user.confirmed is False:
        db.session.remove()
        return jsonify({'error': 'Please validate your account'}), 400
    if user.twoFA is True:
        otp = OTP(username=user.username, email=user.email)
        OTP.add_to_otp(otp)
        try:
            print(otp.code)
            message_html = "<h3>Your OTP is:</h3> <h1>" + str(otp.code) + "</h1>"
            executor.submit(send_email, current_app, mail, [otp.email],
                            'Hello {}'.format(otp.username), message_html)
            otp_token = MyJWT.encode_OTP_token(username=otp.username, jwt_secret=current_app.config['JWT_SECRET_KEY'])
            token = OTPToken(token=otp_token)
            OTPToken.add_to_token(token)
            response = flask.Response(content_type='application/json')
            response.data = json.dumps({'message': 'OTP send'})
            response.headers['Authorization'] = otp_token
            db.session.remove()
            return response, 200

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
        response.headers['Authorization'] = jwt_token
        db.session.remove()
        return response, 200


def validate_accountDAO(current_app, db, validation_code):
    validate = MyConfirmation.confirm_token(token=validation_code, secret=current_app.config['JWT_SECRET_KEY'],
                                            security_pass=current_app.config['JWT_SECRET_KEY'])
    if validate is False:
        return jsonify({'error': 'Expired link!'}), 400

    if User.check_if_banned(validate):
        db.session.remove()
        return jsonify({'error': 'User is banned'}), 403

    search_user = User.get_user_by_identifier(validate)

    if search_user is None:
        db.session.remove()
        return jsonify({'error': 'Unexpected error'}), 500
    if search_user.confirmed is True:
        db.session.remove()
        return jsonify({'error': 'Account is already confirmed'}), 400
    search_user.confirmed = True
    try:
        pass
    except Exception:
        return jsonify({'error': 'Error in create account'}), 400
    db.session.commit()
    db.session.remove()
    return jsonify({'message': 'Account was confirmed'}), 200


def resend_validate_accountDAO(executor, request, current_app, db, mail, identifier):
    identifier = identifier.lower()
    if User.check_if_banned(identifier):
        db.session.remove()
        return jsonify({'error': 'User is banned'}), 403
    user = User.get_user_by_identifier(identifier=identifier)
    db.session.remove()
    if user is not None:
        if user.confirmed is False:
            try:
                message_html = "<h3> Your activation link is <h3>" + request.host_url + 'validate-account/' + \
                               MyConfirmation.generate_confirmation_token(email=user.email,
                                                                          secret=current_app.config['JWT_SECRET_KEY'],
                                                                          security_pass=current_app.config[
                                                                              'JWT_SECRET_KEY'])
                executor.submit(send_email, current_app, mail, [user.email],
                                'Hello {} {}'.format(user.name, user.surname), message_html)
                return jsonify({'message': 'User registration completed'}), 201
            except Exception:
                return jsonify({'error': 'Confirmation mail send failed'}), 500
        elif user.confirmed is True:
            return jsonify({'error': 'Account is already confirmed'}), 400
    elif user is None:
        return jsonify({'error': 'Unexpected error'}), 500


def validate_otpDAO(current_app, db, otp_jwt, code):
    if OTPToken.check_token(otp_jwt) is False:
        db.session.remove()
        return jsonify({'error': 'Invalid token'}), 403
    decoded_otp_jwt = MyJWT.decode_OTP_token(auth_token=otp_jwt, jwt_secret=current_app.config['JWT_SECRET_KEY'])
    if decoded_otp_jwt[0] == -1 or decoded_otp_jwt[0] == -2:
        db.session.remove()
        return jsonify({'error': 'Token {}'.format(decoded_otp_jwt[1])}), 403
    identifier = decoded_otp_jwt.lower()
    if User.check_if_banned(identifier):
        db.session.remove()
        return jsonify({'error': 'User is banned'}), 403
    check_otp = OTP.check_otp(identifier=identifier, code=code)
    if check_otp is True:
        try:
            user = User.get_user_by_identifier(identifier)
            jwt_token = MyJWT.encode_auth_token(user_id=user.id, username=user.username, email=user.email,
                                                role=user.role,
                                                jwt_secret=current_app.config['JWT_SECRET_KEY'])
            token = Token(token=jwt_token)
            Token.add_to_token(token)
            OTP.delete_all_otp_from_identifier(user.username)
            OTPToken.delete_otp_token(otp_jwt)
            response = flask.Response(content_type='application/json')
            response.data = json.dumps({'message': 'Login successfully'})
            response.headers["Authorization"] = jwt_token
            db.session.remove()
            return response, 200
        except Exception:
            return jsonify({'error': 'OTP OK. Generate token failed'}), 500
    elif check_otp is False:
        OTP.increment_no_of_tries(identifier)
        db.session.remove()
        return jsonify({'error': 'OTP is not valid'}), 400


def resend_otpDAO(executor, current_app, db, mail, otp_jwt):
    if OTPToken.check_token(otp_jwt) is False:
        db.session.remove()
        return jsonify({'error': 'Invalid token'}), 403
    decoded_otp_jwt = MyJWT.decode_OTP_token(auth_token=otp_jwt, jwt_secret=current_app.config['JWT_SECRET_KEY'])
    if decoded_otp_jwt[0] == -1 or decoded_otp_jwt[0] == -2:
        db.session.remove()
        return jsonify({'error': 'Token {}'.format(decoded_otp_jwt[1])}), 403
    identifier = decoded_otp_jwt.lower()
    if User.check_if_banned(identifier):
        db.session.remove()
        return jsonify({'error': 'User is banned'}), 403
    user = User.get_user_by_identifier(identifier=identifier)
    if user.confirmed is False:
        db.session.remove()
        return jsonify({'error': 'Please validate your account'}), 400
    if user.twoFA is True:
        OTP.delete_all_otp_from_identifier(user.username)
        otp = OTP(username=user.username, email=user.email)
        OTP.add_to_otp(otp)
        try:
            message_html = "<h3>Your OTP is:</h3> <h1>" + str(otp.code) + "</h1>"
            executor.submit(send_email, current_app, mail, [otp.email], 'Hello {}'.format(otp.username), message_html)
            db.session.remove()
            return jsonify({'message': 'OTP sent'}), 200
        except Exception:
            db.session.rollback()
            return jsonify({'error': 'OTP mail send failed'}), 500
    elif user.twoFA is False:
        db.session.remove()
        return jsonify({'error': 'Unexpected error'}), 500


def logoutDAO(request, db):
    blacklist = Token.blacklisted_token(auth_token=request.headers['Authorization'])
    if blacklist is True:
        db.session.remove()
        return jsonify({'message': 'Token was blacklisted!'}), 200
    else:
        db.session.remove()
        return jsonify({'message': 'Token was not blacklisted!'}), 400


def change_passwordDAO(identifier, db, password, new_password):
    identifier = identifier.lower()
    if User.check_if_banned(identifier):
        db.session.remove()
        return jsonify({'error': 'User is banned'}), 403
    if Validator.password_check(new_password) is False:
        db.session.remove()
        return jsonify({'error': 'Bad password format'}), 400
    change_user_pass = User.change_pass(identifier=identifier, password=password, new_password=new_password)
    if change_user_pass is False:
        db.session.remove()
        return jsonify({'error': 'Bad password'}), 400
    elif change_user_pass is True:
        db.session.remove()
        return jsonify({'message': 'Password was changed'}), 200


def request_change_passwordDAO(executor, current_app, mail, db, identifier):
    identifier = identifier.lower()
    user = User.get_user_by_identifier(identifier=identifier)
    if user is None:
        return jsonify({'error': 'User did not exists'}), 400

    link = MyConfirmation.generate_confirmation_token(email=user.email,
                                                      secret=current_app.config['JWT_SECRET_KEY'],
                                                      security_pass=current_app.config['JWT_SECRET_KEY'])
    token = ChangePassToken(str(link))
    ChangePassToken.add_to_token(token)
    try:
        message_html = "<h3> Your reset password link is <h3>" + 'http://127.0.0.1:5000/reset-pass/' + \
                       link
        executor.submit(send_email, current_app, mail, [user.email], 'Reset password link',
                        message_html)
        db.session.remove()
        return jsonify({'message': 'Reset password link send'}), 200
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify({'error': 'Reset password link failed'}), 500


def reset_passDAO(reset_code, current_app):
    check = ChangePassToken.check_token(reset_code)
    if check is False:
        return jsonify({'error': 'Token invalid or expired'}), 404
    identifier = MyConfirmation.confirm_token(reset_code, secret=current_app.config['JWT_SECRET_KEY'],
                                              security_pass=current_app.config['JWT_SECRET_KEY'])
    if identifier:
        return jsonify({'message': identifier}), 200
    else:
        return jsonify({'error': 'Token invalid or expired'}), 404


def set_new_passDAO(changePassToken, password, current_app, db):
    identifier = MyConfirmation.confirm_token(changePassToken, secret=current_app.config['JWT_SECRET_KEY'],
                                              security_pass=current_app.config['JWT_SECRET_KEY'])
    if identifier:
        if Validator.password_check(password) is False:
            db.session.remove()
            return jsonify({'error': 'Bad password format'}), 400
        change_user_pass = User.reset_pass(identifier, password)
        ChangePassToken.delete_change_pass_token(changePassToken)
        return jsonify({'message': 'Password was changed'}), 200
    else:
        return jsonify({'error': 'Bad token or expired'}), 404
