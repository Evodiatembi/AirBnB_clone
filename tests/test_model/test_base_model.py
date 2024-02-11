#!/usr/bin/python3
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test__init__(self):
        my_class_model = BaseModel()
        self.assertIsNotNone(my_class_model.created_at)
        self.assertIsNotNone(my_class_model.updated_at)
        self.assertIsNotNone(my_class_model.id)

    def test_str(self):
        my_class_model = BaseModel()
        self.assertTrue(str(my_class_model).startswith('[BaseModel]'))
        self.assertIn(str(my_class_model.__dict__), str(my_class_model))
        self.assertIn(my_class_model.id, str(my_class_model))
    def test_save(self):
        my_class_model = BaseModel()
        at_updated_before = my_class_model.updated_at
        at_updated_now = my_class_model.save()
        self.assertNotEqual(at_updated_before, at_updated_now)

    def test_to_dict(self):
        my_class_model = BaseModel()
        my_class_model_to_dict = my_class_model.to_dict()
        self.assertIsInstance(my_class_model_to_dict, dict)
        self.assertEqual(my_class_model_to_dict['created_at'], my_class_model.created_at.isoformat())
        self.assertNotEqual(my_class_model_to_dict['updated_at'], my_class_model.created_at.isoformat())
        self.assertEqual(my_class_model_to_dict['id'], my_class_model.id)
        self.assertEqual(my_class_model_to_dict['__class__'], 'BaseModel')

if __name__ == "__main__":
    unittest.main
