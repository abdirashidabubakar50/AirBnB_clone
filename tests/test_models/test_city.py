import unittest
from models.city import City


class TestCity(unittest.TestCase):
    def setUp(self):
        """set up test case environment"""
        self.city = City()
    
    def test_state_id(self):
        """Test state_id attribute"""
        self.assertEqual(self.city.state_id, "")
    
    def test_name(self):
        """test the self attribute"""
        self.assertEqual(self.city.name, "")