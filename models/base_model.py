#!/usr/bin/python3
"""
This module defines the BaseModel class which serves as the base for other models.
"""

from datetime import datetime
import uuid
from models import storage


class BaseModel:
    """
    Defines all common attributes/methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the instance's attributes.
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            # Remove the class name from kwargs if present
            kwargs.pop("__class__", None)
            # Convert datetime strings to objects
            for key in ['created_at', 'updated_at']:
                if key in kwargs:
                    kwargs[key] = datetime.strptime(kwargs[key], time_format)
            self.__dict__.update(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.utcnow()
            storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the 'updated_at' attribute with the current datetime.
        """
        self.updated_at = datetime.utcnow()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of the instance's __dict__.
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat() + 'Z'
        new_dict["updated_at"] = self.updated_at.isoformat() + 'Z'
        return new_dict

