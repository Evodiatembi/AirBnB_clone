#!/usr/bin/python3
"""Defines the class Review."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a class called review.

    Attributes:
        place_id (string): The Place id.
        user_id (string): The User id.
        text (string): The text of the review.
    """
    def __init__(self, place_id, user_id, text):
        self.place_id = ""
        self.user_id = ""
         self.text = ""

