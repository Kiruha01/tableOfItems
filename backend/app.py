from flask import Flask
from models import db, Item
from items_module import items_page

import config


def create_app():
    app = Flask(__name__)

    app.config.from_object(config.Config)
    db.init_app(app)

    app.register_blueprint(items_page, url_prefix='/api/items/')

    @app.cli.command('fill-db')
    def fill_db():
        from sqlalchemy.sql import text
        file = open("data.sql")
        query = text(file.read())
        db.engine.execute(query)

    with app.app_context():
        db.create_all()  # Create sql tables for our data models

    return app
