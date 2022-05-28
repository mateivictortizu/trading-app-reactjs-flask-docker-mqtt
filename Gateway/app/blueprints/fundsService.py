from urllib import parse

from flask import Blueprint, request
import requests

funds = Blueprint('funds', __name__)

URL = "http://127.0.0.1:5002/"


@funds.route('/add-money', methods=['POST'])
def add_money():
    json_body = request.json
    headers = request.headers
    r = requests.post(parse.urljoin(URL, "add-money"), json=json_body, headers=headers)
    return r.content, r.status_code


@funds.route('/withdraw-money', methods=['POST'])
def withdraw_money():
    json_body = request.json
    headers = request.headers
    r = requests.post(parse.urljoin(URL, "withdraw-money"), json=json_body, headers=headers)
    return r.content, r.status_code


@funds.route('/get-funds/<user>')
def get_funds(user):
    headers = request.headers
    r = requests.get(parse.urljoin(URL, "get-funds/"+user), headers=headers)
    return r.content, r.status_code
