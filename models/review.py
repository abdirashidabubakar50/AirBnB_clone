#!/usr/bin/python3
"""this module defines review class that inherits from BaseModel class"""

from models.base_model import BaseModel


class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""