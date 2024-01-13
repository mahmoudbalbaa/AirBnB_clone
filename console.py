#!/usr/bin/python3
"""
An interactive console
"""

import cmd


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb)"

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def help_quit(self):
        """
        Quit command docs
        """
        print("Quit command to exit the program")

    def do_EOF(self, line):
        """
        EOF command to exit the program
        """
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
