from flask import Flask
from flask_socketio import SocketIO

from .spurita_api_handler import error_handler

from .status import status_api
from .auth import auth_api
from ..database import db


def create_api_server():

    app = Flask(__name__)

    db.init_app(app)

    socketio = SocketIO(app)

    add_handlers(app)
    add_blueprints(app)

    return app, socketio


def add_handlers(app):
    error_handler(app)


def add_blueprints(app):
    app.register_blueprint(status_api)
    app.register_blueprint(auth_api)
