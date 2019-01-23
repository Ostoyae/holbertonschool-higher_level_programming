#!/usr/bin/python3
import unittest
import os
import tempfile
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.rec = Rectangle(5, 5, 10, 10, 1337)

    def test_rec1(self):
        self.rec1 = Rectangle(4, 4, 5, 5)
        self.assertEqual(self.rec1.width, 4)
        self.assertEqual(self.rec1.height, 4)
        self.assertEqual(self.rec1.x, 5)
        self.assertEqual(self.rec1.y, 5)
        self.assertEqual(self.rec1.id, 1)

    def test_rec538(self):
        self.rec538 = Rectangle(5 , 5, 0, 0, 538)
        self.assertEqual(self.rec538.width, 5)
        self.assertEqual(self.rec538.height, 5)
        self.assertEqual(self.rec538.x, 0)
        self.assertEqual(self.rec538.y, 0)
        self.assertEqual(self.rec538.id, 538)

    def test_rec_validation(self):
        """ test Raises work"""
        with self.assertRaises(TypeError):
            Rectangle("woof","meow")

        with self.assertRaises(TypeError):
            Rectangle(False , False, False, False)

        with self.assertRaises(ValueError):
            Rectangle(-1,-1)

        with self.assertRaises(ValueError):
            Rectangle(5, 5, -1, -1)

    def test_recValueSet_Sucess(self):
        self.rec.width = 4
        self.rec.height = 20
        self.rec.x = 100
        self.rec.y = 2
    
    def test_recValueSet_Fail(self):
        with self.assertRaises(TypeError):
            self.rec.width = "bad type"

    def test_recArea(self):
        self.assertEqual(self.rec.area(), 25)

    def test_rec_str(self):
        self.assertEqual("[Rectangle] (1337) 10/10 - 5/5", str(self.rec))

    def test_rec_update_args(self):
        """requires __str__ to work"""
        self.rec = Rectangle(5, 5, 10, 10, 1337)
        self.rec.update(1001, 2, 2, 1, 1)
        self.assertEqual(str(self.rec), "[Rectangle] (1001) 1/1 - 2/2")


    def test_rec_update_keyArgs(self):
        """requires __str__ to work"""
        self.rec = Rectangle(5, 5, 10, 10, 1337)
        self.rec.update(x=100, y=1, width=50, height=25, id=42)
        self.assertEqual(str(self.rec), "[Rectangle] (42) 100/1 - 50/25")


    def test_rec_update_keyArgs(self):
        """requires __str__ to work"""
        self.rec = Rectangle(5, 5, 10, 10, 1337)
        with self.assertRaises(TypeError):
            self.rec.update(id="cat")
    
    def test_recToDict(self):
        self.assertEqual(
                self.rec.to_dictionary(),
                {"id": 1337, "width": 5, "height" : 5, "x" : 10, "y" : 10 })

    def test_rec_saveFile(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        try:
            self.rec.save_to_file([r1,r2])
            f = open("Rectangle.json")
            f.close()
        finally:
            os.remove("Rectangle.json")
