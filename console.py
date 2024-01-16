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

            key = "{}.{}".format(commands[0], commands[1])
            if key not in objects:
                print("** no instance found **")
            elif len(commands) < 3:
                print("** attribute name missing **")
            elif len(commands) < 4:
                print("** value missing **")
            else:
                obj = objects[key]
                curly_braces = re.search(r"\{(.*?)\}", arg)

                if curly_braces:
                    str_data = curly_braces.group(1)
                    arg_dict = ast.literal_eval("{" + str_data + "}")
                    attribute_names = list(arg_dict.keys())
                    attribute_values = list(arg_dict.values())
                    attr_name1 = attributes_names[0]
                    attr_value1 = attributes_values[0]
                    attr_name2 = attributes_names[1]
                    attr_value2 = attributes_values[1]

                    setattr(obj, attr_name1, attr_value1)
                    setattr(obj, attr_name2, attr_value2)
                else:

                    attr_name = commands[2]
                    attr_value = commands[3]

                    try:
                        attr_value = json.loads(attr_value)
                    except JSONDecodeError:
                        pass
                    setattr(obj, attr_name, attr_value)

                obj.save()

    def default(self, line):
        """
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



if __name__ == '__main__':
    HBNBCommand().cmdloop()
