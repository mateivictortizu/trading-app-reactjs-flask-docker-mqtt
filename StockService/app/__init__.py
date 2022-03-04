from flask import Flask
from flask_executor import Executor
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://matteovk:admin@localhost/stock'
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {"pool_size": 30, "pool_timeout": 9,
                                           'connect_args': {'connect_timeout': 5},
                                           'execution_options': {"timeout": 1.0,
                                                                 "statement_timeout": 1.0,
                                                                 "query_timeout": 1.0,
                                                                 "execution_timeout": 1.0
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
