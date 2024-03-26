#!/usr/bin/python3
""" a class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances """
import json



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
        """Set new __objects to existing dictionary of instances"""
        key = f'{obj.__class__.__name__}.{obj.id}'
        self.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        dict = {}
        dict.update(FileStorage.__objects)
        for key, object in dict.items():
            dict[key] = object.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(dict, file)

    def reload(self):
        from models.base_model import BaseModel
        """Deserialize/convert obj dicts back to instances, if it exists"""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                new_obj_dict = json.load(f)
            for key, value in new_obj_dict.items():
                self.__objects[key] = value
        except FileNotFoundError:
            pass

