# -*- coding: UTF-8 -*-
import os


class Config(object):
    ### BASE ###
    BASE_DIR = os.path.dirname(__file__)

    ### KEYS ###
    CSRF_SESSION_KEY = "secretkeylol"

    ### CSRF ###
    CSRF_ENABLED = True
    SECRET_KEY = "secretkeygglol"

    ### Folders ###
    THEME_FOLDER = os.path.join(BASE_DIR, 'themes')

    ### Babel ###
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

    ### FYSQL ###
    DATABASE = {
        'engine': 'MySQL',
        'host': 'localhost',
        'db': 'dev',
        'user': 'dev',
        'passwd': 'pwd'
    }

    ### UPLOAD ###
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    UPLOAD_DIRECTORY = os.path.join(MEDIA_ROOT, 'uploads')
    CHUNKS_DIRECTORY = os.path.join(MEDIA_ROOT, 'chunks')
    UPLOAD_DIRECTORY_URL = '/files/'

    ### DEBUG ###
    DEBUG = True
    CACHE = False

    ### CACHE ###
    CACHE_TYPE = 'memcached'  # redis, memcached, file
    CACHE_SERV = '127.0.0.1'  # 127.0.0.1, 127.0.0.1, cache/

    ### URL ###
    URL = 'http://127.0.0.1:5000/'


class ConfigProd(Config):
    DEBUG = True
    CACHE = True

del os
