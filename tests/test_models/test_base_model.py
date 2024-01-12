#!/usr/bin/python3
"""

"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.my_model = BaseModel()

    def test_attributes(self):
        self.assertTrue(hasattr(self.my_model, 'id'))
        self.assertTrue(hasattr(self.my_model, 'created_at'))
        self.assertTrue(hasattr(self.my_model, 'updated_at'))

    def test_save_method(self):
        initial_updated_at = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(initial_updated_at, self.my_model.updated_at)

    def test_to_dict_method(self):
        model_dict = self.my_model.to_dict()

        self.assertTrue(isinstance(model_dict, dict))
        self.assertIn('__class__', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)

    def test_str_method(self):
        str_representation = str(self.my_model)
        self.assertTrue(isinstance(str_representation, str))
        self.assertIn('BaseModel', str_representation)
        self.assertIn(self.my_model.id, str_representation)


if __name__ == '__main__':
    unittest.main()
