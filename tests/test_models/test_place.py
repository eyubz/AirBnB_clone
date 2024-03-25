#!/usr/bin/python3
""" Tests for state place """
from datetime import datetime, timedelta
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """ A class to test Place """

    """ Test place object """
    def test_place(self):
        """ Test place object attributes and its inheritance from basemodel"""

        place1 = Place()
        place2 = Place()

        self.assertTrue(issubclass(Place, BaseModel))
        self.assertNotEqual(place1, place2)
        self.assertIsInstance(place1, Place)
        self.assertIsInstance(place1, BaseModel)

        self.assertTrue(hasattr(place1, "id"))
        self.assertTrue(hasattr(place1, "created_at"))
        self.assertTrue(hasattr(place1, "updated_at"))
        self.assertTrue(hasattr(place1, "__str__"))
        self.assertTrue(hasattr(place1, "save"))
        self.assertTrue(hasattr(place1, "to_dict"))
        self.assertTrue(hasattr(place1, "city_id"))
        self.assertTrue(hasattr(place1, "user_id"))
        self.assertTrue(hasattr(place1, "name"))
        self.assertTrue(hasattr(place1, "description"))
        self.assertTrue(hasattr(place1, "number_rooms"))
        self.assertTrue(hasattr(place1, "number_bathrooms"))
        self.assertTrue(hasattr(place1, "max_guest"))
        self.assertTrue(hasattr(place1, "price_by_night"))
        self.assertTrue(hasattr(place1, "latitude"))
        self.assertTrue(hasattr(place1, "longitude"))
        self.assertTrue(hasattr(place1, "amenity_ids"))

    """ Test attribute name"""
    def test_name(self):
        """ Test whether name is an empty string by default
        ans also it is an instance of str """

        place1 = Place()
        self.assertTrue(place1.name == "")
        self.assertIsInstance(place1.name, str)

    """ Test attribute city_id"""
    def test_city_id(self):
        """ Test whether test_city_id is an empty string by default
        ans also it is an instance of str """

        place1 = Place()
        self.assertTrue(place1.city_id == "")
        self.assertIsInstance(place1.city_id, str)

    """ Test attribute user_id"""
    def test_user_id(self):
        """ Test whether use_id is an empty string by default
        and also it is an instance of str """

        place1 = Place()
        self.assertTrue(place1.user_id == "")
        self.assertIsInstance(place1.user_id, str)

    """ Test attribute description """
    def test_description(self):
        """ Test whether descriprtion is an empty string by default
        and also it is an instance of str """

        place1 = Place()
        self.assertTrue(place1.description == "")
        self.assertIsInstance(place1.description, str)

    """ Test attribute number_rooms"""
    def test_number_rooms(self):
        """ Test whether number_rooms is a zero by default
        and also it is an instance of int """

        place1 = Place()
        self.assertTrue(place1.number_rooms == 0)
        self.assertIsInstance(place1.number_rooms, int)

    """ Test attribute number_bathrooms """
    def test_number_bathrooms(self):
        """ Test whether number_bathrooms is a zero string by default
        and also it is an instance of int """

        place1 = Place()
        self.assertTrue(place1.number_bathrooms == 0)
        self.assertIsInstance(place1.number_bathrooms, int)

    """ Test attribute max_guest """
    def test_max_guest(self):
        """ Test whether max_guest is a zero by default
        and also it is an instance of int """

        place1 = Place()
        self.assertTrue(place1.max_guest == 0)
        self.assertIsInstance(place1.max_guest, int)

    """ Test attribute price_by_night """
    def test_price_by_night(self):
        """ Test whether price_by_night is a zero by default
        and also it is an instance of int """

        place1 = Place()
        self.assertTrue(place1.price_by_night == 0.)
        self.assertIsInstance(place1.price_by_night, int)

    """ Test attribute latitude """
    def test_latitude(self):
        """ Test whether latitude is an empty string by default
        and also it is an instance of float """

        place1 = Place()
        self.assertTrue(place1.latitude == 0.0)
        self.assertIsInstance(place1.latitude, float)

    """ Test attribute longitude """
    def test_longitude(self):
        """ Test whether longitude is an empty string by default
        and also it is an instance of float """

        place1 = Place()
        self.assertTrue(place1.longitude == 0.0)
        self.assertIsInstance(place1.longitude, float)

    """ Test attribute amenity_ids """
    def test_amenity_ids(self):
        """ Test whether amenity_ids is an empty string by default
        and also it is an instance of list """

        place1 = Place()
        self.assertTrue(place1.amenity_ids == [])
        self.assertIsInstance(place1.amenity_ids, list)
