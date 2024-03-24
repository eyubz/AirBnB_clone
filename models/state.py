#!/usr/bin/python3
""" This module contains a state class """
from models.base_model import BaseModel


class State(BaseModel):
    """ A class defining a state

    Attributes:
        name (str): name of the state
    """
    name = ""
    """ Constructor """
    def __init__(self):
        """ Call superclass constructor """
        super().__init__()x
