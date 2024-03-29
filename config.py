import os
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.googlemail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in \
        ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    HIUSMAGIA_MAIL_SUBJECT_PREFIX = '[Hiusmagia]'
    HIUSMAGIA_MAIL_SENDER = 'HIUSMAGIA <hiusmagia@example.com>'
    HIUSMAGIA_ADMIN = os.environ.get('HIUSMAGIA_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_recycle': 120
    }
    #SQLALCHEMY_DATABASE_URI = os.environ.get('CLEARDB_DATABASE_URL')
    #SQLALCHEMY_ECHO = "debug"
    #WTF_CSRF_ENABLED = False 


    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
    #    'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    SQLALCHEMY_DATABASE_URI = 'mysql://'+os.environ.get('MYSQL_USER')+':'+os.environ.get('MYSQL_PASSWORD')+'@'+os.environ.get('MYSQL_HOST')+'/'+os.environ.get('MYSQL_DB')
class TestingConfig(Config):
    TESTING = True
    # SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
    #    'sqlite://'
    SQLALCHEMY_DATABASE_URI = 'mysql://'+os.environ.get('MYSQL_USER')+':'+os.environ.get('MYSQL_PASSWORD')+'@'+os.environ.get('MYSQL_HOST')+'/'+os.environ.get('MYSQL_DB')

class ProductionConfig(Config):
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #     'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    SQLALCHEMY_DATABASE_URI = 'mysql://'+os.environ.get('MYSQL_USER')+':'+os.environ.get('MYSQL_PASSWORD')+'@'+os.environ.get('MYSQL_HOST')+'/'+os.environ.get('MYSQL_DB')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
