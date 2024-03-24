#!/usr/bin/python3
""" A file storage module """
import json
from models.base_model import BaseModel
form models.user import User

class FileStorage:
    """ A file storage class """
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
        o = FileStorage.__objects
        obj_dict = {key: obj.to_dict() for key, obj in o.items()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(obj_dict, file)

    """ Read the data from a file. """
    def reload(self):
        """ Reload the data in the file and store it to __objcts
        dictionary """
        try:
            with open(FileStorage.__file_path, "r") as file:
                obj_dict = json.load(file)
                for values in obj_dict.values():
                    class_name = values["__class__"]
                    del values["__class__"]
                    self.new(eval(class_name)(**values))
        except FileNotFoundError:
            return
