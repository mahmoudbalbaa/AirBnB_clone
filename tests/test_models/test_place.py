#!/usr/bin/python3
"""
Test model for Place class
"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Place model class test case
    """
    def setUp(self):
        """Setup the unittest"""

        self.place = Place()

    def test_attributes(self):
        """
        test place attributes
        """

        self.assertTrue(hasattr(self.place, 'id'))
        self.assertTrue(hasattr(self.place, 'created_at'))
        self.assertTrue(hasattr(self.place, 'updated_at'))
        self.assertTrue(hasattr(self.place, 'city_id'))
        self.assertTrue(hasattr(self.place, 'user_id'))
        self.assertTrue(hasattr(self.place, 'name'))
        self.assertTrue(hasattr(self.place, 'description'))
        self.assertTrue(hasattr(self.place, 'number_rooms'))
        self.assertTrue(hasattr(self.place, 'number_bathrooms'))
        self.assertTrue(hasattr(self.place, 'max_guest'))
        self.assertTrue(hasattr(self.place, 'price_by_night'))
        self.assertTrue(hasattr(self.place, 'latitude'))
        self.assertTrue(hasattr(self.place, 'longitude'))
        self.assertTrue(hasattr(self.place, 'amenity_ids'))

    def test_save_method(self):
        """test saving method"""

        before_save = self.place.updated_at
        self.place.save()
        after_save = self.place.updated_at
        self.assertNotEqual(before_save, after_save)

    def test_to_dict_method(self):
        """test dict methods"""

        place_dict = self.place.to_dict()
        self.assertTrue(isinstance(place_dict, dict))
        self.assertIn('__class__', place_dict)
        self.assertIn('id', place_dict)
        self.assertIn('created_at', place_dict)
        self.assertIn('updated_at', place_dict)
        self.assertIn('city_id', place_dict)
        self.assertIn('user_id', place_dict)
        self.assertIn('name', place_dict)
        self.assertIn('description', place_dict)
        self.assertIn('number_rooms', place_dict)
        self.assertIn('number_bathrooms', place_dict)
        self.assertIn('max_guest', place_dict)
        self.assertIn('price_by_night', place_dict)
        self.assertIn('latitude', place_dict)
        self.assertIn('longitude', place_dict)
        self.assertIn('amenity_ids', place_dict)

    def test_str_method(self):
        """test str representation"""

        str_representation = str(self.place)
        self.assertTrue(isinstance(str_representation, str))
        self.assertIn(self.place.__class__.__name__, str_representation)
        self.assertIn(self.place.id, str_representation)
        self.assertIn('id', str_representation)
        self.assertIn('created_at', str_representation)
        self.assertIn('updated_at', str_representation)


if __name__ == '__main__':
    unitt
