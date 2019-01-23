#!/usr/bin/python3
import unittest
from models.square import Square

class TestSquare(unittest.TestCase):

    def setUp(self):
        self.sqr = Square(5, 10, 10, 1337)

    def test_sqr(self):
        self.sqr = Square(4, 5, 5)
        self.assertEqual(self.sqr.size, 4)
        self.assertEqual(self.sqr.x, 5)
        self.assertEqual(self.sqr.y, 5)
        self.assertEqual(self.sqr.id, 1)

    def test_sqr538(self):
        self.sqr538 = Square(5 , 0, 0, 538)
        self.assertEqual(self.sqr538.size, 5)
        self.assertEqual(self.sqr538.x, 0)
        self.assertEqual(self.sqr538.y, 0)
        self.assertEqual(self.sqr538.id, 538)

    def test_sqr_validation(self):
        """ test Raises work"""
        with self.assertRaises(TypeError):
            Square("woof","meow")

        with self.assertRaises(TypeError):
            Square(False , False, False, False)

        with self.assertRaises(ValueError):
            Square(-1,-1)

        with self.assertRaises(ValueError):
            Square(5, 5, -1, -1)

    def test_sqrValueSet_Sucess(self):
        self.sqr.size = 20
        self.sqr.x = 100
        self.sqr.y = 2
    
    def test_sqrValueSet_Fail(self):
        with self.assertRaises(TypeError):
            self.sqr.size = "bad type"

    def test_sqrArea(self):
        self.assertEqual(self.sqr.area(), 25)

    def test_sqr_str(self):
        self.assertEqual("[Square] (1337) 10/10 - 5", str(self.sqr))

    def test_sqr_update_args(self):
        """requires __str__ to work"""
        self.sqr = Square(5, 10, 10, 1337)
        self.sqr.update(1001, 2, 1, 1)
        self.assertEqual(str(self.sqr), "[Square] (1001) 1/1 - 2")


    def test_sqr_update_keyArgs(self):
        """requires __str__ to work"""
        self.sqr = Square(5, 10, 10, 1337)
        self.sqr.update(x=100, y=1, size=50, id=42)
        self.assertEqual(str(self.sqr), "[Square] (42) 100/1 - 50")


    def test_sqr_update_keyArgs(self):
        """requires __str__ to work"""
        self.sqr = Square(5, 10, 10, 1337)
        with self.assertRaises(TypeError):
            self.sqr.update(id="cat")

    def test_sqrToDict(self):
        self.assertEqual(
                self.sqr.to_dictionary(),
                {"id": 1337, "size" : 5, "x" : 10, "y" : 10 })
