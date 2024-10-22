#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    BaseModel class that defines all common attributes/methods for other
    classes.

    Attributes:
        id(str): Unique identifier for each instance
        created_at: (datetime) The datetime when an instance is created
        updated_at: (datetime) The date time when an instance is created
                    and updated whenever the object changes
    """

    def __init__(self, *args, **kwargs):
        """

        Initializes a new instance of BaseModel

        The id is assigned a unique UUID
        The created_at and updated_at are assigned the current datetieme
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.now
            if 'updated_at' not in kwargs:
                self.updated_at = self.created_at
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """
        Return the string representation of the BaseModel instance.
        The string is formatted as:
        [<class name>] (<self.id>) <self.__dict__>

        Returns:
            str: The string representation of the instance
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the updated_at attribute with the current datetime.

        This method should be called whenever the instance is modified
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the instance.
        The dictionary includes all instance attributes, as ass __class__
        key with the class name of the object
        The updated_at and created_at attributes are converted
        to ISO format strings
        """
        dict_rep = self.__dict__.copy()
        dict_rep['__class__'] = self.__class__.__name__
        dict_rep['created_at'] = self.created_at.isoformat()
        dict_rep['updated_at'] = self.updated_at.isoformat()
        return dict_rep
