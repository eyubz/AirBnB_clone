#!/usr/bin/python3
""" A module containing base_model class """
from datetime import datetime
import models
from uuid import uuid4


class BaseModel:
    """ A class base model which is the base class
    for all other classes by defining basic attributes and
    functions """

    """ Constructor"""
    def __init__(self, *args, **kwargs):
        """ Initialize the class

        Args:
            arg1: list of variable number of arguments
            arg2: key-value pairs of the arguments

        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.fromisoformat(value)
                else:
                    self.__dict[key] = value
        else:
            models.storage.new(self)

    """ String representation of a class"""
    def __str__(self):
        """ Defines the string representation of the class """
        string = f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        return string

    """ Change the updated_at attribute"""
    def save(self):
        """ Update the updated_at attribute to the current time """
        self.updated_at = datetime.now()
        models.storage.save()

    """ Dictionary representation of a class"""
    def to_dict(self):
        """ Define the dictionary representation of a
        class from self.__dict__ and change the created_at
        and updated_at to their representation in iso format.
        And add __class__ key with value class name to the
        dictionary representation """
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = new_dict[key].isoformat()
        new_dict["updated_at"] = new_dict[key].isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
