import json
import os
from urllib import parse
import requests
import pika

URL = 'http://' + os.environ.get('INVEST_MICROSERVICE', '127.0.0.1:5005') + '/'
RABBIT_MQ_HOST = os.environ.get('RABBITMQ_HOST', 'localhost')


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


def on_history_stock_user(ch, method, props, body):
    json_body = json.loads(body)
    r = requests.post(parse.urljoin(URL, "get-history-stock-user"), json=json_body)
    response = {}
    if r.status_code == 200 or r.status_code == 201 or r.status_code == 401:
        json_obj = json.loads(r.content)
        response = json_obj
    else:
        try:
            response = json.loads(r.content)
        except Exception:
            response["message"] = "Get History Stock Invest by user fail"
    response["code"] = r.status_code
    response = json.dumps(response)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=response)
    ch.basic_ack(delivery_tag=method.delivery_tag)


def on_all_history_user(ch, method, props, body):
    json_body = json.loads(body)
    r = requests.post(parse.urljoin(URL, "get-all-history-user"), json=json_body)
    response = {}
    if r.status_code == 200 or r.status_code == 201 or r.status_code == 401:
        json_obj = json.loads(r.content)
        response = json_obj
    else:
        try:
            response = json.loads(r.content)
        except Exception:
            response["message"] = "Get All History Invest by user fail"
    response["code"] = r.status_code
    response = json.dumps(response)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=response)
    ch.basic_ack(delivery_tag=method.delivery_tag)


def on_value_of_account(ch, method, props, body):
    json_body = json.loads(body)
    r = requests.get(parse.urljoin(URL, "get-value-of-user-account"), json=json_body)
    response = {}
    if r.status_code == 200 or r.status_code == 201 or r.status_code == 401:
        json_obj = json.loads(r.content)
        response = json_obj
    else:
        try:
            response = json.loads(r.content)
        except Exception:
            response["message"] = "Get Value of Account User fail"
    response["code"] = r.status_code
    response = json.dumps(response)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=response)
    ch.basic_ack(delivery_tag=method.delivery_tag)


def on_detailed_user(ch, method, props, body):
    json_body = json.loads(body)
    r = requests.get(parse.urljoin(URL, "get-detailed-stock-invest"), json=json_body)
    response = {}
    if r.status_code == 200 or r.status_code == 201 or r.status_code == 401:
        json_obj = json.loads(r.content)
        response = json_obj
    else:
        try:
            response = json.loads(r.content)
        except Exception:
            response["message"] = "Get Detailed User fail"
    response["code"] = r.status_code
    response = json.dumps(response)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=response)
    ch.basic_ack(delivery_tag=method.delivery_tag)


def on_request_autobuy(ch, method, props, body):
    json_body = json.loads(body)
    r = requests.post(parse.urljoin(URL, "autobuy"), json=json_body)
    response = {}
    if r.status_code == 200 or r.status_code == 201 or r.status_code == 401:
        json_obj = json.loads(r.content)
        response = json_obj
    else:
        try:
            response = json.loads(r.content)
        except Exception:
            response["message"] = "AutoBuy fails"
    response["code"] = r.status_code
    response = json.dumps(response)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


def on_request_autosell(ch, method, props, body):
    json_body = json.loads(body)
    r = requests.post(parse.urljoin(URL, "autosell"), json=json_body)
    response = {}
    if r.status_code == 200 or r.status_code == 201 or r.status_code == 401:
        json_obj = json.loads(r.content)
        response = json_obj
    else:
        try:
            response = json.loads(r.content)
        except Exception:
            response["message"] = "AutoSell fails"
    response["code"] = r.status_code
    response = json.dumps(response)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=response)
    ch.basic_ack(delivery_tag=method.delivery_tag)


def on_request_remove_autoinvest(ch, method, props, body):
    json_body = json.loads(body)
    r = requests.delete(parse.urljoin(URL, "remove-autoinvest"), json=json_body)
    response = {}
    if r.status_code == 200 or r.status_code == 201 or r.status_code == 401:
        json_obj = json.loads(r.content)
        response = json_obj
    else:
        try:
            response = json.loads(r.content)
        except Exception:
            response["message"] = "Remove AutoInvest fails"
    response["code"] = r.status_code
    response = json.dumps(response)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=response)
    ch.basic_ack(delivery_tag=method.delivery_tag)


def on_request_pending_autoinvest(ch, method, props, body):
    json_body = json.loads(body)
    r = requests.post(parse.urljoin(URL, "get-autoinvest-stock-user"), json=json_body)
    response = {}
    if r.status_code == 200 or r.status_code == 201 or r.status_code == 401:
        json_obj = json.loads(r.content)
        response = json_obj
    else:
        try:
            response = json.loads(r.content)
        except Exception:
            response["message"] = "Remove AutoInvest fails"
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
        pika.ConnectionParameters(host=RABBIT_MQ_HOST))

    channel = connection.channel()

    channel.queue_declare(queue='buy_queue')
    channel.queue_declare(queue='sell_queue')
    channel.queue_declare(queue='get_all_invest_by_user')
    channel.queue_declare(queue='get_stock_invest_by_user')
    channel.queue_declare(queue='get_history_stock_by_user')
    channel.queue_declare(queue='get_all_history_by_user')
    channel.queue_declare(queue='get_value_of_account')
    channel.queue_declare(queue='get-detailed-user-invest')
    channel.queue_declare(queue='autobuy_queue')
    channel.queue_declare(queue='autosell_queue')
    channel.queue_declare(queue='remove_autoinvest_queue')
    channel.queue_declare(queue='pending_autoinvest')

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='buy_queue', on_message_callback=on_request_buy)
    channel.basic_consume(queue='sell_queue', on_message_callback=on_request_sell)
    channel.basic_consume(queue='get_all_invest_by_user', on_message_callback=on_get_invest_by_user)
    channel.basic_consume(queue='get_stock_invest_by_user', on_message_callback=on_stock_invest_by_user)
    channel.basic_consume(queue='get_history_stock_by_user', on_message_callback=on_history_stock_user)
    channel.basic_consume(queue='get_all_history_by_user', on_message_callback=on_all_history_user)
    channel.basic_consume(queue='get_value_of_account', on_message_callback=on_value_of_account)
    channel.basic_consume(queue='get-detailed-user-invest', on_message_callback=on_detailed_user)
    channel.basic_consume(queue='autobuy_queue', on_message_callback=on_request_autobuy)
    channel.basic_consume(queue='autosell_queue', on_message_callback=on_request_autosell)
    channel.basic_consume(queue='remove_autoinvest_queue', on_message_callback=on_request_remove_autoinvest)
    channel.basic_consume(queue='pending_autoinvest', on_message_callback=on_request_pending_autoinvest)

    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print('Invest RabbitMQ Server down.')


if __name__ == '__main__':
    start()
