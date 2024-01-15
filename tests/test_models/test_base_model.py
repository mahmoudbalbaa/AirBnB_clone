#!/usr/bin/python3
"""
Unit test for the base class base model
"""
import unittest
from datetime import datetime
from unittest.mock import patch
from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):
    """TestBaseClass Test the base class
    Args:
        unittest (): Propertys for unit testing
    """

    def test_init(self):
        """
        Test datetime type
        """
        with patch('models.storage.new') as mock_new:
            instance = BaseModel()
            self.assertIsInstance(instance, BaseModel)
            self.assertIsNotNone(instance.id)
            self.assertIsInstance(instance.created_at, datetime)
            self.assertIsInstance(instance.updated_at, datetime)
            mock_new.assert_called_once_with(instance)

    def test_save(self):
        """
        test save method of basemodel
        """
        with patch('models.storage.save') as mock_save:
            instance = BaseModel()
            instance.save()
            mock_save.assert_called_once()

    def test_to_dict(self):
        """
        testing to dict function
        """
        instance = BaseModel()
        result = instance.to_dict()
        self.assertIsInstance(result, dict)
        self.assertEqual(result['__class__'], 'BaseModel')
        self.assertEqual(result['created_at'], instance.created_at.isoformat())
        self.assertEqual(result['updated_at'], instance.updated_at.isoformat())

    def test_str(self):
        """
        Test str output
        """
        instance = BaseModel()
        result = str(instance)
        self.assertIsInstance(result, str)
        self.assertIn('BaseModel', result)
        self.assertIn(instance.id, result)


if __name__ == '__main__':
    unittest.main()
