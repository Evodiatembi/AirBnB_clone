#!/usr/bin/python3
"""Defines unittests for models/place.py"""
import os
import models
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    plc = place()
    self.assertEqual(str, city_id)
    self.assertIn(city_id, plc)
    self.assertEqual(str, user_id)
    self.assertIn(user_id, plc)
    self.assertEqual(str, name)
    self.assertIn(name, plc)
    self.assertEqual(str, description)
    self.assertIn(description, plc)
    self.assertEqual(int, number_rooms)
    self.assertIn(number_rooms, plc)
    self.assertEqual(int, number_bathrooms)
    self.assertIn(number_bathrooms, plc)
    self.assertEqual(int, max_guest)
    self.assertIn(max_guest, plc)
    self.assertEqual(int, price_by_night)
    self.assertIn(price_by_night, plc)
    self.assertEqual(float, latitude)
    self.assertIn(latitude, plc)
    self.assertEqual(float, longitude)
    self.assertIn(longitude, plc)
    self.assertEqual(list, amenity_id)
    self.assertIn(amenity_id, plc)

if __name__ == "__main__":
    unittest.main()


