"""
Sample tests
"""
from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        """Test adding numbers together"""
        res = calc.add(2, 3)
        self.assertEqual(res, 5)

    def test_subtract_numbers(self):
        """Test subtracting numbers"""
        res = calc.subtract(3, 5)
        self.assertEqual(res, 2)
    