from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost/postgres"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    # Blue Print
    from .views import main, product
    app.register_blueprint(main.bp)
    app.register_blueprint(product.bp)

    return app
