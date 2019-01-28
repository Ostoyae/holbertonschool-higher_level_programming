#!/usr/bin/python3
import unittest
import os
import tempfile
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.rec = Rectangle(5, 5, 10, 10, 1337)

    def tearDown(self):
        Rectangle.reset()

    def test_subclass(self):
        from models.base import Base
        self.assertTrue(issubclass(Rectangle, Base))

    def test_withoutArgs(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_oneArgs(self):
        with self.assertRaises(TypeError):
            Rectangle(5)

    def test_args_overflow(self):
        with self.assertRaises(TypeError):
            Rectangle(4, 4, 4, 4, 4, 4)

    def test_rec1(self):
        self.rec1 = Rectangle(4, 4, 5, 5)
        self.assertEqual(self.rec1.width, 4)
        self.assertEqual(self.rec1.height, 4)
        self.assertEqual(self.rec1.x, 5)
        self.assertEqual(self.rec1.y, 5)
        self.assertEqual(self.rec1.id, 1)

    def test_rec538(self):
        self.rec538 = Rectangle(5, 5, 0, 0, 538)
        self.assertEqual(self.rec538.width, 5)
        self.assertEqual(self.rec538.height, 5)
        self.assertEqual(self.rec538.x, 0)
        self.assertEqual(self.rec538.y, 0)
        self.assertEqual(self.rec538.id, 538)

    def test_rec_id(self):
        r1 = Rectangle(5, 5)
        r2 = Rectangle(5, 5)
        r3 = Rectangle(5, 5)
        r4 = Rectangle(5, 5)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 3)
        self.assertEqual(r4.id, 4)

    def test_rec_validation(self):
        """ test Raises work"""
        with self.assertRaises(TypeError):
            Rectangle("woof", "meow")

        with self.assertRaises(TypeError):
            Rectangle(False, False, False, False)

        with self.assertRaises(ValueError):
            Rectangle(-1, -1)

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

    def test_recArea_Raise(self):
        with self.assertRaises(TypeError):
            self.rec.area(5)

    def test_rec_str(self):
        self.assertEqual("[Rectangle] (1337) 10/10 - 5/5", str(self.rec))

    def test_rec_str_error(self):
        with self.assertRaises(TypeError):
            self.rec.__str__(3)

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
            {"id": 1337, "width": 5, "height": 5, "x": 10, "y": 10})

    def test_rec_saveFile(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        try:
            self.rec.save_to_file([r1, r2])
            f = open("Rectangle.json")
            f.close()
        finally:
            os.remove("Rectangle.json")

    def test_rec_FromJsonString(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_ls_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_ls_input)
        self.assertEqual(
            list_output,
            [
                {'height': 4, 'width': 10, 'id': 89},
                {'height': 7, 'width': 1, 'id': 7}
            ])

    def test_rec_CreateInstance(self):
        r1 = self.rec.to_dictionary()
        r2 = Rectangle.create(**r1)
        self.assertEqual(str(r2), '[Rectangle] (1337) 10/10 - 5/5')

    def test_sqr_CreateInstance_02(self):
        r1 = {"width" : 4}
        r2 = Rectangle.create(**r1)
        self.assertEqual(str(r2), '[Rectangle] (1) 0/0 - 4/1')

    def test_rec_CreateFromFile(self):
        r1 = Rectangle(7, 7, 2, 8, 100)
        r2 = Rectangle(2, 4)
        objs = []
        try:
            Rectangle.save_to_file([r1, r2])
            objs = Rectangle.load_from_file()
        finally:
            os.remove("Rectangle.json")
        self.assertEqual(str(objs[0]), '[Rectangle] (100) 2/8 - 7/7')
        self.assertEqual(
            str(objs[1]), '[Rectangle] ({}) 0/0 - 2/4'.format(r2.id))

    def test_rec_MissingFile(self):
        objs = list()
        try:
            objs = Rectangle.load_from_file()
        finally:
            pass
        self.assertEqual(objs, [])

    def test_rec_SaveCSV(self):
        r1 = Rectangle(7, 7, 2, 8, 100)
        r2 = Rectangle(2, 4)
        try:
            Rectangle.save_to_file_csv([r1, r2])
            with open("Rectangle.csv") as f:
                f.close()
        finally:
            os.remove("Rectangle.csv")

    def test_rec_CreateFromFile_CSV(self):
        r1 = Rectangle(7, 7, 2, 8, 100)
        r2 = Rectangle(2, 4)
        objs = []
        try:
            Rectangle.save_to_file_csv([r1, r2])
            objs = Rectangle.load_from_file_csv()
        finally:
            os.remove("Rectangle.csv")
        self.assertEqual(str(objs[0]), '[Rectangle] (100) 2/8 - 7/7')
        self.assertEqual(
            str(objs[1]), '[Rectangle] ({}) 0/0 - 2/4'.format(r2.id))
