import os

rabbit_mq_host_funds = os.environ.get('RABBIT_MQ_FUNDS', 'localhost')
rabbit_mq_host_invest = os.environ.get('RABBIT_MQ_INVEST', 'localhost')
rabbit_mq_host_recommendation = os.environ.get('RABBIT_MQ_RECOMMENDATION', 'localhost')
rabbit_mq_host_stocks = os.environ.get('RABBIT_MQ_STOCKS', 'localhost')
rabbit_mq_host_user = os.environ.get('RABBIT_MQ_USER', 'localhost')
