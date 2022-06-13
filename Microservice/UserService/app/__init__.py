import os
import socket

from flask import Flask, request
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_executor import Executor
from flask_json_schema import JsonSchema
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)
# , resources={r"/*": {"origins": "http://localhost:3000", "headers":"Authorization"}})
db_user = os.getenv('DB_USER', 'matteovk')
db_password = os.getenv('DB_PASSWORD', 'admin')
db_host = os.getenv('DB_HOST', 'localhost')
db_database = os.getenv('DB_DATABASE', 'users')

application.config["JWT_SECRET_KEY"] = "Licenta2022"

application.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@{}/{}'.format(db_user, db_password, db_host, db_database)
application.config["SQLALCHEMY_ENGINE_OPTIONS"] = {"pool_size": 100, "pool_timeout": 9,
                                                   'connect_args': {'connect_timeout': 5},
                                                   'execution_options': {"timeout": 5.0,
                                                                         "statement_timeout": 5.0,
                                                                         "query_timeout": 5.0,
                                                                         "execution_timeout": 5.0
                                                                         }
                                                   }
application.config['MAIL_SERVER'] = 'smtp.mail.yahoo.com'
application.config['MAIL_PORT'] = 465
application.config['MAIL_USERNAME'] = 'victor.tizu@yahoo.ca'
application.config['MAIL_PASSWORD'] = 'wroxjwgyoqxaiyke'
application.config['MAIL_USE_TLS'] = False
application.config['MAIL_USE_SSL'] = True
application.config['CORS_EXPOSE_HEADERS'] = 'Authorization'
application.config['CORS_ALLOW_HEADERS'] = ['Content-Type','Authorization']
application.config['CORS_ORIGINS'] = 'http://localhost:3000'

cors = CORS(application)
db = SQLAlchemy(application)
migrate = Migrate(application, db, 'app/database/migrations')
bcrypt = Bcrypt()
schema = JsonSchema(application)
mail = Mail(application)
executor = Executor(application)

from app.blueprints import userBlueprint, agentBlueprint

application.register_blueprint(userBlueprint.userBP)
application.register_blueprint(agentBlueprint.agentBP)

from app.database import models
