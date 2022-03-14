import time
import os
import requests
from apscheduler.schedulers.background import BackgroundScheduler
from pytz import utc

stock_host = os.getenv('STOCK_HOST', '127.0.0.1:5000')
stock_protocol = os.getenv('STOCK_PROTOCOL', 'http')


def update_price():
    requests.post('{}://{}/update-price'.format(stock_protocol, stock_host), verify=False)


def update_stocks():
    requests.post('{}://{}/update-stock'.format(stock_protocol, stock_host), verify=False)


if __name__ == "__main__":

    scheduler = BackgroundScheduler()
    scheduler.configure(timezone=utc)
    scheduler.add_job(update_price, 'interval', seconds=10)
    scheduler.add_job(update_stocks, 'interval', days=1)
    scheduler.start()

    try:
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
