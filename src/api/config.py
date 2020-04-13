import os


class Config:
    API_HOST = os.environ.get('API_HOST', '0.0.0.0')
    API_PORT = os.environ.get('API_PORT', 5000)
