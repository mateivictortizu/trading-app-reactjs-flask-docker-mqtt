import json
from urllib import parse
import requests
import pika

URL = "http://127.0.0.1:5005/"


def on_request_buy(ch, method, props, body):
    json_body = json.loads(body)
    r = requests.post(parse.urljoin(URL, "buy"), json=json_body)
    response = {}
    if r.status_code == 200 or r.status_code == 201 or r.status_code == 401:
        json_obj = json.loads(r.content)
        response = json_obj
    else:
        try:
            response = json.loads(r.content)
        except Exception:
            response["message"] = "Buy fails"
    response["code"] = r.status_code
    response = json.dumps(response)
    print(response)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


def on_request_sell(ch, method, props, body):
    json_body = json.loads(body)
    r = requests.post(parse.urljoin(URL, "sell"), json=json_body)
    response = {}
    if r.status_code == 200 or r.status_code == 201 or r.status_code == 401:
        json_obj = json.loads(r.content)
        response = json_obj
    else:
        try:
            response = json.loads(r.content)
        except Exception:
            response["message"] = "Sell fails"
    response["code"] = r.status_code
    response = json.dumps(response)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=response)
    ch.basic_ack(delivery_tag=method.delivery_tag)


def on_get_invest_by_user(ch, method, props, body):
    json_body = json.loads(body)
    r = requests.post(parse.urljoin(URL, "get-invest-by-user"), json=json_body)
    response = {}
    if r.status_code == 200 or r.status_code == 201 or r.status_code == 401:
        json_obj = json.loads(r.content)
        response = json_obj
    else:
        try:
            response = json.loads(r.content)
        except Exception:
            response["message"] = "Get Stock Invest by user fail"
    response["code"] = r.status_code
    response = json.dumps(response)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=response)
    ch.basic_ack(delivery_tag=method.delivery_tag)


def on_stock_invest_by_user(ch, method, props, body):
    json_body = json.loads(body)
    r = requests.post(parse.urljoin(URL, "get-stock-invest-by-user"), json=json_body)
    response = {}
    if r.status_code == 200 or r.status_code == 201 or r.status_code == 401:
        json_obj = json.loads(r.content)
        response = json_obj
    else:
        try:
            response = json.loads(r.content)
        except Exception:
            response["message"] = "Get Stock Invest by user fail"
    response["code"] = r.status_code
    response = json.dumps(response)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=response)
    ch.basic_ack(delivery_tag=method.delivery_tag)


def start():
    print('Invest RabbitMQ Server start...')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))

    channel = connection.channel()

    channel.queue_declare(queue='buy_queue')
    channel.queue_declare(queue='sell_queue')
    channel.queue_declare(queue='get_all_invest_by_user')
    channel.queue_declare(queue='get_stock_invest_by_user')

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='buy_queue', on_message_callback=on_request_buy)
    channel.basic_consume(queue='sell_queue', on_message_callback=on_request_sell)
    channel.basic_consume(queue='get_all_invest_by_user', on_message_callback=on_get_invest_by_user)
    channel.basic_consume(queue='get_stock_invest_by_user', on_message_callback=on_stock_invest_by_user)
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print('Invest RabbitMQ Server down.')


if __name__ == '__main__':
    start()
