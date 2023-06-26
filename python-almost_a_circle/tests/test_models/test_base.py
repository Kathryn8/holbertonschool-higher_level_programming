#!/usr/bin/python3
"""Unittest for base class"""
import unittest
Base = __import__('models.base').Base


class TestBaseClass(unittest.TestCase):
    """Unit testing functions for testing base class"""

    def setUp(self):
        """Set up testing conditions"""
        self.b1 = Base()
        self.b2 = Base(42)
        self.b3 = Base()
        self.b4 = Base()
        self.b5 = Base()

    def test_base_class(self):
        """Test case functions"""
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 42)
        self.assertEqual(self.b3.id, 2)
        self.assertEqual(self.b4.id, 3)
        self.assertEqual(self.b5.id, 4)

    def test_base_dummy(self):
        """Test case functions"""
        return True
