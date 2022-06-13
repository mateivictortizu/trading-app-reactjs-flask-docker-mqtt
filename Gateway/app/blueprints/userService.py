import json

from flask import Blueprint, request, jsonify

from app.RabbitMQClients.UserRabbitMQ import ResendOTPClient, BanClient, VerifyUserClient, CheckTokenClient, \
    RegisterClient, LoginClient, ResendValidateAccountClient, ValidateOTPClient, LogoutClient, ChangePasswordClient, \
    RequestChangePasswordClient, ResetPassClient, SetNewPassClient

user = Blueprint('user', __name__)

URL = "http://127.0.0.1:5003/"

ban_client = None
verify_user_client = None
check_token_client = None
register_client = None
login_client = None
validate_account_client = None
resend_validate_account_client = None
validate_otp_client = None
resend_otp_client = None
logout_client = None
change_password_client = None
request_change_password_client = None
reset_pass_client = None
set_new_pass_client = None


@user.route('/ban', methods=['DELETE'])
def ban_user():
    global ban_client
    if ban_client is None:
        ban_client = BanClient()
    try:
        response = json.loads(ban_client.call(request.json))
        return response, response['code']
    except Exception:
        try:
            ban_client = BanClient()
            response = json.loads(ban_client.call(request.json))
            return response, response['code']
        except Exception:
            return jsonify({'error': 'Ban server error', 'code': 500}), 500


@user.route('/verify-user', methods=['PUT'])
def verify_user():
    global verify_user_client
    if verify_user_client is None:
        verify_user_client = VerifyUserClient()
    try:
        response = json.loads(verify_user_client.call(request.json))
        return response, response['code']
    except Exception:
        try:
            verify_user_client = VerifyUserClient()
            response = json.loads(verify_user_client.call(request.json))
            return response, response['code']
        except Exception:
            return jsonify({'error': 'Verify user server error', 'code': 500}), 500


@user.route('/check-token', methods=['GET'])
def check_token():
    global check_token_client
    if check_token_client is None:
        check_token_client = CheckTokenClient()
    try:
        response = json.loads(check_token_client.call(request.json))
        return response, response['code']
    except Exception:
        try:
            check_token_client = CheckTokenClient()
            response = json.loads(check_token_client.call(request.json))
            return response, response['code']
        except Exception:
            return jsonify({'error': 'Check token server error', 'code': 500}), 500


@user.route('/register', methods=['POST'])
def register():
    global register_client
    if register_client is None:
        register_client = RegisterClient()
    try:
        response = json.loads(register_client.call(request.json))
        return response, response['code']
    except Exception:
        try:
            register_client = RegisterClient()
            response = json.loads(register_client.call(request.json))
            return response, response['code']
        except Exception:
            return jsonify({'error': 'Register server error', 'code': 500}), 500


@user.route('/login', methods=['POST'])
def login():
    global login_client
    if login_client is None:
        login_client = LoginClient()
    try:
        response = json.loads(login_client.call(request.json))
        return response, response['code']
    except Exception:
        try:
            login_client = LoginClient()
            response = json.loads(login_client.call(request.json))
            return response, response['code']
        except Exception:
            return jsonify({'error': 'Login server error', 'code': 500}), 500


@user.route('/validate-account/<validation_code>', methods=['GET'])
def validate_account(validation_code):
    global validate_account_client
    if validate_account_client is None:
        validate_account_client = LoginClient()
    try:
        response = json.loads(validate_account_client.call({'validation_code': validation_code}))
        return response, response['code']
    except Exception:
        try:
            validate_account_client = LoginClient()
            response = json.loads(validate_account_client.call({'validation_code': validation_code}))
            return response, response['code']
        except Exception:
            return jsonify({'error': 'Validate account server error', 'code': 500}), 500


