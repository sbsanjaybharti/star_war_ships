#!/usr/bin/env python3
"""
Import packages
"""

from base import BaseTestCase, existsin
from app.main.service import StarWarsAPI

class TestStarWarsAPIMethodExist(BaseTestCase):
    """Test the class exist status"""

    @existsin(StarWarsAPI)
    def test_class_have_method_get_list(self):
        """--> class:StarWarsAPI -> method:get_list exists"""

    @existsin(StarWarsAPI)
    def test_class_have_method_get_single(self):
        """--> class:StarWarsAPI -> method:get_single exists"""


class TestStarWarsMethod(BaseTestCase):
    """Test class methods"""

    def test_method_get_list(self):
        """--> class:StarWarsAPI -> method:get_list status"""
        api = StarWarsAPI('starships')
        response = api.get_list()
        self.assertIsInstance(response, object)
        self.assertEqual(type(response), dict)
        self.assertGreater(response['count'], 0)
        self.assertEqual(type(response['results']), list)

    def test_method_get_single(self):
        """--> class:StarWarsAPI -> method:single_film status"""
        api = StarWarsAPI('starships')
        self.assertIsInstance(api.get_single(9), object)
        self.assertEqual(type(api.get_single(9)), dict)
