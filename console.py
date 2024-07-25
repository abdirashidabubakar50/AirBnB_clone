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
    
    def do_help(self, line):
        """Show help information."""
        # Call the parent class's help method to show default help text
        cmd.Cmd.do_help(self, line)

if __name__ == "__main__":
    HBNBCommand().cmdloop()