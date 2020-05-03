from api.config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import scoped_session, sessionmaker


db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    from api.routes import api_bp
    app.register_blueprint(api_bp)
    db.init_app(app)

    with app.app_context():
        db.create_all()
        session = scoped_session(sessionmaker())
        metadata = MetaData('sqlite:///face.db')
    return app
