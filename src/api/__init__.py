from api.config import Config
from flask import Flask


def create_app(config_class=Config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)
    app.config['SECRET_KEY'] = '17276c20537c1daa27e80f9acd7a95e0'

    from api.routes import api_bp
    app.register_blueprint(api_bp)

    return app
