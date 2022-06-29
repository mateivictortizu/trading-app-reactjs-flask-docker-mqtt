import shutil
from unittest import TestCase

from flask_migrate import init, migrate, upgrade

from app import app


class StockTest(TestCase):

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

    def test_add_stock(self):
        flask_app = self.create_app()
        with flask_app.test_client() as test_client:
            json_body = {
                "stock_symbol": "TSLA"
            }
            response = test_client.post('/add-stock', json=json_body)
            assert response.status_code == 200

    def test_get_stock_info(self):
        flask_app = self.create_app()
        with flask_app.test_client() as test_client:
            response = test_client.get('/get-stock-info/TSLA')
            assert response.status_code == 200

    def test_get_stock_price(self):
        flask_app = self.create_app()
        with flask_app.test_client() as test_client:
            response = test_client.get('/get-stock-price/TSLA')
            assert response.status_code == 200

    def test_get_list_stock_price(self):
        flask_app = self.create_app()
        with flask_app.test_client() as test_client:
            json_body = {
                "stock_list": ["TSLA"]
            }
            response = test_client.post('/get-list-stock-price', json=json_body)
            assert response.status_code == 200