@user.route('/resend-validate-account', methods=['POST'])
def resend_validate_account():
    global resend_validate_account_client
    if resend_validate_account_client is None:
        resend_validate_account_client = ResendValidateAccountClient()
    try:
        response = json.loads(resend_validate_account_client.call(request.json))
        return response, response['code']
    except Exception:
        try:
            resend_validate_account_client = ResendValidateAccountClient()
            response = json.loads(resend_validate_account_client.call(request.json))
            return response, response['code']
        except Exception:
            return jsonify({'error': 'Resend validate account server error', 'code': 500}), 500


@user.route('/validate-otp', methods=['POST'])
def validate_otp():
    global validate_otp_client
    if validate_otp_client is None:
        validate_otp_client = ValidateOTPClient()
    try:
        response = json.loads(validate_otp_client.call(request.json))
        return response, response['code']
    except Exception:
        try:
            validate_otp_client = ValidateOTPClient()
            response = json.loads(validate_otp_client.call(request.json))
            return response, response['code']
        except Exception:
            return jsonify({'error': 'Validate OTP account server error', 'code': 500}), 500


@user.route('/resend-otp', methods=['POST'])
def resend_otp():
    global resend_otp_client
    if resend_otp_client is None:
        resend_otp_client = ResendOTPClient()
    try:
        response = json.loads(resend_otp_client.call(request.json))
        return response, response['code']
    except Exception:
        try:
            resend_otp_client = ResendOTPClient()
            response = json.loads(resend_otp_client.call(request.json))
            return response, response['code']
        except Exception:
            return jsonify({'error': 'Resend OTP server error', 'code': 500}), 500


@user.route('/logout', methods=['DELETE'])
def logout():
    global logout_client
    if logout_client is None:
        logout_client = LogoutClient()
    try:
        response = json.loads(logout_client.call(request.json))
        return response, response['code']
    except Exception:
        try:
            logout_client = LogoutClient()
            response = json.loads(logout_client.call(request.json))
            return response, response['code']
        except Exception:
            return jsonify({'error': 'Logout server error', 'code': 500}), 500


@user.route('/change-password', methods=['PUT'])
def change_password():
    global change_password_client
    if change_password_client is None:
        change_password_client = ChangePasswordClient()
    try:
        response = json.loads(change_password_client.call(request.json))
        return response, response['code']
    except Exception:
        try:
            change_password_client = ChangePasswordClient()
            response = json.loads(change_password_client.call(request.json))
            return response, response['code']
        except Exception:
            return jsonify({'error': 'Change Password server error', 'code': 500}), 500


@user.route('/request-change-password', methods=['POST'])
def request_change_password():
    global request_change_password_client
    if request_change_password_client is None:
        request_change_password_client = RequestChangePasswordClient()
    try:
        response = json.loads(request_change_password_client.call(request.json))
        return response, response['code']
    except Exception:
        try:
            request_change_password_client = RequestChangePasswordClient()
            response = json.loads(request_change_password_client.call(request.json))
            return response, response['code']
        except Exception:
            return jsonify({'error': 'Request Change Password server error', 'code': 500}), 500


@user.route('/reset-pass/<reset_code>', methods=['GET'])
def reset_pass(reset_code):
    global reset_pass_client
    if reset_pass_client is None:
        reset_pass_client = ResetPassClient()
    try:
        response = json.loads(reset_pass_client.call({"reset_code": reset_code}))
        return response, response['code']
    except Exception:
        try:
            reset_pass_client = ResetPassClient()
            response = json.loads(reset_pass_client.call({"reset_code": reset_code}))
            return response, response['code']
        except Exception:
            return jsonify({'error': 'Reset Pass server error', 'code': 500}), 500


@user.route('/set-new-pass', methods=['POST'])
def set_new_pass():
    global set_new_pass_client
    if set_new_pass_client is None:
        set_new_pass_client = SetNewPassClient()
    try:
        response = json.loads(set_new_pass_client.call(request.json))
        return response, response['code']
    except Exception:
        try:
            set_new_pass_client = SetNewPassClient()
            response = json.loads(set_new_pass_client.call(request.json))
            return response, response['code']
        except Exception:
            return jsonify({'error': 'Set New Pass server error', 'code': 500}), 500
