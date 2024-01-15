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

    _time_format = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """Initializes the instance's attributes."""
        if kwargs:
            kwargs.pop("__class__", None)
            for key in ['_created_at', '_updated_at']:
                if key in kwargs:
                    kwargs[key] = \
                            datetime.strptime(kwargs[key], self._time_format)
            self.__dict__.update(kwargs)
        else:
            current_time = datetime.utcnow()
            self._id = str(uuid.uuid4())
            self._created_at = current_time
            self._updated_at = current_time
            models.storage.new(self)

    def save(self):
        """Updates the _updated_at attribute and saves to storage."""
        self._updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """Generate a new dict with an extra field __class__."""
        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["_created_at"] = self._created_at.isoformat()
        inst_dict["_updated_at"] = self._updated_at.isoformat()
        return inst_dict

    def __str__(self):
        """Returns a string representation of the instance."""
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self._id}) {self.short_summary()}"
