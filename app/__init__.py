from flask import Flask
from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#create a flask app (need to change name to avoid confusion)
flaskApp = Flask(__name__)
flaskApp.config.from_object(Config)
#create objects for database
db = SQLAlchemy(flaskApp)
migrate = Migrate(flaskApp, db)


# import routes from our app folder
from app import routes,models

