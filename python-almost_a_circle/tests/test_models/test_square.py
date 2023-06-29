#!/usr/bin/python3
"""Unittest for square class"""
import unittest
Square = __import__('models.square').Square


class TestBaseClass(unittest.TestCase):
    """Unit testing functions for testing square class"""

    def test_1(self):
        """Two arguments"""
        self.s1 = Square(1, 2)
        self.assertEqual(self.s1.size, 1)
        self.assertEqual(self.s1.x, 2)

    def test_2(self):
        """Three arguments"""
        self.s2 = Square(1, 2, 3)
        self.assertEqual(self.s2.size, 1)
        self.assertEqual(self.s2.x, 2)
        self.assertEqual(self.s2.y, 3)

    def test_3(self):
        """Four arguments"""
        self.s3 = Square(1, 2, 3, 4)
        self.assertEqual(self.s3.size, 1)
        self.assertEqual(self.s3.x, 2)
        self.assertEqual(self.s3.y, 3)
        self.assertEqual(self.s3.id, 4)

    def test_4(self):
        """Size not integer"""
        with self.assertRaises(TypeError):
            self.s4 = Square("1")

    def test_5(self):
        """x not integer"""
        with self.assertRaises(TypeError):
            self.s5 = Square(1, "2")

    def test_6(self):
        """y not integer"""
        with self.assertRaises(TypeError):
            self.s6 = Square(1, 2, "3")

    def test_7(self):
        """size zero"""
        with self.assertRaises(ValueError):
            self.s7 = Square(0)

    def test_8(self):
        """negative size"""
        with self.assertRaises(ValueError):
            self.s8 = Square(-1)

    def test_9(self):
        """negative x"""
        with self.assertRaises(ValueError):
            self.s9 = Square(1, -2)

    def test_10(self):
        """negative y"""
        with self.assertRaises(ValueError):
            self.s10 = Square(2, 2, -3)
