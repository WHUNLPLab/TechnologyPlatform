# -*- coding:utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    NEO4J_DATABASE_URI = os.environ.get('NEO4J_DATABASE_URI') or \
        'http://neo4j:password@ip:7474/db/data/'

    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')


class ProductionConfig(Config):
    NEO4J_DATABASE_URI = os.environ.get('NEO4J_DATABASE_URI') or \
        'http://neo4j:password@ip:7474/db/data/'

    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}