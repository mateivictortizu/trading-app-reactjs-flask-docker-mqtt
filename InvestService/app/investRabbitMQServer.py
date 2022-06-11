import json

import pika

from app.DAO.investDAO import buy_investDAO, sell_investDAO


def on_request_buy(ch, method, props, body):
    json_body = json.loads(body)
    user = json_body['user']
    stock_symbol = json_body['stock_symbol']
    cantitate = json_body['cantitate']
    price = json_body['price']
    try:
        buy_investDAO(user, stock_symbol, cantitate, price)
        response = json.dumps({"message": "Buy Ok", "code": 200})
    except Exception:
        response = json.dumps({"message": "Buy Fail", "code": 400})

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


def on_request_sell(ch, method, props, body):
    json_body = json.loads(body)
    user = json_body['user']
    stock_symbol = json_body['stock_symbol']
    cantitate = json_body['cantitate']
    print(stock_symbol)
    price = json_body['price']
    try:
        sell_investDAO(user, stock_symbol, cantitate, price)
        response = json.dumps({"message": "Sell Ok", "code": 200})
    except Exception:
        response = json.dumps({"message": "Sell Fail", "code": 400})

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

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='buy_queue', on_message_callback=on_request_buy)
    channel.basic_consume(queue='sell_queue', on_message_callback=on_request_sell)
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print('Invest RabbitMQ Server down.')
