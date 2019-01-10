#!/usr/bin/python3
"""Unittest for Rectangle class
"""

import unittest
Rectangle = __import__('0-rectangle').Rectangle

class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rec = Rectangle()

    def test_class(self):
        self.assertEqual(self.rec.__dict__, {})

    def test_Rec_define(self):
        self.rec(4,8)
        assertEqual(self.rec.width, 4)
        assertEqual(self.rec.height, 8)

        self.rec.width = 10
        self.rec.height = 3
        assertEqual(self.rec.width, 10)
        assertEqual(self.rec.height, 3)
