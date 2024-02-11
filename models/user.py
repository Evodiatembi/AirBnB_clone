#!/usr/bin/python3
"""
defines a class user
"""
from models import storage
from models.base_model import BaseModel
class User(BaseModel):
    """represent a class called user

    Attributes:
        email(string): user email
        password(string): user password
        first_name(string): user first name
        last_name(string): user last name
    """
 def __init__(self, email, password, first_name, last_name):
     self.email = " "
     self.password = " "
     self.first_name = " "
     self.last_name = " "
