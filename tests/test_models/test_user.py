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

    """ Test attribute email"""
    def test_email(self):
        """ Test whether email is an empty string by default
        ans also it is an instance of str """

        user1 = User()
        self.assertTrue(user1.email == "")
        self.assertIsInstance(user1.email, str)

    """ Test attribute password"""
    def test_password(self):
        """ Test whether password is an empty string by default
        and also an instance of str"""

        user1 = User()
        self.assertTrue(user1.password == "")
        self.assertIsInstance(user1.password, str)

    """ Test attribute frist_name"""
    def test_first_name(self):
        """ Test whether first_name is an empty string by default
        and also an instance of str"""

        user1 = User()
        self.assertTrue(user1.first_name == "")
        self.assertIsInstance(user1.first_name, str)

    """ Test attribute last_name"""
    def test_last_name(self):
        """ Test whether last_name is an empty string by default
        and also an instance of str"""

        user1 = User()
        self.assertTrue(user1.last_name == "")
        self.assertIsInstance(user1.last_name, str)
