#!/usr/bin/python3
""" This module contains amenity class """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ A class defining amenity

    Attributes:
        name (str): name of the state
    """
    name = ""
