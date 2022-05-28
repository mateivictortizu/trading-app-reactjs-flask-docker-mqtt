from urllib import parse

from flask import Blueprint, request
import requests

user = Blueprint('user', __name__)

URL = "http://127.0.0.1:5003/"


@user.route('/ban', methods=['DELETE'])
def ban_user():
    json_body = request.json
    headers = request.headers
    r = requests.delete(parse.urljoin(URL, "ban"), json=json_body, headers=headers)
    return r.content, r.status_code


@user.route('/verify-user', methods=['PUT'])
def verify_user():
    json_body = request.json
    headers = request.headers
    r = requests.put(parse.urljoin(URL, "verify-user"), json=json_body, headers=headers)
    return r.content, r.status_code


@user.route('/check-token', methods=['GET'])
def check_token():
    pass


@user.route('/register', methods=['POST'])
def register():
    json_body = request.json
    headers = request.headers
    r = requests.post(parse.urljoin(URL, "register"), json=json_body, headers=headers)
    return r.content, r.status_code


@user.route('/login', methods=['POST'])
def login():
    json_body = request.json
    headers = request.headers
    r = requests.post(parse.urljoin(URL, "login"), json=json_body, headers=headers)
    return r.content, r.status_code


@user.route('/validate-account/<validation_code>', methods=['GET'])
def validate_account(validation_code):
    headers = request.headers
    r = requests.get(parse.urljoin(URL, "validate-account/"+validation_code), headers=headers)
    return r.content, r.status_code


@user.route('/resend-validate-account', methods=['POST'])
def resend_validate_account():
    json_body = request.json
    headers = request.headers
    r = requests.post(parse.urljoin(URL, "resend-validate-account"), json=json_body, headers=headers)
    return r.content, r.status_code


@user.route('/validate-otp', methods=['POST'])
def validate_otp():
    json_body = request.json
    headers = request.headers
    r = requests.post(parse.urljoin(URL, "validate-otp"), json=json_body, headers=headers)
    return r.content, r.status_code


@user.route('/resend-otp', methods=['POST'])
def resend_otp():
    json_body = request.json
    headers = request.headers
    r = requests.post(parse.urljoin(URL, "resend-otp"), json=json_body, headers=headers)
    return r.content, r.status_code


@user.route('/logout', methods=['DELETE'])
def logout():
    json_body = request.json
    headers = request.headers
    r = requests.delete(parse.urljoin(URL, "logout"), json=json_body, headers=headers)
    return r.content, r.status_code


@user.route('/change-password', methods=['PUT'])
def change_password():
    json_body = request.json
    headers = request.headers
    r = requests.put(parse.urljoin(URL, "change-password"), json=json_body, headers=headers)
    return r.content, r.status_code


@user.route('/request-change-password', methods=['POST'])
def request_change_password():
    json_body = request.json
    headers = request.headers
    r = requests.post(parse.urljoin(URL, "request-change-password"), json=json_body, headers=headers)
    return r.content, r.status_code


@user.route('/reset-pass/<reset_code>', methods=['GET'])
def reset_pass(reset_code):
    headers = request.headers
    r = requests.get(parse.urljoin(URL, "reset-pass/" + reset_code), headers=headers)
    return r.content, r.status_code


@user.route('/set-new-pass', methods=['POST'])
def set_new_pass():
    json_body = request.json
    headers = request.headers
    r = requests.post(parse.urljoin(URL, "set-new-pass"), json=json_body, headers=headers)
    return r.content, r.status_code
