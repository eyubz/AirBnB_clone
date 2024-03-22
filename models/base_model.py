#!/usr/bin/python3
from datetime import datetime
import uuid
""" This module contains a base class which is
the main class in which other classes inherit from """


class BaseModel():
    """ A class base model which is the base class
    for all other classes by defining basic attributes and
    functions """

    """ Constructor"""
    def __init__(self):
        """ Initialize the class

        Args:
            arg1: Description of arg1.
            arg2: Description of arg2.

        Returns:
            Description of what the function returns.
        Raises:
            ValueError: If some condition is not met.
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    """ String representation of a class"""
    def __str__(self):
        """ Defines the string representation of the class

        Args:
            arg1: Description of arg1.
            arg2: Description of arg2.

        Returns:
            The string representation of the function

        Raises:
            ValueError: If some condition is not met.
        """
        string = f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        return string

    """ Change the updated_at attribute"""
    def save(self):
        """ Update the updated_at attribute to the current time

        Args:
            arg1: Description of arg1.
            arg2: Description of arg2.

        Returns:
            Description of what the function returns.

        Raises:
            ValueError: If some condition is not met.
        """
        self.updated_at = datetime.now()

    """ Dictionary representation of a class"""
    def to_dict(self):
        """ Define the dictionary representation of a
        class from self.__dict__ and change the created_at
        and updated_at to their representation in iso format.
        And add __class__ key with value class name to the
        dictionary representation

        Args:
            arg1: Description of arg1.
            arg2: Description of arg2.

        Returns:
            A dictionary representation of a class

        Raises:
            ValueError: If some condition is not met.
        """
        new_dict = self.__dict__
        for key in new_dict:
            if key == "created_at" or key == "updated_at":
                new_dict[key] = new_dict[key].isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
