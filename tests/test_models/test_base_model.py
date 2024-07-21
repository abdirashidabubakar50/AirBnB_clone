#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """unittest class for testing teh BaseModel class"""
    def setUp(self):
        """set up a new instance of BaseModel before each test"""
        self.model = BaseModel()

    def test_initialization(self):
        """Test the initialization fo the BaseModel instance"""
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)
        self.assertEqual(self.model.created_at, self.model.updated_at)


if __name__ == "__main__":
    unittest.main()
