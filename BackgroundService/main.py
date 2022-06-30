import time
import os
import requests
from apscheduler.schedulers.background import BackgroundScheduler
from pytz import utc

gateway_host = os.getenv('GATEWAY_HOST', '127.0.0.1:5000')
gateway_protocol = os.getenv('GATEWAY_PROTOCOL', 'http')

stock_host = os.getenv('STOCK_HOST', '127.0.0.1:5001')
stock_protocol = os.getenv('STOCK_PROTOCOL', 'http')

invest_host = os.getenv('INVEST_HOST', '127.0.0.1:5005')
invest_protocol = os.getenv('INVEST_PROTOCOL', 'http')

funds_host = os.getenv('FUNDS_HOST', '127.0.0.1:5002')
funds_protocol = os.getenv('FUNDS_PROTOCOL', 'http')


def update_price():
    x = requests.post('{}://{}/update-price'.format(gateway_protocol, gateway_host), verify=False)
    if x.status_code == 200:
        time.sleep(20)
        invest_autobuy()
        requests.get('{}://{}/update-price-clients'.format(gateway_protocol, gateway_host), verify=False)


def update_stocks():
    requests.post('{}://{}/update-stock'.format(gateway_protocol, gateway_host), verify=False)


def invest_autobuy():
    stock_prices = requests.get('{}://{}/get-all-stocks'.format(stock_protocol, stock_host), verify=False)
    all_invests = requests.get('{}://{}/get-all-autoinvests'.format(invest_protocol, invest_host), verify=False)
    if stock_prices.status_code == 200 and all_invests.status_code == 200:
        all_invests = all_invests.json()['message']
        for sp in stock_prices.json()['message']:
            if sp['stock_symbol'] in all_invests:
                for pending_invest in all_invests[sp['stock_symbol']]:
                    if pending_invest['action_type'] == 'BUY':
                        if sp['price'] <= pending_invest['price']:
                            user_funds = requests.get(
                                '{}://{}/get-funds/{}'.format(funds_protocol, funds_host, pending_invest['user']),
                                verify=False)
                            print(user_funds.status_code)
                            if user_funds.status_code == 200:
                                if user_funds.json()['value'] >= sp['price'] * pending_invest['cantitate']:
                                    json_modify_money = {
                                        'user': pending_invest['user'],
                                        'value': sp['price'] * pending_invest['cantitate']
                                    }
                                    requests.post('{}://{}/withdraw-money-after-buy'.format(funds_protocol, funds_host),
                                                  json=json_modify_money, verify=False)

                                    json_body = {"cantitate": pending_invest['cantitate'],
                                                 "price": sp['price'],
                                                 "user": pending_invest['user'],
                                                 "stock_symbol": sp['stock_symbol']}
                                    result_post = requests.post('{}://{}/buy'.format(invest_protocol, invest_host),
                                                                verify=False, json=json_body)
                                    requests.delete(
                                            '{}://{}/remove-autoinvest'.format(invest_protocol, invest_host),
                                            verify=False, json={'id_invest': pending_invest['id']})
                    else:
                        if sp['price'] >= pending_invest['price']:
                            json_body = {"cantitate": pending_invest['cantitate'],
                                         "price": sp['price'],
                                         "user": pending_invest['user'],
                                         "stock_symbol": sp['stock_symbol']}
                            result_post = requests.post('{}://{}/sell'.format(invest_protocol, invest_host),
                                                        verify=False, json=json_body)
                            if result_post.status_code == 200:
                                requests.delete('{}://{}/remove-autoinvest'.format(invest_protocol, invest_host),
                                                verify=False, json={'id_invest': pending_invest['id']})


if __name__ == "__main__":

    scheduler = BackgroundScheduler()
    scheduler.configure(timezone=utc)
    scheduler.add_job(update_price, 'interval', seconds=45)
    scheduler.add_job(update_stocks, 'interval', days=1)
    scheduler.start()

    try:
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
