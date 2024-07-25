#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()
        self.file_path = self.storage._FileStorage__file_path
        # Ensure __objects is cleared before each test
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_file_path(self):
        self.assertTrue(hasattr(self.storage, '_FileStorage__file_path'))
        self.assertEqual(self.storage._FileStorage__file_path, 'file.json')

    def test_objects(self):
        self.assertTrue(hasattr(self.storage, '_FileStorage__objects'))
        self.assertIsInstance(self.storage._FileStorage__objects, dict)

    def test_all(self):
        self.assertEqual(self.storage.all(), {})

    def test_new(self):
        obj = BaseModel()
        self.storage.new(obj)
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, self.storage.all())

    def test_save(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))

    def test_reload(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, self.storage.all())


if __name__ == "__main__":
    unittest.main()
