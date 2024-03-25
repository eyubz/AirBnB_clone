#!/usr/bin/python3
""" Tests for review class """
from datetime import datetime, timedelta
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """ A class to test review """

    """ Test review object """
    def test_review(self):
        """ Test city object attributes and its inheritance from basemodel"""

        review1 = Review()
        review2 = Review()

        self.assertTrue(issubclass(Review, BaseModel))
        self.assertNotEqual(review1, review2)
        self.assertIsInstance(review1, Review)
        self.assertIsInstance(review1, BaseModel)

        self.assertTrue(hasattr(review1, "id"))
        self.assertTrue(hasattr(review1, "created_at"))
        self.assertTrue(hasattr(review1, "updated_at"))
        self.assertTrue(hasattr(review1, "__str__"))
        self.assertTrue(hasattr(review1, "save"))
        self.assertTrue(hasattr(review1, "to_dict"))
        self.assertTrue(hasattr(review1, "place_id"))
        self.assertTrue(hasattr(review1, "user_id"))
        self.assertTrue(hasattr(review1, "text"))

    """ Test attribute place_id """
    def test_place_id(self):
        """ Test whether place_id is an empty string by default
        ans also it is an instance of str """

        review1 = Review()
        self.assertTrue(review1.place_id == "")
        self.assertIsInstance(review1.place_id, str)

    """ Test attribute user_id """
    def test_user_id(self):
        """ Test whether user_id is an empty string by default
        ans also it is an instance of str """

        review1 = Review()
        self.assertTrue(review1.user_id == "")
        self.assertIsInstance(review1.user_id, str)

    """ Test attribute text """
    def test_text(self):
        """ Test whether text is an empty string by default
        ans also it is an instance of str """

        review1 = Review()
        self.assertTrue(review1.text == "")
        self.assertIsInstance(review1.text, str)
