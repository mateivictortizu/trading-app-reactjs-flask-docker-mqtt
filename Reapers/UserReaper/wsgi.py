import json
from urllib import parse
import requests
import pika

URL = "http://127.0.0.1:5003/"


def on_ban(ch, method, props, body):
    pass


def on_verify_user(ch, method, props, body):
    pass


def on_check_token(ch, method, props, body):
    pass


def on_register(ch, method, props, body):
    pass


def on_login(ch, method, props, body):
    pass


def on_validate_account(ch, method, props, body):
    pass


def on_resend_validate_account(ch, method, props, body):
    pass


def on_validate_otp(ch, method, props, body):
    pass


def on_resend_otp(ch, method, props, body):
    pass


def on_logout(ch, method, props, body):
    pass


def on_change_password(ch, method, props, body):
    pass


def on_request_change_password(ch, method, props, body):
    pass


def on_reset_pass(ch, method, props, body):
    pass


def on_set_new_pass(ch, method, props, body):
    pass


def start():
    print('Stock RabbitMQ Server start...')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))

    channel = connection.channel()

    channel.queue_declare(queue='add-stock')
    channel.queue_declare(queue='get-stock-info')
    channel.queue_declare(queue='get-stock-price')
    channel.queue_declare(queue='get-list-stock-price')
    channel.queue_declare(queue='update-price')
    channel.queue_declare(queue='update-stock')
    channel.queue_declare(queue='get-all-stocks')

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
        print('Stock RabbitMQ Server down.')


if __name__ == '__main__':
    start()
