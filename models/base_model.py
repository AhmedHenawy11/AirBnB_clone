#!/usr/bin/python3
"""This module defines a base class to be inherited for all models in our project"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """A base class for all  models"""

    def __init__(self):
        """Instantiation of each object created"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ Representational method of the instance """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__ of the instance """
        dictionary = self.__dict__
        dictionary.update({"__class__": type(self).__name__})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
