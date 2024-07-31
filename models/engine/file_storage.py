#!/usr/bin/python3
# from models.base_model import BaseModel
from os.path import exists
import json
# from models.base_model import BaseModel
# from models.user import User
# from models.place import Place
# from models.state import State
# from models.city import City
# from models.amenity import Amenity
# from models.review import Review

""" This moduel defines FileStorage class that serializes instatances
to a JSON file and deserializes JSON file to instances
"""


class FileStorage:
    """class FileStorage; serializes instances to a JSON file and deserialize
    JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects

        Returns:
            dict: the dictionary object
        """
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key  <obj class name>.id.
        Args:
            obj(BaseModel): The object to be added to __objects
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        if exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                json_objects = json.load(file)
                for obj_dict in json_objects.values():
                    class_name = obj_dict["__class__"]
                    del obj_dict["__class__"]
                    try:
                        module = __import__('models.' + class_name.lower(),
                                            fromlist=[class_name])
                        cls = getattr(module, class_name)
                        self.new(cls(**obj_dict))
                    except ImportError:
                        print(f"** Error importing class {class_name} **")
                    except AttributeError:
                        print(f"** Error finding class {class_name} in module **")
