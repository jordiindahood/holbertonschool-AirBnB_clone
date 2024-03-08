#!/usr/bin/python3
"""
BaseModel module

This module defines the BaseModel class,
which serves as the base class for other classes.
"""

from models import storage
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    BaseModel class represents the base model
    for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if kwargs:
            format_of_date = "%Y-%m-%dT%H:%M:%S.%f"
            for ky, vl in kwargs.items():
                if ky not in ["__class__", "created_at", "updated_at"]:
                    setattr(self, ky, vl)
                if ky in {"created_at", "updated_at"}:
                    setattr(self, ky, datetime.strptime(vl, format_of_date))
        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            storage.new(self)

    def save(self):
        """
        Updates the updated_at attribute to the
        current datetime and saves the instance.
        """
        self.updated_at = datetime.utcnow()
        storage.save()

    def to_dict(self):
        """
        Converts the BaseModel instance to a dictionary.

        Returns:
            dict: Dictionary representation of the instance.
        """
        my_dictionary = self.__dict__.copy()
        my_dictionary["__class__"] = self.__class__.__name__
        my_dictionary["created_at"] = self.created_at.isoformat()
        my_dictionary["updated_at"] = self.updated_at.isoformat()
        return my_dictionary

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.

        Returns:
            str: String representation.
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
