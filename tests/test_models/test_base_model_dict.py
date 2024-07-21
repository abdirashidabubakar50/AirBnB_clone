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

    def test_initialization_with_kwargs(self):

        """Test the initialization of the BaseModel instance with kwargs."""
        data = {
            'id': '1234',
            'created_at': '2023-07-20T14:28:23.382748',
            'updated_at': '2023-07-20T14:28:23.382748',
            'name': 'My Model'
        }
        model = BaseModel(**data)
        self.assertEqual(model.id, '1234')
        self.assertEqual(model.created_at, datetime.fromisoformat
                         ('2023-07-20T14:28:23.382748'))
        self.assertEqual(model.updated_at, datetime.fromisoformat
                         ('2023-07-20T14:28:23.382748'))
        self.assertEqual(model.name, 'My Model')

    def test_str(self):
        """Test the string representation of the BaseModel instance."""
        expected_str = f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        actual_str = str(self.model)
        self.assertEqual(actual_str, expected_str)


if __name__ == "__main__":
    unittest.main()
