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
        args = line.split(maxsplit=2)

        if len(args) < 3:
            if len(args) < 1:
                print("** class name missing **")
                return
            elif len(args) < 2:
                print("** instance id missing **")
                return
            elif len(args) < 3:
                print("** dictionary representation missing **")
                return

        class_name = args[0]
        instance_id = args[1]
        attribute_dict = args[2]

        self.do_class_update(class_name, instance_id, attribute_dict)

    def do_class_all(self, class_name):
        """Prints all instances of a specific class"""
        cls = self.classes.get(class_name)
        
        if cls is None:
            print("** class doesn't exist **")
            return
        
        instances = [str(inst) for key, inst in storage.all().items() if key.startswith(f"{class_name}.")]
        print(instances)
    
    def do_class_count(self, class_name):
        """Prints the number of instances of a specific class"""
        cls = self.classes.get(class_name)
        
        if cls is None:
            print("** class doesn't exist **")
            return
        
        count = sum(1 for key in storage.all().keys() if key.startswith(f"{class_name}."))
        print(count)
    
    def do_class_show(self, class_name, instance_id):
        """Prints the string representation of an instance based on the class name and id"""
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
    
    def do_class_destroy(self, class_name, instance_id):
        """Deletes an instance based on the class name and id"""
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
    
    def do_class_update(self, class_name, instance_id, attribute_dict):
        """Updates an instance based on the class name and id by adding or updating attribute"""
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
            attributes = eval(attribute_dict)
            if not isinstance(attributes, dict):
                raise ValueError
        except (SyntaxError, ValueError):
            print("** invalid dictionary format **")
            return

        for attribute_name, attribute_value in attributes.items():
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

    def default(self, line):
        """Handles unknown commands or class method calls"""
        if '.' in line and '(' in line and ')' in line:
            class_name, method_call = line.split('.', 1)
            method_name, params = method_call.split('(', 1)
            params = params.rstrip(')')
            if method_name == "all":
                return self.do_class_all(class_name)
            elif method_name == "count":
                return self.do_class_count(class_name)
            elif method_name == "show":
                params = params.strip('"')
                return self.do_class_show(class_name, params)
            elif method_name == "destroy":
                params = params.strip('"')
                return self.do_class_destroy(class_name, params)
            elif method_name == "update":
                params = params.split(', ')
                if len(params) == 3:
                    instance_id = params[0].strip('"')
                    attribute_name = params[1].strip('"')
                    attribute_value = params[2].strip('"')
                    return self.do_class_update(class_name, instance_id, attribute_name, attribute_value)
        print("** Unknown syntax: {} **".format(line))

if __name__ == "__main__":
    HBNBCommand().cmdloop()
