import unittest
from models.amenity import Amenity


class TestState(unittest.TestCase):
    def setUp(self):
        """sets up the environments for the test cases"""
        self.amenity = Amenity()
    
    def test_name(self):
        """tests the name attribute"""
        self.assertEqual(self.amenity.name, "")