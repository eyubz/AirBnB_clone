#!/usr/bin/python3
""" This module contains review class """
from models.base_model import BaseModel


class Review(BaseModel):
    """ A class defining review

    Attributes:
        place_id (str): plce id
        user_id (str): user id
        text (str): empty string
    """
    place_id = ""
    user_id = ""
    text = ""
