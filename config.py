from dotenv import load_dotenv

from os import path, environ

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    """
    Setting Flask config variables
    """
    TESTING = True
    DEBUG = True
    FLASK_ENV = 'development'
    SECRET_KEY = environ.get('SECRET_KEY')

    # Database
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    password = environ.get('password')
    BOOKS_PER_PAGE = 5
