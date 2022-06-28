import json
import time
import uuid
import pika

from app.RabbitMQClients import rabbit_mq_host_invest


class BuyClient(object):

    def __init__(self):
        self.corr_id = None
        self.response = None
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=rabbit_mq_host_invest))

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
            routing_key='buy_queue',
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


class SellClient(object):

    def __init__(self):
        self.corr_id = None
        self.response = None
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=rabbit_mq_host_invest))

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
            routing_key='sell_queue',
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


class GetAllInvestByUserClient(object):

    def __init__(self):
        self.corr_id = None
        self.response = None
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=rabbit_mq_host_invest))

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
            routing_key='get_all_invest_by_user',
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


class GetStockInvestByUserClient(object):

    def __init__(self):
        self.corr_id = None
        self.response = None
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=rabbit_mq_host_invest))

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
            routing_key='get_stock_invest_by_user',
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


class GetHistoryStockByUserClient(object):

    def __init__(self):
        self.corr_id = None
        self.response = None
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=rabbit_mq_host_invest))

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
            routing_key='get_history_stock_by_user',
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


class GetAllHistoryByUserClient(object):

    def __init__(self):
        self.corr_id = None
        self.response = None
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=rabbit_mq_host_invest))

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
            routing_key='get_all_history_by_user',
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


class GetValueOfAccountClient(object):

    def __init__(self):
        self.corr_id = None
        self.response = None
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=rabbit_mq_host_invest))

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
            routing_key='get_value_of_account',
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


class GetDetailedUserInvest(object):

    def __init__(self):
        self.corr_id = None
        self.response = None
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=rabbit_mq_host_invest))

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
            routing_key='get-detailed-user-invest',
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


class AutoBuyClient(object):

    def __init__(self):
        self.corr_id = None
        self.response = None
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=rabbit_mq_host_invest))

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
            routing_key='autobuy_queue',
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


class AutoSellClient(object):

    def __init__(self):
        self.corr_id = None
        self.response = None
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=rabbit_mq_host_invest))

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
            routing_key='autosell_queue',
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


class PendingAutoinvestClient(object):

    def __init__(self):
        self.corr_id = None
        self.response = None
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=rabbit_mq_host_invest))

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
            routing_key='pending_autoinvest',
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


class RemoveAutoinvestClient(object):
    def __init__(self):
        self.corr_id = None
        self.response = None
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=rabbit_mq_host_invest))

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
            routing_key='remove_autoinvest_queue',
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
