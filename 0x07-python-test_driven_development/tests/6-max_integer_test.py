#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        self.assertEqual(max_integer([1, 2, 3 , 4]), 4)
        self.assertEqual(max_integer([4, 2, 3 , 1]), 4)
        self.assertEqual(max_integer([1, 3, 2]), 3)
        self.assertEqual(max_integer([3, 1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([-1, -2, -3 , -4), -1)
        self.assertEqual(max_integer([4]), 4)

        self.assertEqual(max_integer(), None)

        with self.assertRaises(TypeError):
            max_integer(4)
            max_integer(["cat", "dog"])
            max_integer(["woof", 2 , 4])
            max_integer({1,2,3})
            max_integer((1,2,3))
