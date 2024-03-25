#!/usr/bin/python3
""" Tests for state class """
from datetime import datetime, timedelta
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """ A class to test State """

    """ Test state object """
    def test_state(self):
        """ Test state object attributes and its inheritance from basemodel"""

        state1 = State()
        state2 = State()

        self.assertTrue(issubclass(State, BaseModel))
        self.assertNotEqual(state1, state2)
        self.assertIsInstance(state1, State)
        self.assertIsInstance(state1, BaseModel)

        self.assertTrue(hasattr(state1, "id"))
        self.assertTrue(hasattr(state1, "created_at"))
        self.assertTrue(hasattr(state1, "updated_at"))
        self.assertTrue(hasattr(state1, "__str__"))
        self.assertTrue(hasattr(state1, "save"))
        self.assertTrue(hasattr(state1, "to_dict"))
        self.assertTrue(hasattr(state1, "name"))

    """ Test attribute name"""
    def test_name(self):
        """ Test whether name is an empty string by default
        ans also it is an instance of str """

        state1 = State()
        self.assertTrue(state1.name == "")
        self.assertIsInstance(state1.name, str)
