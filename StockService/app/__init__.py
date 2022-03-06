from flask import Flask
from flask_executor import Executor
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

db_user = os.getenv('DB_USER', 'matteovk')
db_password = os.getenv('DB_PASSWORD', 'admin')
db_host = os.getenv('DB_HOST', 'localhost')
db_database = os.getenv('DB_DATABASE', 'stock')

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@{}/{}'.format(db_user, db_password, db_host, db_database)
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {"pool_size": 50, "pool_timeout": 9,
                                           'connect_args': {'connect_timeout': 5},
                                           'execution_options': {"timeout": 5.0,
                                                                 "statement_timeout": 5.0,
                                                                 "query_timeout": 5.0,
                                                                 "execution_timeout": 5.0
                                                                 }
                                           }

db = SQLAlchemy(app)
migrate = Migrate(app, db, 'app/database/migrations')
executor = Executor(app)

from app.blueprints import stockBlueprint

app.register_blueprint(stockBlueprint.stockBP)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()


from app.database import models
