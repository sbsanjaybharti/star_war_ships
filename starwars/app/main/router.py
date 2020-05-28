#!/usr/bin/env python3
"""
Import packages
"""
from flask import jsonify
from flask_restplus import Resource
from flask_restplus import Namespace
from .service import StarWarsAPI, StarWars

api = Namespace('Index', description='List of StarWarsShips based on rating')

@api.route('/')
class index(Resource):
    @api.doc('Get list of Star Wars starships')
    def get(self):
        """Get List"""
        result = StarWars().starships().list()

        response_object = {
            'code': '200',
            'type': 'Response',
            'message': 'test setting',
            'result': result
        }
        return jsonify(result)
