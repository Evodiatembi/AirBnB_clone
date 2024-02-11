#!/usr/bin/python3
"""Defines a class called State."""
from models.base_model import BaseModel
class State(BaseModel):
    """Represent a class state.

    Attributes:
        name (string): name of the state
    """
 def __init__(self, name):
     self.name = ""

