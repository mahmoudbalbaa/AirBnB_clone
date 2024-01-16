#!/usr/bin/python3
"""
An interactive console
"""

import json
import cmd
import shlex
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

    def empty_line(self):
        """
        Do nothing when an empty line is entered
        """
        pass

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def help_quit(self):
        """
        Quit command docs
        """
        print("Quit command to exit the program\n")

    def do_EOF(self, arg):
        """
        EOF command to exit the program
        """
        print()
        return True

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

    def do_update(self, arg):
        """
        Updates an instance based on the class
        name and id by adding or updating an attribute.
        usage: update <class name> <id> <attribute name> "<attribute value>"
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
            if key not in objects:
                print("** no instance found **")
            elif len(commands) < 3:
                print("** attribute name missing **")
            elif len(commands) < 4:
                print("** value missing **")
            else:
                obj = objects[key]

                attr_name = commands[2]
                attr_value = commands[3]

                try:
                    attr_value = json.loads(attr_value)
                except JSONDecodeError:
                    pass
                setattr(obj, attr_name, attr_value)

                obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
