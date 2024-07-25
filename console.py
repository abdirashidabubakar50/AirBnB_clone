#!/usr/bin/python3
""" This module defines a program that contains the entry point of the
command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB project"""
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
