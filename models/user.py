#!/usr/bin/python3
from models.base_model import BaseModel
"""This module defines a class user that inherits from BaseModel"""


class User(BaseModel):
    """Represents a user for the AirBnB clone project"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    