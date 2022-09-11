from flask import Flask


def create_app(config_name):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///validador_abc.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    return app
