import os
import shutil
import unittest
from unittest import TestCase

from flask_migrate import upgrade, migrate, init

from app import app


class InvestTest(TestCase):

    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {}
        return app

    @classmethod
    def setUpClass(cls):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {}
        app.config['TESTING'] = True
        with app.app_context():
            try:
                init()
            except:
                pass
            migrate()
            upgrade()

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree('app')

    def test_buy(self):
        flask_app = self.create_app()
        with flask_app.test_client() as test_client:
            json_body = {
                "user": "test",
                "stock_symbol": "TSLA",
                "cantitate": 5,
                "price": 720
            }
            response = test_client.post('/buy', json=json_body)
            assert response.status_code == 200

    def test_sell(self):
        flask_app = self.create_app()
        with flask_app.test_client() as test_client:
            json_body = {
                "user": "test",
                "stock_symbol": "TSLA",
                "cantitate": 2,
                "price": 720
            }
            response = test_client.post('/sell', json=json_body)
            assert response.status_code == 200

    def test_get_stock_invest_by_user(self):
        flask_app = self.create_app()
        with flask_app.test_client() as test_client:
            json_body = {
                "identifier": "test",
                "stock_symbol": "TSLA"
            }
            response = test_client.post('/get-stock-invest-by-user', json=json_body)
            assert response.status_code == 200

    def test_get_invest_by_user(self):
        flask_app = self.create_app()
        with flask_app.test_client() as test_client:
            json_body = {
                "identifier": "test",
                "stock_symbol": "TSLA"
            }
            response = test_client.post('/get-stock-invest-by-user', json=json_body)
            assert response.status_code == 200

    def test_invest_summary(self):
        flask_app = self.create_app()
        with flask_app.test_client() as test_client:
            json_body = {
                "identifier": "test",
                "stock_symbol": "TSLA"
            }
            response = test_client.post('/get-invest-summary-by-user', json=json_body)
            assert response.status_code == 200

    def test_get_users_invest(self):
        flask_app = self.create_app()
        with flask_app.test_client() as test_client:
            response = test_client.get('/get-users-invest')
            assert response.status_code == 200

    def test_get_history_stock_user(self):
        flask_app = self.create_app()
        with flask_app.test_client() as test_client:
            json_body = {
                "identifier": "test",
                "stock_symbol": "TSLA"
            }
            response = test_client.post('/get-history-stock-user', json=json_body)
            assert response.status_code == 200

    def test_get_all_history_user(self):
        flask_app = self.create_app()
        with flask_app.test_client() as test_client:
            json_body = {
                "identifier": "test"
            }
            response = test_client.post('/get-all-history-user', json=json_body)
            assert response.status_code == 200

    def test_get_value_of_user_account(self):
        flask_app = self.create_app()
        with flask_app.test_client() as test_client:
            json_body = {
                "identifier": "test"
            }
            response = test_client.get('/get-value-of-user-account', json=json_body)
            assert response.status_code == 200

    def test_get_detailed_stock_invest(self):
        flask_app = self.create_app()
        with flask_app.test_client() as test_client:
            json_body = {
                "identifier": "test"
            }
            response = test_client.get('/get-detailed-stock-invest', json=json_body)
            assert response.status_code == 200

    def test_autobuy(self):
        flask_app = self.create_app()
        with flask_app.test_client() as test_client:
            json_body = {
                "user": "test",
                "stock_symbol": "TSLA",
                "cantitate": 2,
                "price": 720
            }
            response = test_client.post('/autobuy', json=json_body)
            assert response.status_code == 200

    def test_autosell(self):
        flask_app = self.create_app()
        with flask_app.test_client() as test_client:
            json_body = {
                "user": "test",
                "stock_symbol": "TSLA",
                "cantitate": 2,
                "price": 720
            }
            response = test_client.post('/autosell', json=json_body)
            assert response.status_code == 200

    def test_remove_autoinvest(self):
        flask_app = self.create_app()
        with flask_app.test_client() as test_client:
            json_body = {
                "id_invest": 1
            }
            response = test_client.delete('/remove-autoinvest', json=json_body)
            assert response.status_code == 200

    def test_get_autoinvest_stock_user(self):
        flask_app = self.create_app()
        with flask_app.test_client() as test_client:
            json_body = {
                "identifier": "test",
                "stock_symbol": "TSLA"
            }
            response = test_client.post('/get-autoinvest-stock-user', json=json_body)
            assert response.status_code == 200

    def test_get_all_autoinvest(self):
        flask_app = self.create_app()
        with flask_app.test_client() as test_client:
            response = test_client.get('/get-all-autoinvests')
            assert response.status_code == 200


if __name__ == '__main__':
    unittest.main()
