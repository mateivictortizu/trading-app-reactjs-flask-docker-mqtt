import json
import os
from urllib import parse
import requests
import pika

URL = 'http://'+os.environ.get('STOCK_MICROSERVICE', '127.0.0.1:5001')+'/'
RABBIT_MQ_HOST = os.environ.get('RABBITMQ_HOST', 'localhost')


def on_add_stock(ch, method, props, body):
    json_body = json.loads(body)
    r = requests.post(parse.urljoin(URL, "add-stock"), json=json_body)
    response = dict()
    if r.status_code not in range(300, 509):
        json_obj = json.loads(r.content)
        response = json_obj
    response["code"] = r.status_code
    response = json.dumps(response)
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


def on_get_stock_info(ch, method, props, body):
    json_body = json.loads(body)
    r = requests.get(parse.urljoin(URL, "get-stock-info/" + json_body['stock_symbol']))
    response = dict()
    if r.status_code not in range(300, 509):
        json_obj = json.loads(r.content)
        response = json_obj
    response["code"] = r.status_code
    response = json.dumps(response)
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


def on_get_stock_price(ch, method, props, body):
    json_body = json.loads(body)
    r = requests.get(parse.urljoin(URL, "get-stock-price/" + json_body['stock_symbol']))
    response = dict()
    if r.status_code not in range(300, 509):
        json_obj = json.loads(r.content)
        response = json_obj
    response["code"] = r.status_code
    response = json.dumps(response)
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


def on_get_list_stock_price(ch, method, props, body):
    json_body = json.loads(body)
    r = requests.post(parse.urljoin(URL, "get-list-stock-price"), json=json_body)
    response = dict()
    if r.status_code not in range(300, 509):
        json_obj = json.loads(r.content)
        response = json_obj
    response["code"] = r.status_code
    response = json.dumps(response)
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


def on_update_price(ch, method, props, body):
    json_body = json.loads(body)
    r = requests.post(parse.urljoin(URL, "update-price"), json=json_body)
    response = dict()
    if r.status_code not in range(300, 509):
        json_obj = json.loads(r.content)
        response = json_obj
    response["code"] = r.status_code
    response = json.dumps(response)
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


def on_update_stock(ch, method, props, body):
    json_body = json.loads(body)
    r = requests.post(parse.urljoin(URL, "update-stock"), json=json_body)
    response = dict()
    if r.status_code not in range(300, 509):
        json_obj = json.loads(r.content)
        response = json_obj
    response["code"] = r.status_code
    response = json.dumps(response)
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


def on_get_all_stocks(ch, method, props, body):
    r = requests.get(parse.urljoin(URL, "get-all-stocks"))
    response = dict()
    if r.status_code not in range(300, 509):
        json_obj = json.loads(r.content)
        response = json_obj
    response["code"] = r.status_code
    response = json.dumps(response)
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


def on_get_all_stocks_by_user_wathclist(ch, method, props, body):
    json_body = json.loads(body)
    r = requests.get(parse.urljoin(URL, "get-all-stocks-by-user-watchlist"), json=json_body)
    response = dict()
    if r.status_code not in range(300, 509):
        json_obj = json.loads(r.content)
        response = json_obj
    response["code"] = r.status_code
    response = json.dumps(response)
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


def on_remove_watchlist(ch, method, props, body):
    json_body = json.loads(body)
    r = requests.post(parse.urljoin(URL, "remove-watchlist"), json=json_body)
    response = dict()
    if r.status_code not in range(300, 509):
        json_obj = json.loads(r.content)
        response = json_obj
    response["code"] = r.status_code
    response = json.dumps(response)
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


def on_add_watchlist(ch, method, props, body):
    json_body = json.loads(body)
    r = requests.post(parse.urljoin(URL, "add-watchlist"), json=json_body)
    response = dict()
    if r.status_code not in range(300, 509):
        json_obj = json.loads(r.content)
        response = json_obj
    response["code"] = r.status_code
    response = json.dumps(response)
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


def start():
    print('Stock RabbitMQ Server start...')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=RABBIT_MQ_HOST))

    channel = connection.channel()

    channel.queue_declare(queue='add-stock')
    channel.queue_declare(queue='get-stock-info')
    channel.queue_declare(queue='get-stock-price')
    channel.queue_declare(queue='get-list-stock-price')
    channel.queue_declare(queue='update-price')
    channel.queue_declare(queue='update-stock')
    channel.queue_declare(queue='get-all-stocks')
    channel.queue_declare(queue='get-all-stocks-by-user-watchlist')
    channel.queue_declare(queue='remove-watchlist')
    channel.queue_declare(queue='add-watchlist')

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='add-stock', on_message_callback=on_add_stock)
    channel.basic_consume(queue='get-stock-info', on_message_callback=on_get_stock_info)
    channel.basic_consume(queue='get-stock-price', on_message_callback=on_get_stock_price)
    channel.basic_consume(queue='get-list-stock-price', on_message_callback=on_get_list_stock_price)
    channel.basic_consume(queue='update-price', on_message_callback=on_update_price)
    channel.basic_consume(queue='update-stock', on_message_callback=on_update_stock)
    channel.basic_consume(queue='get-all-stocks', on_message_callback=on_get_all_stocks)
    channel.basic_consume(queue='get-all-stocks-by-user-watchlist',
                          on_message_callback=on_get_all_stocks_by_user_wathclist)
    channel.basic_consume(queue='add-watchlist', on_message_callback=on_add_watchlist)
    channel.basic_consume(queue='remove-watchlist', on_message_callback=on_remove_watchlist)

    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print('Stock RabbitMQ Server down.')


if __name__ == '__main__':
    start()
