import os


class Config:
    API_HOST = os.environ.get('API_HOST', '0.0.0.0')
    API_PORT = os.environ.get('API_PORT', 5000)

    SECRET_KEY = '17276c20537c1daa27e80f9acd7a95e0'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///face.db'

    GUNICORN_BIND = f'{API_HOST}:{API_PORT}'
