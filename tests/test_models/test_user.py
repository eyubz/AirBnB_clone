#!/usr/bin/python3
""" Tests for user class """
from datetime import datetime, timedelta
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """ A class to test User """

    """ Test user object """
    def test_userObject(self):
        """ Test Use object attributes and its inheritance from basemodel"""

        user1 = User()
        user2 = User()

        self.assertTrue(issubclass(User, BaseModel))
        self.assertNotEqual(user1, user2)
        self.assertIsInstance(user1, User)
        self.assertIsInstance(user1, BaseModel)

        self.assertTrue(hasattr(user1, "id"))
        self.assertTrue(hasattr(user1, "created_at"))
        self.assertTrue(hasattr(user1, "updated_at"))
        self.assertTrue(hasattr(user1, "__str__"))
        self.assertTrue(hasattr(user1, "save"))
        self.assertTrue(hasattr(user1, "to_dict"))
        self.assertTrue(hasattr(user1, "email"))
        self.assertTrue(hasattr(user1, "password"))
        self.assertTrue(hasattr(user1, "first_name"))
        self.assertTrue(hasattr(user1, "last_name"))

    """ Test attribut id"""
    def test_id(self):
        """ Test whether two objets have different id.
        Tese whether id is an instance of string """

        user1 = User()
        user2 = User()

        self.assertIsInstance(user1.id, str)
        self.assertNotEqual(user1.id, user2.id)
