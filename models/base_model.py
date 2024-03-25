#!/usr/bin/python3
"""This module defines a base class to be inherited for all models in our project"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """A base class for all hbnb models"""
    def __init__(self):
        """ Instantiation of each object created """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ Representational method of the instance """
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """ Method that updates the public instance attribute updated_at with the current datetime """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__ of the instance """
        dict = self.__dict__
        dict.update({'__class__': type(self).__name__ })
        dict['created_at'] = self.created_at.isoformat()
        dict['updated_at'] = self.updated_at.isoformat()
        return dict
