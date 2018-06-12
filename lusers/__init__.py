# -*- coding: utf-8 -*-
import logging
import os
import sys

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from lutils.api_errors import install_error_handlers

from itsdangerous import TimestampSigner

db = SQLAlchemy()


logger = logging.getLogger(__name__)
migrate = Migrate()


def configure_logger(app):
    if not logger.handlers:
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(app.config['LOGS_LEVEL'])
        logger.addHandler(ch)


def create_app(config_var=os.getenv('DEPLOY_ENV', 'Development')):
    app = Flask(__name__)
    app.config.from_object('lusers.config.%sConfig' % config_var)

    configure_logger(app)
    app.signer = TimestampSigner(app.config['SIGNER_KEY'])

    db.init_app(app)

    """ Import models to be used by alembic
    from .models.email import template, message

    _module_dir = os.path.dirname(os.path.abspath(__file__))
    migrate.init_app(app, db, directory=os.path.join(_module_dir, '..', 'migrations')) """

    from lusers.views.api import api

    app.register_blueprint(api)

    # install error handler for views
    error_codes = [400, 401, 403, 404, 405, 406, 408, 409, 410, 412, 415, 428, 429, 500, 501]
    install_error_handlers(error_codes, app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
        return response

    @app.route('/', methods=['GET'])
    @app.route('/health', methods=['GET'])
    def index():
        return 'TV GLOBO Login API '

    return app
