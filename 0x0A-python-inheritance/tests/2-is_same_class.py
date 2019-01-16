#!/usr/bin/python3
import unittest
is_same_class = __import__('2-is_same_class').is_same_class

class TestIsSameClass(unittest.TestCase):
    
    def test_usage(self):
        a = 1
        b = 1.0
        s = "meow"

        self.assertTrue(is_same_class(a, int), "value isn't a INT")
        self.assertTrue(is_same_class(b, float), "value isn't a FLOAT")
        self.assertTrue(is_same_class(s, str), "value isn't a STR")
    
    def test_fail(self):
        a = 'test'
        b = 1
        s = 1.0

        self.assertFalse(is_same_class(a, int), "value isn't a INT")
        self.assertFalse(is_same_class(b, float), "value isn't a FLOAT")
        self.assertFalse(is_same_class(s, str), "value isn't a STR")
