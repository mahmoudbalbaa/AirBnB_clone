#!/usr/bin/python3
"""
An interactive console
"""

import re
import json
import cmd
import shlex
import ast
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from json.decoder import JSONDecodeError


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "
    valid_classes = [
            "BaseModel",
            "User",
            "Place",
            "State",
            "City",
            "Amenity",
            "Review"
            ]

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_help(self, arg):
        """
        Quit command docs
        """
        cmd.Cmd.do_help(self, arg)

    def do_EOF(self, arg):
        """
        EOF command to exit the program
        """
        print()
        return True

    def emptyline(self):
        """
        Do nothing when an empty line is entered
        """
        pass

    def do_create(self, arg):
        """
        Create a new instance of BaseModel and save it to a JSON file.
        usage: create <class_name>
        """
        commands = shlex.split(arg)

        if not commands:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            new_instance = globals()[commands[0]]()
            storage.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Show the string representation of an instance.
        usage: show <class_name> <id>
        """
        commands = shlex.split(arg)

        if not commands:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()

            key = "{}.{}".format(commands[0], commands[1])
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.
        usage: destroy <class_name> <id>
        """
        commands = shlex.split(arg)

        if not commands:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()

            key = "{}.{}".format(commands[0], commands[1])
            if key in objects:
                del objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representations of in ba or not on the class name.
        usage: all <class_name> or all
        """
        objects = storage.all()
        commands = shlex.split(arg)

        if not commands:
            for key, value in objects.items():
                print(str(value))
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            for key, value in objects.items():
                if key.split('.')[0] == commands[0]:
                    print(str(value))

    def do_count(self, line):
        """Print the count all class instances"""
        kclass = globals().get(line, None)
        if kclass is None:
            print("** class doesn't exist **")
            return
        count = 0
        for obj in storage.all().values():
            if obj.__class__.__name__ == line:
                count += 1
        print(count)

    def default(self, line):
        """
        default behavior for cmd module when input is invalid
        """
        if line is None:
            return

        cmdPattern = "^([A-Za-z]+)\.([a-z]+)\(([^(]*)\)"
        paramsPattern = """^"([^"]+)"(?:,\s*(?:"([^"]+)"|(\{[^}]+\}))(?:,\s*(?:("?[^"]+"?)))?)?"""
        m = re.match(cmdPattern, line)
        if not m:
            super().default(line)
            return
        mName, method, params = m.groups()
        m = re.match(paramsPattern, params)
        params = [item for item in m.groups() if item] if m else []

        cmd = " ".join([mName] + params)

        if method == 'all':
            return self.do_all(cmd)

        if method == 'count':
            return self.do_count(cmd)

        if method == 'show':
            return self.do_show(cmd)

        if method == 'destroy':
            return self.do_destroy(cmd)

        if method == 'update':
            return self.do_update(cmd)

    def do_update(self, line):
        """Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary.
        usage:  update <class> <id> <attribute_name> <attribute_value> or
                <class>.update(<id>, <attribute_name>, <attribute_value>) or
                <class>.update(<id>, <dictionary>)
        """
        arr = line.split()
        if len(arr) < 1:
            print("** class name missing **")
            return
        elif arr[0] not in class_home:
            print("** class doesn't exist **")
            return
        elif len(arr) < 2:
            print("** instance id missing **")
            return
        else:
            new_str = f"{arr[0]}.{arr[1]}"
            if new_str not in storage.all().keys():
                print("** no instance found **")
            elif len(arr) < 3:
                print("** attribute name missing **")
                return
            elif len(arr) < 4:
                print("** value missing **")
                return
            else:
                setattr(storage.all()[new_str], arr[2], arr[3])
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
