import json
import time
import uuid
import pika

from app.RabbitMQClients import rabbit_mq_host_user


class BanClient(object):

    def __init__(self):
        self.corr_id = None
        self.response = None
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=rabbit_mq_host_user))

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
            routing_key='ban',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=json.dumps(body))
        timeout = time.time() + 5
        while self.response is None:
            self.connection.process_data_events()
            if time.time() > timeout:
                return {'error': 'Ban Error', 'code': 500}
        return self.response


class VerifyUserClient(object):

    def __init__(self):
        self.corr_id = None
        self.response = None
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=rabbit_mq_host_user))

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
            routing_key='verify-user',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=json.dumps(body))
        timeout = time.time() + 5
        while self.response is None:
            self.connection.process_data_events()
            if time.time() > timeout:
                return {'error': 'Verify User Error', 'code': 500}
        return self.response


class CheckTokenClient(object):

    def __init__(self):
        self.corr_id = None
        self.response = None
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=rabbit_mq_host_user))

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
            routing_key='check-token',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=json.dumps(body))
        timeout = time.time() + 5
        while self.response is None:
            self.connection.process_data_events()
            if time.time() > timeout:
                return {'error': 'Check Token Error', 'code': 500}
        return self.response


class RegisterClient(object):

    def __init__(self):
        self.corr_id = None
        self.response = None
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=rabbit_mq_host_user))

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
            routing_key='register',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=json.dumps(body))
        timeout = time.time() + 5
        while self.response is None:
            self.connection.process_data_events()
            if time.time() > timeout:
                return {'error': 'Register Error', 'code': 500}
        return self.response


class LoginClient(object):

    def __init__(self):
        self.corr_id = None
        self.response = None
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=rabbit_mq_host_user))

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
            routing_key='login',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=json.dumps(body))
        timeout = time.time() + 5
        while self.response is None:
            self.connection.process_data_events()
            if time.time() > timeout:
                return {'error': 'Login Error', 'code': 500}
        return self.response


class ValidateAccountClient(object):

    def __init__(self):
        self.corr_id = None
        self.response = None
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=rabbit_mq_host_user))

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
            routing_key='validate-account',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=json.dumps(body))
        timeout = time.time() + 5
        while self.response is None:
            self.connection.process_data_events()
            if time.time() > timeout:
                return {'error': 'Validate account Error', 'code': 500}
        return self.response


class ResendValidateAccountClient(object):

    def __init__(self):
        self.corr_id = None
        self.response = None
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=rabbit_mq_host_user))

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
            routing_key='resend-validate-account',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=json.dumps(body))
        timeout = time.time() + 5
        while self.response is None:
            self.connection.process_data_events()
            if time.time() > timeout:
                return {'error': 'Resend Validate Error', 'code': 500}
        return self.response


class ValidateOTPClient(object):

    def __init__(self):
        self.corr_id = None
        self.response = None
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=rabbit_mq_host_user))

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
            routing_key='validate-otp',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=json.dumps(body))
        timeout = time.time() + 5
        while self.response is None:
            self.connection.process_data_events()
            if time.time() > timeout:
                return {'error': 'Validate OTP Error', 'code': 500}
        return self.response


class ResendOTPClient(object):

    def __init__(self):
        self.corr_id = None
        self.response = None
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=rabbit_mq_host_user))

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
            routing_key='resend-otp',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=json.dumps(body))
        timeout = time.time() + 5
        while self.response is None:
            self.connection.process_data_events()
            if time.time() > timeout:
                return {'error': 'Resend OTP Error', 'code': 500}
        return self.response


class LogoutClient(object):

    def __init__(self):
        self.corr_id = None
        self.response = None
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=rabbit_mq_host_user))

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
            routing_key='logout',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=json.dumps(body))
        timeout = time.time() + 5
        while self.response is None:
            self.connection.process_data_events()
            if time.time() > timeout:
                return {'error': 'Logout Error', 'code': 500}
        return self.response


class ChangePasswordClient(object):

    def __init__(self):
        self.corr_id = None
        self.response = None
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=rabbit_mq_host_user))

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
            routing_key='change-password',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=json.dumps(body))
        timeout = time.time() + 5
        while self.response is None:
            self.connection.process_data_events()
            if time.time() > timeout:
                return {'error': 'Change Password Error', 'code': 500}
        return self.response


class RequestChangePasswordClient(object):

    def __init__(self):
        self.corr_id = None
        self.response = None
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=rabbit_mq_host_user))

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
            routing_key='request-change-password',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=json.dumps(body))
        timeout = time.time() + 5
        while self.response is None:
            self.connection.process_data_events()
            if time.time() > timeout:
                return {'error': 'Request Change Password Error', 'code': 500}
        return self.response


class ResetPassClient(object):

    def __init__(self):
        self.corr_id = None
        self.response = None
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=rabbit_mq_host_user))

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
            routing_key='reset-pass',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=json.dumps(body))
        timeout = time.time() + 5
        while self.response is None:
            self.connection.process_data_events()
            if time.time() > timeout:
                return {'error': 'Reset Password Error', 'code': 500}
        return self.response


class SetNewPassClient(object):

    def __init__(self):
        self.corr_id = None
        self.response = None
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=rabbit_mq_host_user))

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
            routing_key='set-new-pass',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=json.dumps(body))
        timeout = time.time() + 5
        while self.response is None:
            self.connection.process_data_events()
            if time.time() > timeout:
                return {'error': 'Set New Pass Error', 'code': 500}
        return self.response
