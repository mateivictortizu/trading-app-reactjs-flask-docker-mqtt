import json
import os
from urllib import parse
import requests
import pika

URL = 'http://'+os.environ.get('RECOMMENDATION_MICROSERVICE', 'http://127.0.0.1:5006/')+'/'
RABBIT_MQ_HOST = os.environ.get('RABBITMQ_HOST', 'localhost')


def on_recommendation(ch, method, props, body):
    json_body = json.loads(body)
    r = requests.get(parse.urljoin(URL, "/recommendation"), json=json_body)
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
    print('Recommendation RabbitMQ Server start...')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=RABBIT_MQ_HOST))

    channel = connection.channel()

    channel.queue_declare(queue='recommendation')
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='recommendation', on_message_callback=on_recommendation)

    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print('Recommendation RabbitMQ Server down.')


if __name__ == '__main__':
    start()
