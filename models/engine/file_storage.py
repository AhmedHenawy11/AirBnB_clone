#!/usr/bin/python3
""" a class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances """

import json


class FileStorage:
    """a class  that serializes instances to a JSON file and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f'{obj.__class__.__name__}.{obj.id}'
        self.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        from models.base_model import BaseModel
        """ Reload stored objects """
        classes = {'BaseModel': BaseModel,}
        try:
            with open(FileStorage.__file_path, 'r') as file:
                data = {}
                data = json.load(file)
                for key, value in data.items():
                    self.all()[key] = classes[value['__class__']](**value)

        except FileNotFoundError:
            pass
