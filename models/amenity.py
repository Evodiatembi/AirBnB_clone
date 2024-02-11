#!/usr/bin/python3
"""Defines a class called Amenity."""
from models.base_model import BaseModel
class Amenity(BaseModel):
    """Represent a class Amenity.

    Attributes:
        name (string): name of Amenity
    """
 def __init__(self, name):
     self.name = ""
