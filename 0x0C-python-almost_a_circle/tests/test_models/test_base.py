#!/usr/bin/python3
"""Module for Base unit test"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from models.base import __doc__ as doc_check
import json
import os


class TestBaseMethods(unittest.TestCase):
    """Class to test the Base Class"""
    def setUp(self):
        """Initialize nb_objects before each test"""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Cleans up tasks"""
        pass

    def test_docstrings(self):
        self.assertIsNotNone(doc_check)
        self.assertIsNotNone(Base.__doc__)
        self.assertIs(hasattr(Base, "__init__"), True)
        self.assertIsNotNone(Base.__init__.__doc__)
        self.assertIs(hasattr(Base, "create"), True)
        self.assertIsNotNone(Base.create.__doc__)
        self.assertIs(hasattr(Base, "to_json_string"), True)
        self.assertIsNotNone(Base.to_json_string.__doc__)
        self.assertIs(hasattr(Base, "from_json_string"), True)
        self.assertIsNotNone(Base.from_json_string.__doc__)
        self.assertIs(hasattr(Base, "save_to_file"), True)
        self.assertIsNotNone(Base.save_to_file.__doc__)
        self.assertIs(hasattr(Base, "load_from_file"), True)
        self.assertIsNotNone(Base.load_from_file.__doc__)
        self.assertIs(hasattr(Base, "save_to_file_csv"), True)
        self.assertIsNotNone(Base.save_to_file.__doc__)
        self.assertIs(hasattr(Base, "load_from_file_csv"), True)
        self.assertIsNotNone(Base.load_from_file.__doc__)
        self.assertIs(hasattr(Base, "draw"), True)
        self.assertIsNotNone(Base.draw.__doc__)

# ----------Task_1 Tests-------------------
    def testNbPriv(self):
        """test if nb_objects is a private attribute"""
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_nb_initialisation(self):
        """tests the initialisation of nb_objects"""
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)

    def test_instanciation(self):
        """tests the regular instanciation of Base"""
        Base_t = Base()
        self.assertEqual(str(type(Base_t)), "<class 'models.base.Base'>")
        self.assertEqual(Base_t.__dict__, {"id": 1})
        self.assertEqual(Base_t.id, 1)

    def test_init_no_args(self):
        """test init with no args"""
        with self.assertRaises(TypeError) as excep:
            Base.__init__()
        message = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(excep.exception), message)

    def test_init_too_many_args(self):
        """test init with too many args"""
        with self.assertRaises(TypeError) as excep:
            Base.__init__(self, 13, 45)
        message = "__init__() takes from 1 to 2 positional \
arguments but 3 were given"
        self.assertEqual(str(excep.exception), message)

    def test_id_count(self):
        "tests if the id is following"
        op = Base()
        po = Base()
        lm = Base(4)
        lp = Base()
        self.assertEqual(op.id, 1)
        self.assertEqual(po.id, 2)
        self.assertEqual(lm.id, 4)
        self.assertEqual(lp.id, 3)

    def test_class_inst_id(self):
        """Test synchronous between instance and class id"""
        Base_t = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), Base_t.id)
        Base_t = Base()
        Base_t = Base("pok")
        Base_t = Base(54)
        Base_t = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), Base_t.id)

    def test_int_variable(self):
        """Tests id dependent on a variable"""
        num = 45
        Base_t = Base(num)
        self.assertEqual(Base_t.id, num)

    def test_int_variable(self):
        """Test id dependent on a variable"""
        string = "poxk"
        Base_t = Base(string)
        self.assertEqual(Base_t.id, string)

    def test_key_word(self):
        """Test id dependent on a variable (with tag)"""
        num = 6
        Base_t = Base(id=num)
        self.assertEqual(Base_t.id, num)

# --------------------------Task_15 Tests-----------------
    def test_to_json_string_isattr(self):
        """test the to_json_string method"""
        with self.assertRaises(TypeError) as excep:
            Base.to_json_string()
        message = "to_json_string() missing 1 required positional argument: \
'list_dictionaries'"
        self.assertEqual(str(excep.exception), message)

        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string(None), "[]")
        dic = [{}]
        self.assertEqual(Base.to_json_string(dic), '[{}]')
        dic = [{}, {}, {}]
        self.assertEqual(Base.to_json_string(dic), '[{}, {}, {}]')

        dic = [{'width': 65, 'height': 98, 'x': 54, 'y': 24, 'id': 98}]
        self.assertEqual(len(Base.to_json_string(dic)), len(str(dic)))

        dic = [{'width': 25, 'height': 3, 'x': 9, 'y': 14, 'id': 214},
               {'width': 51, 'height': 12, 'x': 14, 'y': 54, 'id': 45}]
        self.assertEqual(len(Base.to_json_string(dic)), len(str(dic)))

        dic = [{'di': 7}, {'alx': 75}]
        dic_json = '[{"di": 7}, {"alx": 75}]'
        self.assertEqual(Base.to_json_string(dic), dic_json)

        dic = [{'help': 7}]
        dic_json = '[{"help": 7}]'
        self.assertEqual(Base.to_json_string(dic), dic_json)

        Rect_t = Rectangle(12, 15, 32, 13)
        dic = Rect_t.to_dictionary()
        json_dic = Base.to_json_string([dic])
        dic = str([dic])
        dic = dic.replace("'", '"')
        self.assertEqual(dic, json_dic)

        Rect_t1 = Rectangle(51, 16, 3, 9)
        Rect_t2 = Rectangle(7, 16, 29, 1)
        dic = [Rect_t1.to_dictionary(), Rect_t2.to_dictionary()]
        json_dic = Base.to_json_string([dic])
        dic = str([dic])
        dic = dic.replace("'", '"')
        self.assertEqual(dic, json_dic)

        Square_t = Square(5, 2, 1)
        dic = Square_t.to_dictionary()
        json_dic = Base.to_json_string([dic])
        dic = str([dic])
        dic = dic.replace("'", '"')
        self.assertEqual(dic, json_dic)

        Square_t1 = Square(5, 3, 19)
        Square_t2 = Square(6, 7, 1)
        dic = [Square_t1.to_dictionary(), Square_t2.to_dictionary()]
        json_dic = Base.to_json_string([dic])
        dic = str([dic])
        dic = dic.replace("'", '"')
        self.assertEqual(dic, json_dic)


if __name__ == "__main__":
    unittest.main()
