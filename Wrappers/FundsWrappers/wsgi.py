import json
from urllib import parse
import requests
import pika

URL = "http://127.0.0.1:5002/"


def on_add_money(ch, method, props, body):
    json_body = json.loads(body)
    r = requests.post(parse.urljoin(URL, "add-money"), json=json_body)
    response = dict()
    json_obj = json.loads(r.content)
    response = json_obj
    response["code"] = r.status_code
    response = json.dumps(response)
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


def on_withdraw_money(ch, method, props, body):
    json_body = json.loads(body)
    r = requests.post(parse.urljoin(URL, "withdraw-money"), json=json_body)
    response = dict()
    json_obj = json.loads(r.content)
    response = json_obj
    response["code"] = r.status_code
    response = json.dumps(response)
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)

def on_add_money_after_sell(ch, method, props, body):
    json_body = json.loads(body)
    r = requests.post(parse.urljoin(URL, "add-money-after-sell"), json=json_body)
    response = dict()
    json_obj = json.loads(r.content)
    response = json_obj
    response["code"] = r.status_code
    response = json.dumps(response)
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


def on_withdraw_money_after_buy(ch, method, props, body):
    json_body = json.loads(body)
    r = requests.post(parse.urljoin(URL, "withdraw-money-after-buy"), json=json_body)
    response = dict()
    json_obj = json.loads(r.content)
    response = json_obj
    response["code"] = r.status_code
    response = json.dumps(response)
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


def on_get_funds(ch, method, props, body):
    json_body = json.loads(body)
    r = requests.get(parse.urljoin(URL, "get-funds/" + json_body["user"]), json=json_body)
    response = dict()
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
    print('Funds RabbitMQ Server start...')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))

    channel = connection.channel()

    channel.queue_declare(queue='add-money')
    channel.queue_declare(queue='withdraw-money')
    channel.queue_declare(queue='add-money-after-sell')
    channel.queue_declare(queue='withdraw-money-after-buy')
    channel.queue_declare(queue='get-funds')

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='add-money', on_message_callback=on_add_money)
    channel.basic_consume(queue='withdraw-money', on_message_callback=on_withdraw_money)
    channel.basic_consume(queue='add-money-after-sell', on_message_callback=on_add_money_after_sell)
    channel.basic_consume(queue='withdraw-money-after-buy', on_message_callback=on_withdraw_money_after_buy)
    channel.basic_consume(queue='get-funds', on_message_callback=on_get_funds)
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print('Funds RabbitMQ Server down.')


if __name__ == '__main__':
    start()
