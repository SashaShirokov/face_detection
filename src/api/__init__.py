from api import generator
from api.models import interview_data
from api.config import Config

from flask import Flask


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    from api.routes import api_bp
    app.register_blueprint(api_bp)

    return app
