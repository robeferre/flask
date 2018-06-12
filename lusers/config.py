# -*- coding: utf-8 -*-
import logging
import os


class Config(object):
    SIGNER_KEY = 'R2R6DRiMK3YzmvOTioQ3'
    DEBUG = True
    TESTING = False
    LOGS_LEVEL = logging.INFO
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PASS_SALT = 'æ'
    PASS_CHARSET_ENCODE = 'ISO-8859-1'


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    pass


class DevelopmentConfig(Config):
    # SQLALCHEMY_ECHO = True

    SQLALCHEMY_DATABASE_URI = 'mysql://root:D45m7eba@tvg-databases-negocio-dev.clieq3vdmtrq.us-east-1.rds.amazonaws.com/tvg_db_users'
    S3_BUCKET = 'documents-stg'
    SIGNER_KEY = 'R2R6DRiMK3YzmvOTioQ3'


class TestingConfig(Config):
    TESTING = True
    PRODUCTION = True  # test production code
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    S3_DOCS_BUCKET = 'documents-testing'
