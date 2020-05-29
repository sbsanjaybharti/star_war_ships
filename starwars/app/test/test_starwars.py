#!/usr/bin/env python3
"""
Import packages
"""
import collections

from base import BaseTestCase, existsin
from app.main.service import StarWars, StarWarsAPI

class TestStarWarsMethodExist(BaseTestCase):
    """Test the class exist status"""

    @existsin(StarWars)
    def test_class_have_method_group(self):
        """--> class:StarWars -> method:group exists"""

    @existsin(StarWars)
    def test_class_have_method_starships(self):
        """--> class:StarWars -> method:starships exists"""

    @existsin(StarWars)
    def test_class_have_method_get(self):
        """--> class:StarWars -> method:starships exists"""

    @existsin(StarWars)
    def test_class_have_method_get_fields(self):
        """--> class:StarWars -> method:get_fields exists"""

    @existsin(StarWars)
    def test_class_have_method_page(self):
        """--> class:StarWars -> method:page exists"""

    @existsin(StarWars)
    def test_class_have_method_list(self):
        """--> class:StarWars -> method:list exists"""


class TestStarWarsMethod(BaseTestCase):
    """Test class methods"""
    #
    # def test_method_starships(self):
    #     """--> class:StarWars -> method:starships status"""
    #     api = StarWars()
    #     response = api.get_list()
    #     self.assertIsInstance(response, object)
    #     self.assertEqual(type(response), dict)
    #     self.assertGreater(response['count'], 0)
    #     self.assertEqual(type(response['results']), list)

    def test_method_group(self):
        """--> class:StarWarsAPI -> method:group status"""
        api = StarWars()
        data = [
            {
                "name": "CR90 corvette",
                "hyperdrive_rating": "2.0"
            },
            {
                "name": "Star Destroyer",
                "hyperdrive_rating": "2.0"
            },
            {
                "name": "Sentinel-class landing craft",
                "hyperdrive_rating": "1.0",
            },
            {
                "name": "Death Star",
                "hyperdrive_rating": "4.0",
            },
            {
                "name": "Millennium Falcon",
                "hyperdrive_rating": "0.5"
            },
            {
                "name": "Y-wing",
                "hyperdrive_rating": "1.0",
            },
            {
                "name": "X-wing",
                "hyperdrive_rating": "1.0"
            },
            {
                "name": "TIE Advanced x1",
                "hyperdrive_rating": "1.0",
            },
            {
                "name": "Executor",
                "hyperdrive_rating": "2.0",
            },
            {
                "name": "Rebel transport",
                "hyperdrive_rating": "4.0"
            }
        ]
        response = {
            '4.0': [
                {'name': 'Rebel transport', 'hyperdrive': '4.0'},
                {'name': 'Death Star', 'hyperdrive': '4.0'}
            ],
            '2.0': [
                {'name': 'Executor', 'hyperdrive': '2.0'},
                {'name': 'Star Destroyer', 'hyperdrive': '2.0'},
                {'name': 'CR90 corvette', 'hyperdrive': '2.0'}
            ],
            '1.0': [
                {'name': 'TIE Advanced x1', 'hyperdrive': '1.0'},
                {'name': 'X-wing', 'hyperdrive': '1.0'},
                {'name': 'Y-wing', 'hyperdrive': '1.0'},
                {'name': 'Sentinel-class landing craft', 'hyperdrive': '1.0'}
            ],
            '0.5': [
                {'name': 'Millennium Falcon', 'hyperdrive': '0.5'}
            ]
        }
        api.group(data)
        self.assertEqual(api.get()['starships'], response)
        self.assertEqual(api.get()['starships_unknown_hyperdrive'], [])
    def test_method_null_group(self):
        """--> class:StarWarsAPI -> method:group status"""
        api = StarWars()
        data = [
            {
                "name": "CR90 corvette",
                "hyperdrive_rating": "unknown"
            },
            {
                "name": "Star Destroyer",
                "hyperdrive_rating": "unknown"
            }
        ]
        api.group(data)
        self.assertNotEqual(api.get()['starships_unknown_hyperdrive'], [])

    def test_method_page(self):
        """--> class:StarWarsAPI -> method:page status"""
        api = StarWars()
        data = {
            "count": 36,
            "next": "http://swapi.dev/api/starships/?page=1",
            "previous": 'null',
            "results": []
        }
        self.assertEqual(api.page(StarWarsAPI('starships').get_list(), 1), None)

        self.assertEqual(api.page(StarWarsAPI('starships').get_list(), 1), None)

    def test_method_field(self):
        """--> class:StarWarsAPI -> method:fields status"""
        api = StarWars()
        data = {
            "name": "Executor",
            "hyperdrive_rating": "2.0",
            "MGLT": "40",
            "starship_class": "Star dreadnought",
            "pilots": [],
            "films": [
                "http://swapi.dev/api/films/2/",
                "http://swapi.dev/api/films/3/"
            ],
            "created": "2014-12-15T12:31:42.547000Z",
            "edited": "2014-12-20T21:23:49.893000Z",
            "url": "http://swapi.dev/api/starships/15/"
        }
        response = api.get_fields(data)
        self.assertEqual(type(response), dict)
        self.assertListEqual(list(response.keys()), ['name', 'hyperdrive'])

    def test_method_list_null(self):
        """--> class:StarWarsAPI -> method:list status"""
        api = StarWars()
        response = api.list()
        self.assertEqual(type(response), dict)
        self.assertListEqual(list(response.keys()), ['starships', 'starships_unknown_hyperdrive'])
        self.assertEqual(type(response['starships']), list)
        self.assertEqual(type(response['starships_unknown_hyperdrive']), list)

