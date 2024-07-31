#!/usr/bin/python3
"""this module defines City class that inherits from BaseModel class"""

from models.base_model import BaseModel


class City(BaseModel):
    state_id = ""
    name = ""