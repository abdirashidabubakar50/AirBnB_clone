#!/usr/bin/python3
""" This module defines a program that contains the entry point of the
command interpreter
"""
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True
    
    def do_EOF(self):
        """Exit the command interpreter on EOF"""
        print()
        return True
    
    def emptyline(self):
        """Override the empty line behaviour to do nothing."""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()