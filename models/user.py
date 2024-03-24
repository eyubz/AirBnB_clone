#!/usr/bin/python3
""" This modeule contains a User class """
from models.base_model import BaseModel


class User(BaseModel):
    """ A class defining a user """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
