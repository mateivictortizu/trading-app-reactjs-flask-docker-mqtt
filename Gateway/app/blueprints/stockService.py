from urllib import parse

from flask import Blueprint, request
import requests

stock = Blueprint('stock', __name__)

URL = "http://127.0.0.1:5001/"


@stock.route('/add-stock', methods=['POST'])
def add_stock():
    json_body = request.json
    headers = request.headers
    r = requests.post(parse.urljoin(URL, "add-stock"), json=json_body, headers=headers)
    return r.content, r.status_code


@stock.route('/get-stock-info/<stock_symbol>', methods=['GET'])
def get_stock_info(stock_symbol):
    headers = request.headers
    r = requests.get(parse.urljoin(URL, "get-stock-info/" + stock_symbol), headers=headers)
    return r.content, r.status_code


@stock.route('/get-stock-price/<stock_symbol>', methods=['GET'])
def get_stock_price(stock_symbol):
    headers = request.headers
    r = requests.get(parse.urljoin(URL, "get-stock-price/"+stock_symbol), headers=headers)
    return r.content, r.status_code


@stock.route('/get-list-stock-price', methods=['POST'])
def get_list_stock_price():
    json_body = request.json
    headers = request.headers
    r = requests.post(parse.urljoin(URL, "get-list-stock-price"), json=json_body, headers=headers)
    return r.content, r.status_code


@stock.route('/update-price', methods=['POST'])
def update_price():
    json_body = request.json
    headers = request.headers
    r = requests.post(parse.urljoin(URL, "update-price"), json=json_body, headers=headers)
    return r.content, r.status_code


@stock.route('/update-stock', methods=['POST'])
def update_stock():
    json_body = request.json
    headers = request.headers
    r = requests.post(parse.urljoin(URL, "update-stock"), json=json_body, headers=headers)
    return r.content, r.status_code


@stock.route('/get-all-stocks', methods=['GET'])
def get_all_stocks():
    headers = request.headers
    r = requests.get(parse.urljoin(URL, "get-all-stocks"), headers=headers)
    return r.content, r.status_code
