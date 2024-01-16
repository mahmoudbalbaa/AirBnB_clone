#!/usr/bin/python3

"""
This file defines the BaseModel class which will
serve as the base of our model.
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initializes the instance's attributes."""

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
            current_time = datetime.utcnow()
            self.id = str(uuid.uuid4())
            self.created_at = current_time
            self.updated_at = current_time
            models.storage.new(self)

    def save(self):
        """this is save method that updates update_at"""

        self.updated_at = datetime.utcnow()
        models.storage.save()
        pass

    def to_dict(self):
        """Generate a new dict with an extra field __class__"""

        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()

        return inst_dict

    def __str__(self):
        """Returns a string representation of the instance."""

        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
