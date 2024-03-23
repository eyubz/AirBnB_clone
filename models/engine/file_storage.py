#!/usr/bin/python3
""" A file storage module """
import json
import os


class FileStorage():
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
        key = f"{obj.__class__.name}.{obj.id}"
        FileStorage.__objects[key] = obj.__dict__

    """ Write to a file """   
    def save(self):
        """ Write the dictionary __objects to a file """
        with open(FileStorage.__file_path, "w") as file:
            json.dump(FileStorage.__objects, file)
    
    """ Read the data from a file. """
    def reload(self):
        """ Reload the data in the file and store it to __objcts
        dictionary """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as file:
                FileStorage.__objects = json.load(file)
