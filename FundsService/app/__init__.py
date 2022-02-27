from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///{}'.format('registration.db')

db = SQLAlchemy(app)
migrate = Migrate(app, db, 'app/database/migrations')

from app.blueprints import fundsBlueprint

app.register_blueprint(fundsBlueprint.fundsBP)

from app.database import models
