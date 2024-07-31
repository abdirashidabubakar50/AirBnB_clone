import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    def setUp(self):
        """set up test case environment"""
        self.place = Place()
    
    def test_city_id(self):
        """test the city_id attribute"""
        self.assertEqual(self.place.user_id, "")
    
    def test_user_id(self):
        "test the user_id attribute"
        self.assertEqual(self.place.user_id, "")
    
    def test_name(self):
        """test the name attribute"""
        self.assertEqual(self.place.name, "")
    
    def test_description(self):
        """test the description attribute"""
        self.assertEqual(self.place.description, "")
    
    def test_number_rooms(self):
        """test teh number_rooms attribute"""
        self.assertEqual(self.place.number_rooms, 0)
    