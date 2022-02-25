from flask import Flask
from models import db

import config


def create_app():
    app = Flask(__name__)

    app.config.from_object(config.Config)
    db.init_app(app)

    # app.register_blueprint(locations, url_prefix='/api/locations/')

    # @app.cli.command()
    # def recreate_db():
    #     # db.drop_all()
    #     # db.create_all()
    #     pass
    #
    # @app.cli.command()
    # def create_data():
    #     pass

    # with app.app_context():
    #     db.create_all()  # Create sql tables for our data models

    return app
