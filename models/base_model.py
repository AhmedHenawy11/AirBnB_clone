#!/usr/bin/python3
"""This module defines a base class to be inherited for all models in our project"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """A base class for all  models"""

    def __init__(self, *args, **kwargs):
        """ Instantiation of each object created """
        date_format = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for key, value in kwargs.items():
                if "created_at" == key:
                    self.created_at = datetime.strptime(kwargs["created_at"],
                                                        date_format)
                elif "updated_at" == key:
                    self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                        date_format)
                elif "__class__" == key:
                    pass
                else:
                    setattr(self, key, value)
        else:
            from models import storage
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ Representational method of the instance """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__ of the instance """
        dict = self.__dict__
        dict.update({'__class__': type(self).__name__})
        dict['created_at'] = self.created_at.isoformat()
        dict['updated_at'] = self.updated_at.isoformat()
        return dict
