#!/usr/bin/python3
""" Tests foramenity class """
from datetime import datetime, timedelta
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """ A class to test amenity """

    """ Test amenity object """
    def test_amenity(self):
        """ Test amenity object attributes and its
        inheritance from basemodel"""

        amenity1 = Amenity()
        amenity2 = Amenity()

        self.assertTrue(issubclass(Amenity, BaseModel))
        self.assertNotEqual(amenity1, amenity2)
        self.assertIsInstance(amenity1, Amenity)
        self.assertIsInstance(amenity1, BaseModel)

        self.assertTrue(hasattr(amenity1, "id"))
        self.assertTrue(hasattr(amenity1, "created_at"))
        self.assertTrue(hasattr(amenity1, "updated_at"))
        self.assertTrue(hasattr(amenity1, "__str__"))
        self.assertTrue(hasattr(amenity1, "save"))
        self.assertTrue(hasattr(amenity1, "to_dict"))
        self.assertTrue(hasattr(amenity1, "name"))

    """ Test attribute name"""
    def test_name(self):
        """ Test whether name is an empty string by default
        ans also it is an instance of str """

        amenity1 = Amenity()
        self.assertTrue(amenity1.name == "")
        self.assertIsInstance(amenity1.name, str)
