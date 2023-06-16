#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Unit testing functions for max_integer
    """
    def test_max_int(self):
        # test if case normal
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        # test is list is empty
        self.assertRaises(TypeError, max_integer([]))
        # test is list is empty, return none
        self.assertEqual(max_integer([]), None)
        # test if only one element in list
        self.assertEqual(max_integer([10]), 10)
        # test if no parameter given
        self.assertRaises(TypeError, max_integer())
        # test if list contains float values
        self.assertRaises(TypeError, max_integer([1.333, 23.8907, 0.5]))
        # test if list contains all same values
        self.assertEqual(max_integer([5, 5, 5, 5, 5]), 5)
        # test if list contains all 0
        self.assertEqual(max_integer([0, 0, 0]), 0)
        # test if list contains all None value
        self.assertEqual(max_integer([None]), None)
        # test if list contains all NaN
        import math
        self.assertRaises(TypeError, max_integer([9, 8, 7, math.nan]))
        # self.assertRaisesRegex(TypeError, "'>' not supported between instanc\
        # es of 'NoneType' and 'NoneType'", max_integer([None, None, None]))
