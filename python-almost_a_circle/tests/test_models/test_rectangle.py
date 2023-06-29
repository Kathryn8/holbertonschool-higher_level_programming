#!/usr/bin/python3
"""Unittest for rectangle class"""
import unittest
Rectangle = __import__('models.rectangle').Rectangle


class TestBaseClass(unittest.TestCase):
    """Unit testing functions for testing rectangle class"""

    def test_1(self):
        """Two arguments"""
        self.r1 = Rectangle(1, 2)
        self.assertEqual(self.r1.width, 1)
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r1.y, 0)

    def test_2(self):
        """Three arguments"""
        self.r2 = Rectangle(1, 2, 3)
        self.assertEqual(self.r2.width, 1)
        self.assertEqual(self.r2.height, 2)
        self.assertEqual(self.r2.x, 3)
        self.assertEqual(self.r2.y, 0)

    def test_3(self):
        """Four arguments"""
        self.r3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(self.r3.width, 1)
        self.assertEqual(self.r3.height, 2)
        self.assertEqual(self.r3.x, 3)
        self.assertEqual(self.r3.y, 4)

    def test_4(self):
        """Width not integer"""
        with self.assertRaises(TypeError):
            self.r4 = Rectangle("1", 2)

    def test_5(self):
        """Height not integer"""
        with self.assertRaises(TypeError):
            self.r5 = Rectangle(1, "2")

    def test_6(self):
        """x not integer"""
        with self.assertRaises(TypeError):
            self.r6 = Rectangle(1, 2, "3")

    def test_7(self):
        """y not integer"""
        with self.assertRaises(TypeError):
            self.r7 = Rectangle(1, 2, 3, "4")

    def test_8(self):
        """Five arguments"""
        self.r8 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(self.r8.width, 1)
        self.assertEqual(self.r8.height, 2)
        self.assertEqual(self.r8.x, 3)
        self.assertEqual(self.r8.y, 4)
        self.assertEqual(self.r8.id, 5)

    def test_9(self):
        """negative width"""
        with self.assertRaises(ValueError):
            self.r9 = Rectangle(-1, 2)

    def test_10(self):
        """negative height"""
        with self.assertRaises(ValueError):
            self.r10 = Rectangle(1, -2)

    def test_11(self):
        """zero width"""
        with self.assertRaises(ValueError):
            self.r11 = Rectangle(0, 2)

    def test_12(self):
        """zero height"""
        with self.assertRaises(ValueError):
            self.r12 = Rectangle(1, 0)

    def test_13(self):
        """Negative x"""
        with self.assertRaises(ValueError):
            self.r13 = Rectangle(1, 2, -3)

    def test_14(self):
        """Negative y"""
        with self.assertRaises(ValueError):
            self.r14 = Rectangle(1, 2, 3, -4)

    def test_15(self):
        """Test the area method"""
        self.r15 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(self.r15.area(), 2)
