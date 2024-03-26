#!/usr/bin/python3
""" a class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances """
import json
from models.base_model import BaseModel

class FileStorage:
    """ This is a storage engine for AirBnB clone project
    Class Methods:
        all: Returns the object
        new: updates the dictionary id
        save: Serializes, or converts Python objects into JSON strings
        reload: Deserializes, or converts JSON strings into Python objects.
    Class Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
        class_dict (dict): A dictionary of all the classes.
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        FileStorage.__objects.update({obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as file:
            dict = {}
            dict.update(FileStorage.__file_path)
            for key, object in self.__objects

