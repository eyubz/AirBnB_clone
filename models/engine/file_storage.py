#!/usr/bin/python3
""" A file storage module """
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ A file storage class
    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    """ Return dictionary"""
    def all(self):
        """ Return the dictionary __objects
        Returns:
            Dictionary __objects
        """
        return FileStorage.__objects

    """ Update the dictionary __objects"""
    def new(self, obj):
        """ Update the dictionary __objects with key
        <obj class name>.id and a value obj

        Args:
            arg1: an object
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    """ Write to a file """
    def save(self):
        """ Write the dictionary __objects to a file """
        new_dict = {}
        o = FileStorage.__objects
        for k, v in o.items():
            new_dict[k] = v.to_dict()
        with open(FileStorage.__file_path, "w") as file:
            json.dump(new_dict, file)

    """ Read the data from a file. """
    def reload(self):
        """ Reload the data in the file and store it to __objcts
        dictionary """
        try:
            with open(FileStorage.__file_path) as file:
                obj_dict = json.load(file)
                for key, values in obj_dict.items():
                    class_name = values["__class__"]
                    new_obj = self.new(eval(class_name)(**values))
                    FileStorage.__objects[key] = new_obj
        except FileNotFoundError:
            return
