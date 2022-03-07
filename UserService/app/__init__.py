import os

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_executor import Executor
from flask_json_schema import JsonSchema
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db_user = os.getenv('DB_USER', 'matteovk')
db_password = os.getenv('DB_PASSWORD', 'admin')
db_host = os.getenv('DB_HOST', 'localhost')
db_database = os.getenv('DB_DATABASE', 'users')

app.config["JWT_SECRET_KEY"] = "Licenta2022"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@{}/{}'.format(db_user, db_password, db_host, db_database)
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {"pool_size": 100, "pool_timeout": 9,
                                           'connect_args': {'connect_timeout': 5},
                                           'execution_options': {"timeout": 5.0,
                                                                 "statement_timeout": 5.0,
                                                                 "query_timeout": 5.0,
                                                                 "execution_timeout": 5.0
                                                                 }
                                           }
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
executor = Executor(app)

from app.blueprints import userBlueprint, agentBlueprint

app.register_blueprint(userBlueprint.userBP)
app.register_blueprint(agentBlueprint.agentBP)

from app.database import models
