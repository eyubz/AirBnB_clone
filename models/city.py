#!/usr/bin/python3
""" This module contains a city class """
from models.base_model import BaseModel


class City(BaseModel):
    """ A class defining a city

    Attributes:
        name (str): name of the state
        state_id (str): Id of state
    """
    name = ""
    state_id = ""
