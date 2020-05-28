# app/__init__.py
"""
Import packages
"""
from flask_restplus import Api
from flask import Blueprint

from .main.service import api as index

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='STAR WARS REST API'
          )

api.add_namespace(index, path='/index')