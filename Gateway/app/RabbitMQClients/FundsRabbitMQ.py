import json
import time
import uuid
import pika

from app.RabbitMQClients import rabbit_mq_host_funds


class AddMoneyClient(object):

    def __init__(self):
        self.corr_id = None
        self.response = None
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=rabbit_mq_host_funds))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, body):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key='add-money',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=json.dumps(body))
        timeout = time.time() + 5
        while self.response is None:
            self.connection.process_data_events()
            if time.time() > timeout:
                break
        return self.response


class AddMoneyAfterSellClient(object):

    def __init__(self):
        self.corr_id = None
        self.response = None
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=rabbit_mq_host_funds))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, body):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key='add-money-after-sell',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=json.dumps(body))
        timeout = time.time() + 5
        while self.response is None:
            self.connection.process_data_events()
            if time.time() > timeout:
                break
        return self.response


class WithdrawMoneyClient(object):

    def __init__(self):
        self.corr_id = None
        self.response = None
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=rabbit_mq_host_funds))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, body):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key='withdraw-money',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=json.dumps(body))
        timeout = time.time() + 5
        while self.response is None:
            self.connection.process_data_events()
            if time.time() > timeout:
                break
        return self.response


class WithdrawMoneyAfterBuyClient(object):

    def __init__(self):
        self.corr_id = None
        self.response = None
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=rabbit_mq_host_funds))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, body):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key='withdraw-money-after-buy',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=json.dumps(body))
        timeout = time.time() + 5
        while self.response is None:
            self.connection.process_data_events()
            if time.time() > timeout:
                break
        return self.response


class GetFundsClient(object):

    def __init__(self):
        self.corr_id = None
        self.response = None
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=rabbit_mq_host_funds))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, body):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key='get-funds',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=json.dumps(body))
        timeout = time.time() + 5
        while self.response is None:
            self.connection.process_data_events()
            if time.time() > timeout:
                break
        return self.response
