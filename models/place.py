#!/usr/bin/python3
""" This module contains a place class """
from models.base_model import BaseModel


class Place(BaseModel):
    """ A class defining place

    Attributes:
        city_id (str): the id of the city
        user_id (str): user is
        name (str): name of place
        description (str): place description
        number_rooms (int): number of nu,ber rooms
        number_bathrooms (int): number of bathroom
        max_guest (int): number of guest
        price_by_night (int): price
        latitude (float): latitude position
        longitude (float): longtiude position
        amenity_ids (list): list of amenity ids
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
