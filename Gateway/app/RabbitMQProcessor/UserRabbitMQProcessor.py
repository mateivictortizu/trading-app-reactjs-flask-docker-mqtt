import json

from flask import jsonify, make_response

from app.RabbitMQClients.UserRabbitMQ import CheckTokenClient, RegisterClient, LoginClient, ValidateAccountClient, \
    ResendValidateAccountClient, ValidateOTPClient, ResendOTPClient, LogoutClient, ChangePasswordClient, \
    RequestChangePasswordClient, ResetPassClient, SetNewPassClient, VerifyUserClient, BanClient


def ban_user_processor(ban_client, json_body):
    if ban_client is None:
        ban_client = BanClient()
    try:
        response = json.loads(ban_client.call(json_body))
        return response, response['code']
    except Exception:
        try:
            ban_client = BanClient()
            response = json.loads(ban_client.call(json_body))
            return response, response['code']
        except Exception:
            return jsonify({'error': 'Ban server error', 'code': 500}), 500


def verify_user_processor(verify_user_client, json_body):
    if verify_user_client is None:
        verify_user_client = VerifyUserClient()
    try:
        response = json.loads(verify_user_client.call(json_body))
        return response, response['code']
    except Exception:
        try:
            verify_user_client = VerifyUserClient()
            response = json.loads(verify_user_client.call(json_body))
            return response, response['code']
        except Exception:
            return jsonify({'error': 'Verify user server error', 'code': 500}), 500


def check_token_processor(check_token_client, json_body):
    if check_token_client is None:
        check_token_client = CheckTokenClient()
    try:
        response = json.loads(check_token_client.call(json_body))
        return response, response['code']
    except Exception:
        try:
            check_token_client = CheckTokenClient()
            response = json.loads(check_token_client.call(json_body))
            return response, response['code']
        except Exception:
            return jsonify({'error': 'Check token server error', 'code': 500}), 500


def register_processor(register_client, json_body):
    if register_client is None:
        register_client = RegisterClient()
    try:
        response = json.loads(register_client.call(json_body))
        return response, response['code']
    except Exception:
        try:
            register_client = RegisterClient()
            response = json.loads(register_client.call(json_body))
            return response, response['code']
        except Exception:
            return jsonify({'error': 'Register server error', 'code': 500}), 500


def login_processor(login_client, json_body):
    if login_client is None:
        login_client = LoginClient()
    try:
        response = json.loads(login_client.call(json_body))
        # TODO add auth
        return response, response['code']
    except Exception:
        try:
            login_client = LoginClient()
            response = json.loads(login_client.call(json_body))
            return response, response['code']
        except Exception:
            return jsonify({'error': 'Login server error', 'code': 500}), 500


def validate_account_processor(validate_account_client, json_body):
    if validate_account_client is None:
        validate_account_client = ValidateAccountClient()
    try:
        response = json.loads(validate_account_client.call(json_body))
        return response, response['code']
    except Exception:
        try:
            validate_account_client = ValidateAccountClient()
            response = json.loads(validate_account_client.call(json_body))
            return response, response['code']
        except Exception:
            return jsonify({'error': 'Validate account server error', 'code': 500}), 500


def resend_validate_account_processor(resend_validate_account_client, json_body):
    if resend_validate_account_client is None:
        resend_validate_account_client = ResendValidateAccountClient()
    try:
        response = json.loads(resend_validate_account_client.call(json_body))
        return response, response['code']
    except Exception:
        try:
            resend_validate_account_client = ResendValidateAccountClient()
            response = json.loads(resend_validate_account_client.call(json_body))
            return response, response['code']
        except Exception:
            return jsonify({'error': 'Resend validate account server error', 'code': 500}), 500


def validate_otp_processor(validate_otp_client, json_body):
    if validate_otp_client is None:
        validate_otp_client = ValidateOTPClient()
    try:
        response = json.loads(validate_otp_client.call(json_body))
        resp = make_response(response, response['code'])
        resp.set_cookie('jwt', response['Authorization'], samesite='None', secure=True)
        return resp
    except Exception:
        try:
            validate_otp_client = ValidateOTPClient()
            response = json.loads(validate_otp_client.call(json_body))
            resp = make_response(response, response['code'])
            resp.set_cookie('jwt', response['Authorization'], samesite='None', secure=True)
            return resp
        except Exception:
            return jsonify({'error': 'Validate OTP account server error', 'code': 500}), 500


def resend_otp_processor(resend_otp_client, json_body):
    if resend_otp_client is None:
        resend_otp_client = ResendOTPClient()
    try:
        response = json.loads(resend_otp_client.call(json_body))
        return response, response['code']
    except Exception:
        try:
            resend_otp_client = ResendOTPClient()
            response = json.loads(resend_otp_client.call(json_body))
            return response, response['code']
        except Exception:
            return jsonify({'error': 'Resend OTP server error', 'code': 500}), 500


def logout_processor(logout_client, json_body):
    if logout_client is None:
        logout_client = LogoutClient()
    try:
        response = json.loads(logout_client.call(json_body))
        return response, response['code']
    except Exception:
        try:
            logout_client = LogoutClient()
            response = json.loads(logout_client.call(json_body))
            return response, response['code']
        except Exception:
            return jsonify({'error': 'Logout server error', 'code': 500}), 500


def change_password_processor(change_password_client, json_body):
    if change_password_client is None:
        change_password_client = ChangePasswordClient()
    try:
        response = json.loads(change_password_client.call(json_body))
        return response, response['code']
    except Exception:
        try:
            change_password_client = ChangePasswordClient()
            response = json.loads(change_password_client.call(json_body))
            return response, response['code']
        except Exception:
            return jsonify({'error': 'Change Password server error', 'code': 500}), 500


def request_change_password_processor(request_change_password_client, json_body):
    if request_change_password_client is None:
        request_change_password_client = RequestChangePasswordClient()
    try:
        response = json.loads(request_change_password_client.call(json_body))
        return response, response['code']
    except Exception:
        try:
            request_change_password_client = RequestChangePasswordClient()
            response = json.loads(request_change_password_client.call(json_body))
            return response, response['code']
        except Exception:
            return jsonify({'error': 'Request Change Password server error', 'code': 500}), 500


def reset_pass_processor(reset_pass_client, json_body):
    if reset_pass_client is None:
        reset_pass_client = ResetPassClient()
    try:
        response = json.loads(reset_pass_client.call(json_body))
        return response, response['code']
    except Exception:
        try:
            reset_pass_client = ResetPassClient()
            response = json.loads(reset_pass_client.call(json_body))
            return response, response['code']
        except Exception:
            return jsonify({'error': 'Reset Pass server error', 'code': 500}), 500


def set_new_pass_processor(set_new_pass_client, json_body):
    if set_new_pass_client is None:
        set_new_pass_client = SetNewPassClient()
    try:
        response = json.loads(set_new_pass_client.call(json_body))
        return response, response['code']
    except Exception:
        try:
            set_new_pass_client = SetNewPassClient()
            response = json.loads(set_new_pass_client.call(json_body))
            return response, response['code']
        except Exception:
            return jsonify({'error': 'Set New Pass server error', 'code': 500}), 500
