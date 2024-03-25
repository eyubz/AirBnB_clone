#!/usr/bin/python3
""" Tests for city class """
from datetime import datetime, timedelta
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """ A class to test city """

    """ Test state object """
    def test_city(self):
        """ Test city object attributes and its inheritance from basemodel"""

        city1 = City()
        city2 = City()

        self.assertTrue(issubclass(City, BaseModel))
        self.assertNotEqual(city1, city2)
        self.assertIsInstance(city1, City)
        self.assertIsInstance(city, BaseModel)

        self.assertTrue(hasattr(city1, "id"))
        self.assertTrue(hasattr(city1, "created_at"))
        self.assertTrue(hasattr(city1, "updated_at"))
        self.assertTrue(hasattr(city1, "__str__"))
        self.assertTrue(hasattr(city1, "save"))
        self.assertTrue(hasattr(city1, "to_dict"))
        self.assertTrue(hasattr(city1, "name"))
        self.assertTrue(hasattr(city1, "state_id"))

    """ Test attribute name"""
    def test_name(self):
        """ Test whether name is an empty string by default
        ans also it is an instance of str """

        city1 = City()
        self.assertTrue(city1.name == "")
        self.assertIsInstance(city1.state_id, str)
