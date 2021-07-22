from django.test import TestCase
from .calc import add
from .calc import subtract


class CalcTest(TestCase):
    def test_add_numbers(self):
        """Test that two numbers are added togetger"""
        self.assertEqual(add(3, 8), 11)
        self.assertEqual(add(2, 4), 6)

    def test_subtract_numbes(self):
        """Test that two numbers are subtracterd and returned"""
        self.assertEqual(subtract(5, 11), -6)
        self.assertEqual(subtract(5, 4), 1)
