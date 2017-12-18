



class BaseConfig(object):
    SECRET_KEY = 'secret'
    DEBUG = True
    PYTHONPATH = '/Users/omarelmohri/Documents/Python/Samples/test_flask_before_request'

    @staticmethod
    def init_app(app):
        pass


config = {
    'default': BaseConfig
}