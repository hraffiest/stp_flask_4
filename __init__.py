from flask import Flask
from config import Config
from models import *
from admin import *


def create_app(config):
    app = Flask(__name__)

    app.config.from_object(config)
    db.init_app(app)
    admin.init_app(app)
    # blueprint for auth routes in our app
    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from views import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

