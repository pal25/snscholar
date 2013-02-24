import os

class BaseConfig(object):

    # Get app root path
    # ../../configs/config.py
    _basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    PROJECT = "snscholar"
    DEBUG = False
    TESTING = False

    # os.urandom(24)
    SECRET_KEY = 'secret key'


class DeveloperConfig(BaseConfig):

    DEBUG = True

    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/' + BaseConfig.PROJECT + ".db"

class ProductionConfig(BaseConfig):

    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/' + BaseConfig.PROJECT + ".db"