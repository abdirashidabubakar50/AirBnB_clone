import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        """Set up test case environment"""
        self.user = User()

    def test_email(self):
        """Test email attribute"""
        self.assertEqual(self.user.email, "")

    def test_password(self):
        """Test password attribute"""
        self.assertEqual(self.user.password, "")

    def test_first_name(self):
        """Test first name attribute"""
        self.assertEqual(self.user.first_name, "")

    def test_last_name(self):
        """Test last name attribute"""
        self.assertEqual(self.user.last_name, "")

if __name__ == '__main__':
    unittest.main()
