import unittest
from models.state import State


class TestState(unittest.TestCase):
    def setUp(self):
        """sets up the environments for the test cases"""
        self.state = State()
    
    def test_name(self):
        """tests the name attribute"""
        self.assertEqual(self.state.name, "")