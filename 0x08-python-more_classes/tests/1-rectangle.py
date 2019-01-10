#!/usr/bin/python3
"""Unittest for Rectangle class
"""

import unittest
Rectangle = __import__('1-rectangle').Rectangle

class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rec = Rectangle(4,8)

    def test_class(self):
        self.assertEqual(
                self.rec.__dict__,
                {'_Rectangle__height': 8, '_Rectangle__width': 4}
                )

    def test_Rec_define(self):
        self.assertEqual(self.rec.width, 4)
        self.assertEqual(self.rec.height, 8)

        self.rec.width = 10
        self.rec.height = 3
        self.assertEqual(self.rec.width, 10)
        self.assertEqual(self.rec.height, 3)

    @unittest.expectedFailure
    def test_wrong_width(self):
        self.rec.width = "cat"

    @unittest.expectedFailure
    def test_wrong_height(self):
        self.rec.height = "dog"
