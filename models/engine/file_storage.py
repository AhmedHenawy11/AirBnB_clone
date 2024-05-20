# #!/usr/bin/python3
# """ a class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances """
#
# import json
#
#
# class FileStorage:
#     """a class  that serializes instances to a JSON file and deserializes JSON file to instances"""
#     __file_path = "file.json"
#     __objects = {}
#
#     def all(self):
#         """returns the dictionary __objects"""
#         return FileStorage.__objects
#
#     def new(self, obj):
#         """sets in __objects the obj with key <obj class name>.id"""
#         key = f'{obj.__class__.__name__}.{obj.id}'
#         self.__objects[key] = obj
#
#     def save(self):
#         """serializes __objects to the JSON file (path: __file_path)"""
