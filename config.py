from distutils.debug import DEBUG
import os
from os import environ
from unittest.mock import DEFAULT

class Config(object):

    DEBUG = False
    TESTING = False

    basedir = os.path.abspath(os.path.dirname(__file__))

    SECRET_KEY = "this_is_secrete_key"

    UPLOAD = 'D:\COURSE\Personal Projects\Mini Projects\Text Extract From Image\app\static\uploads'

    SESSION_COOKIE_SECURE = True
    DEFAULT_THEME = None

class DevelopmentConfig(Config):
    DEBUG = True
    SESSION_COOKIE_SECURE = False

class DebugConfig(Config):
    DEBUG = True