import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    def setUp(self):
        """sets up the environment for the  test cases"""
        self.review = Review()
    
    def test_place_id(self):
        """Tests the place_id attribute"""
        self.assertEqual(self.review.place_id, "")
    
    def test_user_id(self):
        """Tests the user_id attribute"""
        self.assertEqual(self.review.user_id, "")
    
    def test_text(self):
        """tests the text attribute"""
        self.assertEqual(self.review.text, "")
