#!/usr/bin/python3
""" This module defines a program that contains the entry point of the
command interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB project"""
    prompt = '(hbnb) '

    classes = {
        'BaseModel': BaseModel,
        'User': User,
        'Place': Place,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Review': Review
    }

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

        class_name = arg.split()[0]
        cls = self.classes.get(class_name)
        
        if cls is None:
            print("** class doesn't exist **")
            return

        new_instance = cls()
        new_instance.save()
        print(new_instance.id)

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
        cls = self.classes.get(class_name)

        if cls is None:
            print("** class doesn't exist **")
            return

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
        cls = self.classes.get(class_name)

        if cls is None:
            print("** class doesn't exist **")
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
        args = arg.split()


        if len(args) == 1 and args[0].endswith('.all()'):
            class_name = args[0].replace('.all()', '')
            cls = self.classes.get(class_name)
            
            if cls is None:
                print("** class doesn't exist **")
                return
            
            instances = [str(inst) for key, inst in storage.all().items() if key.startswith(f"{class_name}.")]
        
        elif not args:
            instances = [str(inst) for inst in storage.all().values()]
        
        else:
            print("** Unknown syntax: {} **".format(arg))
            return

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

        cls = self.classes.get(class_name)

        if cls is None:
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
            pass
        setattr(instance, attribute_name, attribute_value)
        instance.save()
    
    def do_class_all(self, class_name):
        """Prints all instances of a specific class"""
        cls = self.classes.get(class_name)
        
        if cls is None:
            print("** class doesn't exist **")
            return
        
        instances = [str(inst) for key, inst in storage.all().items() if key.startswith(f"{class_name}.")]
        print(instances)

    def default(self, line):
        """Handles unknown commands or class method calls"""
        if '.' in line:
            class_name, method_call = line.split('.', 1)
            if method_call == "all()":
                return self.do_class_all(class_name)
        print("** Unknown syntax: {} **".format(line))

if __name__ == "__main__":
    HBNBCommand().cmdloop()
