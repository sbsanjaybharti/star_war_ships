#!/usr/bin/env python3
"""
Import packages
"""
from flask import jsonify
from flask_restplus import Resource
from flask_restplus import Namespace
from .service import StarWarsAPI, StarWars

api = Namespace('Index', description='index is the home page of application')

@api.route('/')
class index(Resource):
    @api.doc('Get list of Star Wars starships')
    def get(self):
        """Home page"""
        result = StarWars().starships().list()

        response_object = {
            'code': '200',
            'type': 'Response',
            'message': 'test setting',
            'result': result
        }
        return jsonify(response_object)
