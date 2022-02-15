from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SECRET_KEY"] = 'LICENTA2022'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///registration.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
