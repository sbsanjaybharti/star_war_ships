#!/usr/bin/env python3
"""
Import packages
"""
from functools import wraps
from flask_testing import TestCase
from app.main import create_app


# Class for basic setup for testing which can be use as a base class
class BaseTestCase(TestCase):
    """ Base Tests """
    def create_app(self):
        app = create_app('testing')
        return app

def existsin(namespace):
    """Given a namespace, this decorator asserts that an object with
    the same name as the function it's wrapping (minus ) exists in that
    namespace"""
    def wrapper(namedunittest):
        assert namedunittest.__name__.startswith('test_class_have_method_'), \
            "The wrapped '%s' function doesn't look like a unit test" % namedunittest.__name__

        @wraps(namedunittest)
        def inner(self, *args, **kwargs):
            self.assertTrue(
                hasattr(
                    namespace,
                    namedunittest.__name__.split('_class_have_method_')[1])
            )
            return namedunittest(self, *args, **kwargs)
        return inner
    return wrapper