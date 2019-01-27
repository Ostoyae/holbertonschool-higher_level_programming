#!/usr/bin/python3
from __future__ import print_function
from models.base import Base
import unittest
import tempfile


class TestBase(unittest.TestCase):

    def setUp(self):
        self.b538 = Base(538)

    def test_baseNoID(self):
        self.b2 = Base(2)
        self.b1 = Base()
        self.assertEqual(self.b1.id, 1)

    def test_baseSomeID(self):
        self.assertEqual(self.b538.id, 538)

    def test_arg_overflow(self):
        with self.assertRaises(TypeError):
            Base(1, 2)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBase)
    unittest.TextTestRunner(verbosity=2).run(suite)
