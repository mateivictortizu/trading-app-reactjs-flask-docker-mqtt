from flask import Flask
from flask_bcrypt import Bcrypt
from flask_json_schema import JsonSchema
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

app = Flask(__name__)

# put this variable in a .env file

app.config["JWT_SECRET_KEY"] = "Licenta2022"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///{}'.format('registration.db')
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'tizu.licenta@gmail.com'
app.config['MAIL_PASSWORD'] = 'Licenta2022'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db, 'app/database/migrations')
bcrypt = Bcrypt()
schema = JsonSchema(app)
mail = Mail(app)
jwt = JWTManager(app)

from app.blueprints import userBlueprint

app.register_blueprint(userBlueprint.userBP)

from app.database import models
