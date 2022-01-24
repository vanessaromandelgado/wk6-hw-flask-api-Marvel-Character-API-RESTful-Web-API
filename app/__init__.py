from flask import Flask
from config import Config
from flask_cors import CORS

from .marvel.routes import marvel
from .api.routes import api, apicall
from .models import login, db

from flask_migrate import Migrate, migrate

app = Flask (__name__)

CORS(app, origins = ['*'])

app.config.from_object(Config)

app.register_blueprint(api)
app.register_blueprint(marvel)

db.init_app(app)
migrate = Migrate(app, db)

login.init_app(app)
login.login_view='marvel.signin'
login.login_message='To view this page, please log in.'
login.login_message_category='danger'


from . import routes

from . import models