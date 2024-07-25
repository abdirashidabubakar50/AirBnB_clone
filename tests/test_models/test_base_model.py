#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel
from time import sleep

class TestBaseModel(unittest.TestCase):
    """unittest class for testing the BaseModel class"""
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

    def test_save_method(self):
        """Test that the save method updates the updated_at attribute"""
        model = BaseModel()
        original_updated_at = model.updated_at
        sleep(1)  # Sleep for a second to ensure updated_at will be different
        model.save()
        self.assertNotEqual(model.updated_at, original_updated_at)
        self.assertTrue(isinstance(model.updated_at, datetime))

    def test_to_dict_method(self):
        """Test the to_dict method returns the correct dictionary representation"""
        model = BaseModel()
        model_dict = model.to_dict()

        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(model_dict['created_at'], model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], model.updated_at.isoformat())

        self.assertTrue(isinstance(model_dict['created_at'], str))
        self.assertTrue(isinstance(model_dict['updated_at'], str))

    def test_to_dict_contains_all_attributes(self):
        """Test the to_dict method contains all attributes of the instance"""
        model = BaseModel()
        model.name = "Test"
        model.number = 123
        model_dict = model.to_dict()

        self.assertIn('name', model_dict)
        self.assertIn('number', model_dict)
        self.assertEqual(model_dict['name'], "Test")
        self.assertEqual(model_dict['number'], 123)


if __name__ == "__main__":
    unittest.main()
