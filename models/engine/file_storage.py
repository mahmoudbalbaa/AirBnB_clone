#!/usr/bin/python3
"""
FileStorage module for storing and retrieving instances
"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    FileStorage class for storing and retrieving instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Return the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Set in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serialize __objects to the JSON file (path: __file_path)
        """
        all_objs = FileStorage.__objects
        obj_dict = {key: obj.to_dict() for key, obj in all_objs.items()}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        Deserialize the JSON file to __objects, if the file exists
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                try:
                    obj_dict = json.load(f)

                    for key, values in obj_dict.items():
                        class_name, obj_id = key.split('.')
                        cls = globals().get(class_name)

                        if cls:
                            instance = cls(**values)
                            FileStorage.__objects[key] = instance
                        else:
                            print(f"Warning: Unknown class name"
                                  f"'{class_name}' in file.")
                except Exception as e:
                    print(f"Error reloading: {e}")
