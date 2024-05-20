#!/usr/bin/python3
"""This module defines a base class to be inherited for all models in our project"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """A base class for all  models"""

    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ Representational method of the instance """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ Stores the instance into json file """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__ of the instance """
        dicto = self.__dict__
        dicto.update({'__class__': type(self).__name__})
        dict['created_at'] = self.created_at.isoformat()
        dict['updated_at'] = self.updated_at.isoformat()
        return dicto
