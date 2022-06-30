import json
import os
from urllib import parse
import requests
import pika

URL = 'http://'+os.environ.get('USER_MICROSERVICE', '127.0.0.1:5003')+'/'
RABBIT_MQ_HOST = os.environ.get('RABBITMQ_HOST', 'localhost')


def on_ban(ch, method, props, body):
    json_body = json.loads(body)
    r = requests.delete(parse.urljoin(URL, "ban"), json=json_body)
    response = dict()
    if r.status_code not in range(300, 509):
        json_obj = json.loads(r.content)
        response = json_obj
    else:
        try:
            json_obj = json.loads(r.content)
            response = json_obj
        except Exception as e:
            print(e)
    response["code"] = r.status_code
    response = json.dumps(response)
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


def on_verify_user(ch, method, props, body):
    json_body = json.loads(body)
    r = requests.put(parse.urljoin(URL, "verify-user"), json=json_body)
    response = dict()
    if r.status_code not in range(300, 509):
        json_obj = json.loads(r.content)
        response = json_obj
    else:
        try:
            json_obj = json.loads(r.content)
            response = json_obj
        except Exception as e:
            print(e)
    response["code"] = r.status_code
    response = json.dumps(response)
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


def on_check_token(ch, method, props, body):
    token = json.loads(body)
    r = requests.get(parse.urljoin(URL, "check-token"), cookies={"jwt": token['jwt']})
    response = dict()
    if r.status_code not in range(300, 509):
        json_obj = json.loads(r.content)
        response = json_obj
    else:
        try:
            json_obj = json.loads(r.content)
            response = json_obj
        except Exception as e:
            print(e)
    response["code"] = r.status_code
    response = json.dumps(response)
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


def on_register(ch, method, props, body):
    json_body = json.loads(body)
    r = requests.post(parse.urljoin(URL, "register"), json=json_body)
    response = dict()
    if r.status_code not in range(300, 509):
        json_obj = json.loads(r.content)
        response = json_obj
    else:
        try:
            json_obj = json.loads(r.content)
            response = json_obj
        except Exception as e:
            print(e)
    response["code"] = r.status_code
    response = json.dumps(response)
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


def on_login(ch, method, props, body):
    json_body = json.loads(body)
    r = requests.post(parse.urljoin(URL, "login"), json=json_body)
    response = dict()
    if r.status_code not in range(300, 509):
        json_obj = json.loads(r.content)
        response = json_obj
    else:
        try:
            json_obj = json.loads(r.content)
            response = json_obj
        except Exception as e:
            print(e)
    if "Authorization" in r.headers:
        response["Authorization"] = r.headers["Authorization"]
    response["code"] = r.status_code
    response = json.dumps(response)
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


def on_validate_account(ch, method, props, body):
    json_body = json.loads(body)
    r = requests.get(parse.urljoin(URL, "validate-account/" + json_body['validation_code']), json=json_body)
    response = dict()
    if r.status_code not in range(300, 509):
        json_obj = json.loads(r.content)
        response = json_obj
    else:
        try:
            json_obj = json.loads(r.content)
            response = json_obj
        except Exception as e:
            print(e)
    response["code"] = r.status_code
    response = json.dumps(response)
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


def on_resend_validate_account(ch, method, props, body):
    json_body = json.loads(body)
    r = requests.post(parse.urljoin(URL, "resend-validate-account"), json=json_body)
    response = dict()
    if r.status_code not in range(300, 509):
        json_obj = json.loads(r.content)
        response = json_obj
    else:
        try:
            json_obj = json.loads(r.content)
            response = json_obj
        except Exception as e:
            print(e)
    response["code"] = r.status_code
    response = json.dumps(response)
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


def on_validate_otp(ch, method, props, body):
    json_body = json.loads(body)
    r = requests.post(parse.urljoin(URL, "validate-otp"), json=json_body)
    response = dict()
    if r.status_code not in range(300, 509):
        json_obj = json.loads(r.content)
        response = json_obj
    else:
        try:
            json_obj = json.loads(r.content)
            response = json_obj
        except Exception as e:
            print(e)
    if "Authorization" in r.headers:
        response["Authorization"] = r.headers["Authorization"]
    response["code"] = r.status_code
    response = json.dumps(response)
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


def on_resend_otp(ch, method, props, body):
    json_body = json.loads(body)
    r = requests.post(parse.urljoin(URL, "resend-otp"), json=json_body)
    response = dict()
    if r.status_code not in range(300, 509):
        json_obj = json.loads(r.content)
        response = json_obj
    else:
        try:
            json_obj = json.loads(r.content)
            response = json_obj
        except Exception as e:
            print(e)
    response["code"] = r.status_code
    response = json.dumps(response)
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


