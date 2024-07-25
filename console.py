#!/usr/bin/python3
""" This module defines a program that contains the entry point of the
command interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage


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

    def do_create(self, arg):
        """creates a new instance of BaseModel, saves it
        (to the JSON file), and prints the id """
        if not arg:
            print("** class name missing **")
            return

        try:
            new_instance = eval(arg + "()")
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance based on the
        name class and id
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name, instance_id = args[0], args[1]

        try:
            cls = eval(class_name)
        except NameError:
            print("** class doesn't exist **")

        key = f"{class_name}.{instance_id}"
        instance = storage.all().get(key)

        if instance is None:
            print("** no instance found **")
        else:
            print(instance)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()

        if not arg:
            print("** class name missing **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name, instance_id = args[0], args[1]

        try:
            cls = eval(class_name)
        except NameError:
            print("** class doesn't exist")
            return

        key = f"{class_name}.{instance_id}"
        instance = storage.all().get(key)

        if instance is None:
            print("** no instance found **")
        else:
            del storage.all()[key]
            storage.save()

    def do_all(self, arg):
        """Prints the stirng representation of all instances based or not on
        the class name
        """
        if not arg:
            for instance in storage.all().values():
                instances = str(instance)
            print(instances)
            return

        try:
            cls = eval(arg)
        except NameError:
            print("** class doesn't exist **")
            return

        for key, instance in storage.all().items():
            if key.startswith(arg):
                instances = str(instance)
        print(instances)

    def do_update(self, line):
        """"Updates an instance based on the class name and id
        by adding or updating attribute(save the change into the JSON file)"""
        args = line.split(maxsplit=3)

        if len(args) < 4:
            if len(args) < 1:
                print("** class name missing **")
                return
            elif len(args) < 2:
                print("** instance id missing **")
                return
            elif len(args) < 3:
                print("** attribute name missing **")
                return
            elif len(args) < 4:
                print("** value missing **")
                return

        class_name = args[0]
        instance_id = args[1]
        attribute_name = args[2]
        attribute_value = args[3]

        try:
            cls = eval(class_name)
        except NameError:
            print("** class doesn't exist **")
            return

        key = f"{class_name}.{instance_id}"
        instance = storage.all().get(key)

        if instance is None:
            print("** no instance found **")
            return

        try:
            attr_type = type(getattr(instance, attribute_name))
            if attr_type == int:
                attribute_value = int(attribute_value)
            elif attr_type == float:
                attribute_value = float(attribute_value)
            else:
                attribute_value = str(attribute_value)
        except AttributeError:
            print('** Invalid attribute value **')
            return

        setattr(instance, attribute_name, attribute_value)
        instance.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
