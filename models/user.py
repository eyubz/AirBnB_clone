#!/usr/bin/python3
""" This module contains a User class """
from models.base_model import BaseModel


class User(BaseModel):
    """ A class defining a user

    Attributes:
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    """ Constructor """
    def __init__(self):
        """ Call superclass constructor """
        super().__init__()
