#!/usr/bin/python3

import unittest
lookup = __import__('0-lookup').lookup

class TestLookup(unittest.TestCase):

    def setUp(self):
        class MyClass1(object):
            pass

        class MyClass2(object):
            my_attr1 = 3

            def my_meth(self):
                pass

        self.a = MyClass1()
        self.b = MyClass2()

    def test_return_type(self):
        self.assertEqual(type(lookup(self.a)), list)
        self.assertEqual(type(lookup(self.b)), list)
