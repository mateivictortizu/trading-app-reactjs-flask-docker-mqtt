from flask import Flask
from flask_executor import Executor
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import os

from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool

app = Flask(__name__)

db_user = os.getenv('DB_USER', 'matteovk')
db_password = os.getenv('DB_PASSWORD', 'admin')
db_host = os.getenv('DB_HOST', 'localhost')
db_database = os.getenv('DB_DATABASE', 'stock')

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@{}/{}'.format(db_user, db_password, db_host, db_database)
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {"pool_size": 151, "pool_timeout": 4,
                                           'connect_args': {'connect_timeout': 2},
                                           'execution_options': {"timeout": 1.0,
                                                                 "statement_timeout": 1.0,
                                                                 "query_timeout": 1.0,
                                                                 "execution_timeout": 1.0
                                                                 }
                                           }

db = SQLAlchemy(app)
migrate = Migrate(app, db, 'app/database/migrations')
executor = Executor(app)
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], poolclass=NullPool)

from app.blueprints import stockBlueprint

app.register_blueprint(stockBlueprint.stockBP)

from app.database import models
