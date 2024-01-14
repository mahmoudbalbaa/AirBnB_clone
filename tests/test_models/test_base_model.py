#!/usr/bin/python3
"""
Unit test for the base class base model
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """TestBaseClass Test the base class
    Args:
        unittest (): Propertys for unit testing
    """

    def test_init(self):
        """
        Test datetime type
        """
        my_model = BaseModel()

        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def test_save_method(self):
        """
        test save method of basemodel
        """
        my_model = BaseModel()

        initial_updated_at = my_model.updated_at
        current_updated_at = my_model.save()
        self.assertNotEqual(initial_updated_at, current_updated_at)

    def test_to_dict_method(self):
        """
        testing to dict function
        """
        my_model = BaseModel()
        my_mod_c_iso = my_model.created_at.isoformat()
        my_model_dict = my_model.to_dict()

        self.assertIsInstance(my_model_dict, dict)
        self.assertEqual(my_model_dict['__class__'], 'BaseModel')
        self.assertEqual(my_model_dict['id'], my_model.id)
        self.assertEqual(my_model_dict['created_at'], my_mod_c_iso)
        self.assertEqual(my_model_dict['updated_at'], my_mod_c_iso)

    def test_str_method(self):
        """
        Test str output
        """
        my_model = BaseModel()

        self.assertTrue(str(my_model).startswith('[BaseModel]'))
        self.assertIn(str(my_model.__dict__), str(my_model))
        self.assertIn(my_model.id, str(my_model))


if __name__ == '__main__':
    unittest.main()
