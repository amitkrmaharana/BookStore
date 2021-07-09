import redis
from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint

from os import path, environ

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

db = SQLAlchemy()
migrate = Migrate()
redis_cache = redis.Redis(host=environ.get('REDIS_HOST'), port=environ.get('REDIS_PORT'), db=environ.get('REDIS_DB'))


def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    # app.config['SQLALCHEMY_ECHO'] = False
    # Initialize Plugins
    db.init_app(app)
    migrate.init_app(app, db)

    # swagger specific
    swagger_url = '/swagger'
    api_url = '/static/swagger.json'
    swagger_blueprint = get_swaggerui_blueprint(
        swagger_url,
        api_url,
        config={
            'app_name': "Book Store"
        }
    )

    with app.app_context():
        # Include our Routes
        import api
        # Register Blueprints
        app.register_blueprint(swagger_blueprint, url_prefix=swagger_url)
        app.register_blueprint(api.book_store)

    return app