def on_logout(ch, method, props, body):
    json_body = json.loads(body)
    r = requests.delete(parse.urljoin(URL, "logout"), json=json_body)
    response = dict()
    if r.status_code not in range(300, 509):
        json_obj = json.loads(r.content)
        response = json_obj
    else:
        try:
            json_obj = json.loads(r.content)
            response = json_obj
        except Exception as e:
            print(e)
    response["code"] = r.status_code
    response = json.dumps(response)
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


def on_change_password(ch, method, props, body):
    json_body = json.loads(body)
    r = requests.put(parse.urljoin(URL, "change-password"), json=json_body)
    response = dict()
    if r.status_code not in range(300, 509):
        json_obj = json.loads(r.content)
        response = json_obj
    else:
        try:
            json_obj = json.loads(r.content)
            response = json_obj
        except Exception as e:
            print(e)
    response["code"] = r.status_code
    response = json.dumps(response)
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


def on_request_change_password(ch, method, props, body):
    json_body = json.loads(body)
    r = requests.post(parse.urljoin(URL, "request-change-password"), json=json_body)
    response = dict()
    if r.status_code not in range(300, 509):
        json_obj = json.loads(r.content)
        response = json_obj
    else:
        try:
            json_obj = json.loads(r.content)
            response = json_obj
        except Exception as e:
            print(e)
    response["code"] = r.status_code
    response = json.dumps(response)
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


def on_reset_pass(ch, method, props, body):
    json_body = json.loads(body)
    r = requests.get(parse.urljoin(URL, "reset-pass/" + json_body['reset_code']), json=json_body)
    response = dict()
    if r.status_code not in range(300, 509):
        json_obj = json.loads(r.content)
        response = json_obj
    else:
        try:
            json_obj = json.loads(r.content)
            response = json_obj
        except Exception as e:
            print(e)
    response["code"] = r.status_code
    response = json.dumps(response)
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


def on_set_new_pass(ch, method, props, body):
    json_body = json.loads(body)
    r = requests.post(parse.urljoin(URL, "set-new-pass"), json=json_body)
    response = dict()
    if r.status_code not in range(300, 509):
        json_obj = json.loads(r.content)
        response = json_obj
    else:
        try:
            json_obj = json.loads(r.content)
            response = json_obj
        except Exception as e:
            print(e)
    response["code"] = r.status_code
    response = json.dumps(response)
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


def start():
    print('User RabbitMQ Server start...')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=RABBIT_MQ_HOST))

    channel = connection.channel()

    channel.queue_declare(queue='ban')
    channel.queue_declare(queue='verify-user')
    channel.queue_declare(queue='check-token')
    channel.queue_declare(queue='register')
    channel.queue_declare(queue='login')
    channel.queue_declare(queue='validate-account')
    channel.queue_declare(queue='resend-validate-account')
    channel.queue_declare(queue='validate-otp')
    channel.queue_declare(queue='resend-otp')
    channel.queue_declare(queue='logout')
    channel.queue_declare(queue='change-password')
    channel.queue_declare(queue='request-change-password')
    channel.queue_declare(queue='reset-pass')
    channel.queue_declare(queue='set-new-pass')

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='ban', on_message_callback=on_ban)
    channel.basic_consume(queue='verify-user', on_message_callback=on_verify_user)
    channel.basic_consume(queue='check-token', on_message_callback=on_check_token)
    channel.basic_consume(queue='register', on_message_callback=on_register)
    channel.basic_consume(queue='login', on_message_callback=on_login)
    channel.basic_consume(queue='validate-account', on_message_callback=on_validate_account)
    channel.basic_consume(queue='resend-validate-account', on_message_callback=on_resend_validate_account)
    channel.basic_consume(queue='validate-otp', on_message_callback=on_validate_otp)
    channel.basic_consume(queue='resend-otp', on_message_callback=on_resend_otp)
    channel.basic_consume(queue='logout', on_message_callback=on_logout)
    channel.basic_consume(queue='change-password', on_message_callback=on_change_password)
    channel.basic_consume(queue='request-change-password', on_message_callback=on_request_change_password)
    channel.basic_consume(queue='reset-pass', on_message_callback=on_reset_pass)
    channel.basic_consume(queue='set-new-pass', on_message_callback=on_set_new_pass)

    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print('User RabbitMQ Server down.')


if __name__ == '__main__':
    start()
