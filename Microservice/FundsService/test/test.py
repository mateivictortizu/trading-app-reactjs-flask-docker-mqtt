import shutil
from unittest import TestCase

from flask_migrate import init, migrate, upgrade

from app import app


class FundsTest(TestCase):

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

    def test_add_money(self):
        flask_app = self.create_app()
        with flask_app.test_client() as test_client:
            json_body = {
                "user": "test",
                "value": 5
            }
            response = test_client.post('/add-money', json=json_body)
            assert response.status_code == 200

    def test_withdraw_money(self):
        flask_app = self.create_app()
        with flask_app.test_client() as test_client:
            json_body = {
                "user": "test",
                "value": 4
            }
            response = test_client.post('/withdraw-money', json=json_body)
            assert response.status_code == 200

    def test_get_funds(self):
        flask_app = self.create_app()
        with flask_app.test_client() as test_client:
            response = test_client.get('/get-funds/test')
            assert response.status_code == 200

    def test_add_money_after_sell(self):
        flask_app = self.create_app()
        with flask_app.test_client() as test_client:
            json_body = {
                "user": "test",
                "value": 4
            }
            response = test_client.post('/add-money-after-sell', json=json_body)
            assert response.status_code == 200

    def test_withdraw_money_after_buy(self):
        flask_app = self.create_app()
        with flask_app.test_client() as test_client:
            json_body = {
                "user": "test",
                "value": 4
            }
            response = test_client.post('/withdraw-money-after-buy', json=json_body)
            assert response.status_code == 200

