#!/usr/bin/env python3
"""
Import packages
"""
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """
    Environmental variable configurations
    """

    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')

    STAR_WARS_API = os.getenv('STAR_WARS_API')


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False


config_by_name = dict(
    development=DevelopmentConfig,
    testing=TestingConfig,
    production=ProductionConfig
)

key = Config.SECRET_KEY
