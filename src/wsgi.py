from gunicorn.app.wsgiapp import WSGIApplication

from api.__init__ import create_app
from api.config import Config


class WSGIServer(WSGIApplication):

    def init(self, parser, opts, args):
        pass

    def load(self):
        return create_app(Config)

    def load_config(self):
        for key, value in vars(Config).items():
            if key.startswith('GUNICORN_'):
                gunicorn_setting = key[9:].lower()
                self.cfg.set(gunicorn_setting, value)
        super().load_config()


if __name__ == '__main__':
    WSGIServer('python wsgi.py [OPTIONS]').run()
