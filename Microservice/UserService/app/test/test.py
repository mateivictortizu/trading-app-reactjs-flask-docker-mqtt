import shutil
from unittest import TestCase

from flask_migrate import init, migrate, upgrade

from app import application


class UserTest(TestCase):

    def create_app(self):
        application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        application.config["SQLALCHEMY_ENGINE_OPTIONS"] = {}
        return application

    @classmethod
    def setUpClass(cls):
        application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        application.config["SQLALCHEMY_ENGINE_OPTIONS"] = {}
        application.config['TESTING'] = True
        with application.app_context():
            try:
                init()
            except:
                pass
            migrate()
            upgrade()

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree('app')

    def test_login_invalid_credentials(self):
        flask_app = self.create_app()
        with flask_app.test_client() as test_client:
            json_body = {
                "identifier": "test@gmail.com",
                "password": "12345"
            }
            response = test_client.post('/login', json=json_body)
            assert response.status_code == 401

    def test_register(self):
        flask_app = self.create_app()
        with flask_app.test_client() as test_client:
            json_body = {
                "username": "Testare123",
                "password": "Test123&",
                "email": "test@gmail.com",
                "name": "Test",
                "surname": "Test",
                "address": "Test,Testare",
                "nationality": "RO",
                "phone": "0700000000",
                "date_of_birth": "1999-03-26",
                "country": "RO",
                "hostname": "test",
                "port": "5000"
            }
            response = test_client.post('/register', json=json_body)
            assert response.status_code == 201
