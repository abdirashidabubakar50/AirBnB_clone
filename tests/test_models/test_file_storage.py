#!/usr/bin/python3
import unittest
import os
import json
# from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Setup for each test"""
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = "test_file.json"
        self.base_model = BaseModel()
        self.base_model.name = "Test Model"
        self.base_model.my_number = 42
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """clean up after each test"""
        try:
            os.remove("test_file.json")
        except FileNotFoundError:
            pass

    def test_all_method(self):
        """test all() method"""
        self.assertEqual(self.storage.all(), {})
        self.storage.new(self.base_model)
        self.assertEqual(len(self.storage.all()), 1)
        key = f"{self.base_model.__class__.__name__}.{self.base_model.id}"
        self.assertIn(key, self.storage.all())

    def test_new_method(self):
        """Test the new() method."""
        self.storage.new(self.base_model)
        key = f"{self.base_model.__class__.__name__}.{self.base_model.id}"
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key], self.base_model)

    def test_save_method(self):
        """Test the save() method."""
        self.storage.new(self.base_model)
        self.storage.save()
        with open("test_file.json", "r") as file:
            content = json.load(file)
        key = f"{self.base_model.__class__.__name__}.{self.base_model.id}"
        self.assertIn(key, content)
        self.assertEqual(content[key]["name"], "Test Model")
        self.assertEqual(content[key]["my_number"], 42)

    def test_reload_method(self):
        """Test the reload() method."""
        self.storage.new(self.base_model)
        self.storage.save()
        new_storage = FileStorage()
        new_storage._FileStorage__file_path = "test_file.json"
        new_storage.reload()
        key = f"{self.base_model.__class__.__name__}.{self.base_model.id}"
        self.assertIn(key, new_storage.all())
        self.assertEqual(new_storage.all()[key].name, "Test Model")
        self.assertEqual(new_storage.all()[key].my_number, 42)


if __name__ == "__main__":
    unittest.main()
