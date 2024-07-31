#!/usr/bin/python3

import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User

# Assuming `storage` is a global object in your implementation
storage = FileStorage()
storage.reload()

class TestHBNBCommand(unittest.TestCase):
    """Unit tests for the HBNBCommand class"""

    @patch('sys.stdout', new_callable=StringIO)
    def test_create(self, mock_stdout):
        """Test create method"""
        cmd = HBNBCommand()
        cmd.onecmd('create User')
        output = mock_stdout.getvalue().strip()
        self.assertTrue(output)  # Check that an ID is printed
        instance = storage.all().get(f"User.{output}")
        self.assertIsNotNone(instance)
        self.assertIsInstance(instance, User)

    @patch('sys.stdout', new_callable=StringIO)
    def test_show(self, mock_stdout):
        """Test show method"""
        instance = User()
        instance.save()
        cmd = HBNBCommand()
        cmd.onecmd(f'show User {instance.id}')
        output = mock_stdout.getvalue().strip()
        self.assertIn(instance.id, output)
        self.assertIn('User', output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy(self, mock_stdout):
        """Test destroy method"""
        instance = User()
        instance.save()
        cmd = HBNBCommand()
        cmd.onecmd(f'destroy User {instance.id}')
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "")
        self.assertIsNone(storage.all().get(f"User.{instance.id}"))

    @patch('sys.stdout', new_callable=StringIO)
    def test_all(self, mock_stdout):
        """Test all method"""
        User().save()
        cmd = HBNBCommand()
        cmd.onecmd('all User')
        output = mock_stdout.getvalue().strip()
        self.assertIn('User', output)
        self.assertIn('id', output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_count(self, mock_stdout):
        """Test count method"""
        User().save()
        cmd = HBNBCommand()
        cmd.onecmd('count User')
        output = mock_stdout.getvalue().strip()
        self.assertTrue(output.isdigit())
        count = int(output)
        self.assertGreater(count, 0)

    @patch('sys.stdout', new_callable=StringIO)
    def test_update(self, mock_stdout):
        """Test update method"""
        instance = User()
        instance.save()
        cmd = HBNBCommand()
        cmd.onecmd(f'update User {instance.id} first_name John')
        instance = storage.all().get(f"User.{instance.id}")
        self.assertEqual(instance.first_name, "John")

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_with_dict(self, mock_stdout):
        """Test update method with dictionary"""
        instance = User()
        instance.save()
        cmd = HBNBCommand()
        cmd.onecmd(f'update User {instance.id} {{"first_name": "John", "age": 30}}')
        instance = storage.all().get(f"User.{instance.id}")
        self.assertEqual(instance.first_name, "John")
        self.assertEqual(instance.age, 30)

if __name__ == '__main__':
    unittest.main()
