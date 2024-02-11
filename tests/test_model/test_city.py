#!/usr/bin/python3
"""Defines unittests for models/city.py"""
import os
import models
import unittest
from models.city import City

class TestCity(unittest.TestCase):
    cty = City()
    self.assertIn(state_id, cty)
    self.assertIn(name, cty)

if __name__ == "__main__":
    unittest.main()
