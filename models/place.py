#!/usr/bin/python3
"""Defines the Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represent the class place.

    Attributes:
        city_id(string): The City id
        user_id(string): The User id
        name(string): The name of the place 
        description(string): The description of the place
        number_rooms(integer): The number of rooms of the place
        number_bathrooms(integer): The number of bathrooms of the place
        max_guest(integer): The maximum number of guests of the place
        price_by_night(integer): The price by night of the place
        latitude(float): The latitude of the place
        longitude(float): The longitude of the place
        amenity_ids(list): A list of Amenity ids
    """
    def __init__(self):
       self.city_id = ""
       self.user_id = ""
       self.name = ""
       self.description = ""
       self.number_rooms = 0
       self.number_bathrooms = 0
       self.max_guest = 0
       self.price_by_night = 0
       self.latitude = 0.0
       self.longitude = 0.0
       self.amenity_ids = []
