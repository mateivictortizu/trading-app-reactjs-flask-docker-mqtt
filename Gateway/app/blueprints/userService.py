from flask import Blueprint, request, session

from app.RabbitMQProcessor.UserRabbitMQProcessor import check_token_processor, register_processor, \
    validate_account_processor, login_processor, resend_validate_account_processor, validate_otp_processor, \
    resend_otp_processor, logout_processor, change_password_processor, request_change_password_processor, \
    reset_pass_processor, set_new_pass_processor, verify_user_processor, ban_user_processor
from app.blueprints import ban_client, verify_user_client, check_token_client, register_client, login_client, \
    validate_account_client, resend_validate_account_client, validate_otp_client, resend_otp_client, logout_client, \
    change_password_client, request_change_password_client, reset_pass_client, set_new_pass_client

user = Blueprint('user', __name__)


@user.route('/ban', methods=['DELETE'])
def ban_user():
    return ban_user_processor(ban_client, request.json)


@user.route('/verify-user', methods=['PUT'])
def verify_user():
    return verify_user_processor(verify_user_client, request.json)


@user.route('/check-token', methods=['GET'])
def check_token():
    return check_token_processor(check_token_client, {'jwt': 'Ok'})


@user.route('/register', methods=['POST'])
def register():
    return register_processor(register_client, request.json)


@user.route('/login', methods=['POST'])
def login():
    return login_processor(login_client, request.json)


@user.route('/validate-account/<validation_code>', methods=['GET'])
def validate_account(validation_code):
    return validate_account_processor(validate_account_client, {'validation_code': validation_code})


@user.route('/resend-validate-account', methods=['POST'])
def resend_validate_account():
    return resend_validate_account_processor(resend_validate_account_client, request.json)


@user.route('/validate-otp', methods=['POST'])
def validate_otp():
    return validate_otp_processor(validate_otp_client, request.json)


@user.route('/resend-otp', methods=['POST'])
def resend_otp():
    return resend_otp_processor(resend_otp_client, request.json)


@user.route('/logout', methods=['DELETE'])
def logout():
    session.pop('user_id', None)
    return logout_processor(logout_client, request.json)


@user.route('/change-password', methods=['PUT'])
def change_password():
    return change_password_processor(change_password_client, request.json)


@user.route('/request-change-password', methods=['POST'])
def request_change_password():
    return request_change_password_processor(request_change_password_client, request.json)


@user.route('/reset-pass/<reset_code>', methods=['GET'])
def reset_pass(reset_code):
    return reset_pass_processor(reset_pass_client, {"reset_code": reset_code})


@user.route('/set-new-pass', methods=['POST'])
def set_new_pass():
    return set_new_pass_processor(set_new_pass_client, request.json)
