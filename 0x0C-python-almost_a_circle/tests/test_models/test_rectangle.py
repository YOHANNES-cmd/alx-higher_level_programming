#!/usr/bin/python3
"""Module for Rectangle unit test"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.rectangle import __doc__ as doc_check
from models.square import Square
import json
import io
from contextlib import redirect_stdout


class TestRectangleMethods(unittest.TestCase):
    """Class to test the Rectangle Class"""

    def setUp(self):
        """Initialize nb_objects before each test"""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Cleans up tasks"""
        pass

    def test_docstrings(self):
        self.assertIsNotNone(doc_check)
        self.assertIsNotNone(Rectangle.__doc__)
        self.assertIs(hasattr(Rectangle, "__init__"), True)
        self.assertIsNotNone(Rectangle.__init__.__doc__)
        self.assertIs(hasattr(Rectangle, "width"), True)
        self.assertIsNotNone(Rectangle.width.__doc__)
        self.assertIs(hasattr(Rectangle, "height"), True)
        self.assertIsNotNone(Rectangle.height.__doc__)
        self.assertIs(hasattr(Rectangle, "x"), True)
        self.assertIsNotNone(Rectangle.x.__doc__)
        self.assertIs(hasattr(Rectangle, "y"), True)
        self.assertIsNotNone(Rectangle.y.__doc__)
        self.assertIs(hasattr(Rectangle, "area"), True)
        self.assertIsNotNone(Rectangle.area.__doc__)
        self.assertIs(hasattr(Rectangle, "display"), True)
        self.assertIsNotNone(Rectangle.display.__doc__)
        self.assertIs(hasattr(Rectangle, "__str__"), True)
        self.assertIsNotNone(Rectangle.__str__.__doc__)
        self.assertIs(hasattr(Rectangle, "update"), True)
        self.assertIsNotNone(Rectangle.update.__doc__)
        self.assertIs(hasattr(Rectangle, "to_dictionary"), True)
        self.assertIsNotNone(Rectangle.to_dictionary.__doc__)

# ---------------Tasks_2_&_3 Tests--------------------------------
    def test_class(self):
        """Test Rectangle class"""
        self.assertEqual(str(Rectangle), "<class 'models.rectangle.\
Rectangle'>")

    def test_inheritance(self):
        """Test if Rectangle inherits from Base"""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_init_no_args(self):
        """Test Rectangle() instantiation without self"""
        with self.assertRaises(TypeError) as excep:
            Rect_test = Rectangle()
        message = "__init__() missing 2 required positional \
arguments: 'width' and 'height'"
        self.assertEqual(str(excep.exception), message)

    def test_init_one_arg(self):
        """Test Rectangle() instantiation with a missing argument"""
        with self.assertRaises(TypeError) as excep:
            Rect_test = Rectangle(7)
        message = "__init__() missing 1 required positional argument: 'height'"
        self.assertEqual(str(excep.exception), message)

    def test_init_excedent_args(self):
        """Test Rectangle() instantiation with leftover arguments"""
        with self.assertRaises(TypeError) as excep:
            Rect_test = Rectangle(5, 6, 9, 1, 6, 3)
        message = "__init__() takes from 3 to 6 positional \
arguments but 7 were given"
        self.assertEqual(str(excep.exception), message)

    def test_instantiation(self):
        """Test Rectangle() instantiation with 2 arguments"""
        Rect_test = Rectangle(6, 8)
        self.assertEqual(str(type(Rect_test)), "<class 'models.\
rectangle.Rectangle'>")
        self.assertTrue(isinstance(Rect_test, Base))
        dic = {'_Rectangle__height': 8,
               '_Rectangle__width': 6,
               '_Rectangle__x': 0,
               '_Rectangle__y': 0,
               'id': 1}
        self.assertEqual(Rect_test.__dict__, dic)

    def test_instantiation_positional(self):
        """Test Rectangle() positional instantiation"""
        Rect_test = Rectangle(9, 4, 12, 7, 8)
        self.assertEqual(str(type(Rect_test)), "<class 'models.\
rectangle.Rectangle'>")
        self.assertTrue(isinstance(Rect_test, Base))
        dic = {'_Rectangle__height': 4,
               '_Rectangle__width': 9,
               '_Rectangle__x': 12,
               '_Rectangle__y': 7,
               'id': 8}
        self.assertEqual(Rect_test.__dict__, dic)

        Rect_test = Rectangle(5, 7, 19, 2)
        self.assertEqual(str(type(Rect_test)), "<class 'models.\
rectangle.Rectangle'>")
        self.assertTrue(isinstance(Rect_test, Base))
        dic = {'_Rectangle__height': 7,
               '_Rectangle__width': 5,
               '_Rectangle__x': 19,
               '_Rectangle__y': 2,
               'id': 1}
        self.assertEqual(Rect_test.__dict__, dic)

    def test_instantiation_no_positional(self):
        """Test Rectangle() no positional instantiation"""
        Rect_tst = Rectangle(id=9, x=4, width=12, y=7, height=8)
        self.assertEqual(str(type(Rect_tst)), "<class 'models.\
rectangle.Rectangle'>")
        self.assertTrue(isinstance(Rect_tst, Base))
        dic = {'_Rectangle__height': 8,
               '_Rectangle__width': 12,
               '_Rectangle__x': 4,
               '_Rectangle__y': 7,
               'id': 9}
        self.assertEqual(Rect_tst.__dict__, dic)

    def test_mix_positional(self):
        """Test Rectangle() positional/ no positional instantiation"""
        Rect_test = Rectangle(9, 100, 3, id=12, y=7)
        self.assertEqual(str(type(Rect_test)), "<class 'models.\
rectangle.Rectangle'>")
        self.assertTrue(isinstance(Rect_test, Base))
        dic = {'_Rectangle__height': 100,
               '_Rectangle__width': 9,
               '_Rectangle__x': 3,
               '_Rectangle__y': 7,
               'id': 12}
        self.assertEqual(Rect_test.__dict__, dic)

    def test_inheritance_id(self):
        """Test if id is inherits from base"""
        Base._Base__nb_objects = 78
        Rect_test = Rectangle(2, 4)
        self.assertEqual(Rect_test.id, 79)

    def test_getter_setter(self):
        """Test getters and setters"""
        Rect_test = Rectangle(5, 8)
        Rect_test.width = 54
        Rect_test.height = 43
        Rect_test.x = 3
        Rect_test.y = 2
        d = {'_Rectangle__height': 43,
             '_Rectangle__width': 54,
             '_Rectangle__x': 3,
             '_Rectangle__y': 2,
             'id': 1}
        self.assertEqual(Rect_test.__dict__, d)
        self.assertEqual(Rect_test.width, 54)
        self.assertEqual(Rect_test.height, 43)
        self.assertEqual(Rect_test.x, 3)
        self.assertEqual(Rect_test.y, 2)

    def test_arguments_invalid_type(self):
        """Test invalid arguments types"""
        with self.assertRaises(TypeError) as excep:
            Rect_test = Rectangle("34", 2)
        message = "width must be an integer"
        self.assertEqual(str(excep.exception), message)

        with self.assertRaises(TypeError) as excep:
            Rect_test = Rectangle(89, "w")
        message = "height must be an integer"
        self.assertEqual(str(excep.exception), message)

        with self.assertRaises(TypeError) as excep:
            Rect_test = Rectangle(89, 6, "holby")
        message = "x must be an integer"
        self.assertEqual(str(excep.exception), message)

        with self.assertRaises(TypeError) as excep:
            Rect_test = Rectangle(89, 6, 7, "betty")
        message = "y must be an integer"
        self.assertEqual(str(excep.exception), message)

        with self.assertRaises(ValueError) as excep:
            Rect_test = Rectangle(0, 6)
        message = "width must be > 0"
        self.assertEqual(str(excep.exception), message)

        with self.assertRaises(ValueError) as excep:
            Rect_test = Rectangle(-7, 6)
        message = "width must be > 0"
        self.assertEqual(str(excep.exception), message)

        with self.assertRaises(ValueError) as excep:
            Rect_test = Rectangle(9, 0)
        message = "height must be > 0"
        self.assertEqual(str(excep.exception), message)

        with self.assertRaises(ValueError) as excep:
            Rect_test = Rectangle(9, -12)
        message = "height must be > 0"
        self.assertEqual(str(excep.exception), message)

        with self.assertRaises(ValueError) as excep:
            Rect_test = Rectangle(89, 6, -5)
        message = "x must be >= 0"
        self.assertEqual(str(excep.exception), message)

        with self.assertRaises(ValueError) as excep:
            Rect_test = Rectangle(89, 6, 6, -8)
        message = "y must be >= 0"
        self.assertEqual(str(excep.exception), message)

        def invalid_types(self):
            """Returns lists with different invalid cases"""
            types = (3.56, float('inf'), float('Nan'), True,
                     (5, ), -6.792, [8], None, {8, 7})
            return types

        def validate_types(self):
            """Test invalid arguments types with different cases"""
            Rect_test = Rectangle(8, 5)
            attributes = ["x", "y", "width", "height"]
            for attr in attributes:
                message = "{} must be an integer".format(attr)
                for invalid in self.invalid_types():
                    with self.assertRaises(TypeError) as excep:
                        setattr(Rect_test, attr, invalid_types)
                    self.assertEqual(str(excep.exception), message)

# ---------------Tests: task 4--------------------------------

    def test_area_only_dimensions(self):
        """Test area() with height and witdth only"""
        Rect_test = Rectangle(3, 8)
        Rect_test.area()
        self.assertEqual(Rect_test.area(), 24)

    def test_area_no_self(self):
        """Test area() without self"""
        Rect_test = Rectangle(3, 8)
        with self.assertRaises(TypeError) as excep:
            Rectangle.area()
        message = "area() missing 1 required positional argument: 'self'"
        self.assertEqual(str(excep.exception), message)

    def test_area_positional(self):
        """Test area() with positional arguments"""
        Rect_test = Rectangle(5, 9, 6, 11, 12)
        Rect_test.area()
        self.assertEqual(Rect_test.area(), 45)

    def test_area_no_positional(self):
        """Test area() with no positional arguments"""
        Rect_test = Rectangle(id=5, height=9, y=6, x=11, width=2)
        Rect_test.area()
        self.assertEqual(Rect_test.area(), 18)

# ---------------Tasks_5_&_7 Tests--------------------------------

    def test_display_no_args(self):
        """Test display() without self"""
        Rect_test = Rectangle(5, 9)
        with self.assertRaises(TypeError) as excep:
            Rectangle.display()
        message = "display() missing 1 required positional argument: 'self'"
        self.assertEqual(str(excep.exception), message)

    def test_display_no_x_y(self):
        """Test display() without x and y"""
        Rect_test = Rectangle(1, 1)
        out_put = io.StringIO()
        with redirect_stdout(out_put):
            Rect_test.display()
        out_hope = "#\n"
        self.assertEqual(out_put.getvalue(), out_hope)
        Rect_test.width = 4
        Rect_test.height = 2
        out_put = io.StringIO()
        with redirect_stdout(out_put):
            Rect_test.display()
        out_hope = "\
####\n\
####\n\
"
        self.assertEqual(out_put.getvalue(), out_hope)

    def test_display_with_x_y(self):
        """Test display() with x and y"""
        Rect_test = Rectangle(7, 3, 2, 3, 4)
        out_put = io.StringIO()
        with redirect_stdout(out_put):
            Rect_test.display()
        out_hope = "\
\n\
\n\
\n\
  #######\n\
  #######\n\
  #######\n\
"
        self.assertEqual(out_put.getvalue(), out_hope)

        Rect_test = Rectangle(6, 5, 2, 3)
        out_put = io.StringIO()
        with redirect_stdout(out_put):
            Rect_test.display()
        out_hope = "\
\n\
\n\
\n\
  ######\n\
  ######\n\
  ######\n\
  ######\n\
  ######\n\
"
        self.assertEqual(out_put.getvalue(), out_hope)

        Rect_test = Rectangle(6, 5, 2, 3)
        out_put = io.StringIO()
        with redirect_stdout(out_put):
            Rect_test.display()
        out_hope = "\
\n\
\n\
\n\
  ######\n\
  ######\n\
  ######\n\
  ######\n\
  ######\n\
"
        self.assertEqual(out_put.getvalue(), out_hope)

        def test_display_no_x(self):
            """Test display() without x"""
            Rect_test = Rectangle(width=5, height=4, y=3)
            out_put = io.StringIO()
            with redirect_stdout(out_put):
                Rect_test.display()
            out_hope = "\
\n\
\n\
\n\
#####\n\
#####\n\
#####\n\
#####\n\
"
            self.assertEqual(out_put.getvalue(), out_hope)

            Rect_test = Rectangle(5, 7, 0, 2)
            out_put = io.StringIO()
            with redirect_stdout(out_put):
                Rect_test.display()
            out_hope = "\
\n\
\n\
#####\n\
#####\n\
#####\n\
#####\n\
#####\n\
#####\n\
#####\n\
"
            self.assertEqual(out_put.getvalue(), out_hope)

        def test_display_no_y(self):
            """Test display() without y"""
            Rect_test = Rectangle(width=5, height=4, x=4)
            out_put = io.StringIO()
            with redirect_stdout(out_put):
                Rect_test.display()
            out_hope = "\
    #####\n\
    #####\n\
    #####\n\
    #####\n\
"
            self.assertEqual(out_put.getvalue(), out_hope)

            Rect_test = Rectangle(3, 7, 6)
            out_put = io.StringIO()
            with redirect_stdout(out_put):
                Rect_test.display()
            out_hope = "\
      ###\n\
      ###\n\
      ###\n\
      ###\n\
      ###\n\
      ###\n\
      ###\n\
"
            self.assertEqual(out_put.getvalue(), out_hope)

# ---------------Task_6 Tests--------------------------------
    def test_str_no_self(self):
        """Test str without self"""
        Rect_test = Rectangle(5, 4, 4)
        with self.assertRaises(TypeError) as excep:
            Rectangle.__str__()
        message = "__str__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(excep.exception), message)

    def test_str_n_arg(self):
        """Test str() with different amount of arguments"""
        Rect_test = Rectangle(8, 12)
        message = '[Rectangle] (1) 0/0 - 8/12'
        self.assertEqual(str(Rect_test), message)
        Rect_test = Rectangle(8, 12, 3)
        message = '[Rectangle] (2) 3/0 - 8/12'
        self.assertEqual(str(Rect_test), message)
        Rect_test = Rectangle(8, 12, 3, 4)
        message = '[Rectangle] (3) 3/4 - 8/12'
        self.assertEqual(str(Rect_test), message)
        Rect_test = Rectangle(8, 12, 3, 4, 56)
        message = '[Rectangle] (56) 3/4 - 8/12'
        self.assertEqual(str(Rect_test), message)

# ---------------Tests: task 8 & 9--------------------------------

    def test_update_no_self(self):
        """Test update without self"""
        Rect_test = Rectangle(5, 9)
        with self.assertRaises(TypeError) as excep:
            Rectangle.update()
        message = "update() missing 1 required positional argument: 'self'"
        self.assertEqual(str(excep.exception), message)

        dic = Rect_test.__dict__.copy()
        Rect_test.update()
        self.assertEqual(Rect_test.__dict__, dic)

    def test_update_change_args(self):
        """Test update with different amount of arguments"""
        Rect_test = Rectangle(7, 4)
        dic = Rect_test.__dict__.copy()

        Rect_test.update(55)
        dic["id"] = 55
        self.assertEqual(Rect_test.__dict__, dic)

        Rect_test.update(55, 12)
        dic["_Rectangle__width"] = 12
        self.assertEqual(Rect_test.__dict__, dic)

        Rect_test.update(55, 12, 7)
        dic["_Rectangle__height"] = 7
        self.assertEqual(Rect_test.__dict__, dic)

        Rect_test.update(55, 12, 7, 1)
        dic["_Rectangle__x"] = 1
        self.assertEqual(Rect_test.__dict__, dic)

        Rect_test.update(55, 12, 7, 1, 5)
        dic["_Rectangle__y"] = 5
        self.assertEqual(Rect_test.__dict__, dic)

        Base._Base__nb_objects = 0
        Rect_test = Rectangle(2, 2, 2, 2, 2)
        self.assertEqual(str(Rect_test), "[Rectangle] (2) 2/2 - 2/2")

        Rect_test.update(23)
        self.assertEqual(str(Rect_test), "[Rectangle] (23) 2/2 - 2/2")

        Rect_test.update(11, 33)
        self.assertEqual(str(Rect_test), "[Rectangle] (11) 2/2 - 33/2")

        Rect_test.update(4, 13, 8)
        self.assertEqual(str(Rect_test), "[Rectangle] (4) 2/2 - 13/8")

        Rect_test.update(8, 1, 51, 3)
        self.assertEqual(str(Rect_test), "[Rectangle] (8) 3/2 - 1/51")

    def test_update_args_wrong(self):
        """Test update with different invalid arguments(args)"""
        Rect_test = Rectangle(11, 3)
        dic = Rect_test.__dict__.copy()

        with self.assertRaises(ValueError) as excep:
            Rect_test.update(9, 0)
        message = "width must be > 0"
        self.assertEqual(str(excep.exception), message)

        with self.assertRaises(ValueError) as excep:
            Rect_test.update(9, 1, -98)
        message = "height must be > 0"
        self.assertEqual(str(excep.exception), message)

        with self.assertRaises(ValueError) as excep:
            Rect_test.update(9, 1, 98, -4)
        message = "x must be >= 0"
        self.assertEqual(str(excep.exception), message)

        with self.assertRaises(ValueError) as excep:
            Rect_test.update(9, 1, 98, 4, -8)
        message = "y must be >= 0"
        self.assertEqual(str(excep.exception), message)

    def test_update_args_kwargs(self):
        """Test update with different valid arguments(kwargs)"""
        Rect_test = Rectangle(7, 4)
        dic = Rect_test.__dict__.copy()

        Rect_test.update(id=55)
        dic["id"] = 55
        self.assertEqual(Rect_test.__dict__, dic)

        Rect_test.update(width=12)
        dic["_Rectangle__width"] = 12
        self.assertEqual(Rect_test.__dict__, dic)

        Rect_test.update(height=7)
        dic["_Rectangle__height"] = 7
        self.assertEqual(Rect_test.__dict__, dic)

        Rect_test.update(x=1)
        dic["_Rectangle__x"] = 1
        self.assertEqual(Rect_test.__dict__, dic)

        Rect_test.update(y=5)
        dic["_Rectangle__y"] = 5
        self.assertEqual(Rect_test.__dict__, dic)

        Base._Base__nb_objects = 0
        Rect_test = Rectangle(2, 2, 2, 2, 2)
        self.assertEqual(str(Rect_test), "[Rectangle] (2) 2/2 - 2/2")

        Rect_test.update(x=23)
        self.assertEqual(str(Rect_test), "[Rectangle] (2) 23/2 - 2/2")

        Rect_test.update(y=12, x=33)
        self.assertEqual(str(Rect_test), "[Rectangle] (2) 33/12 - 2/2")

        Rect_test.update(y=4, x=13, height=8)
        self.assertEqual(str(Rect_test), "[Rectangle] (2) 13/4 - 2/8")

        Rect_test.update(height=8, y=1, width=51, x=3)
        self.assertEqual(str(Rect_test), "[Rectangle] (2) 3/1 - 51/8")

        def test_update_kwargs_wrong(self):
            """Test update with different invalid arguments(kwargs)"""
            Rect_test = Rectangle(11, 3)
        dic = Rect_test.__dict__.copy()

        with self.assertRaises(ValueError) as excep:
            Rect_test.update(id=9, height=0)
        message = "height must be > 0"
        self.assertEqual(str(excep.exception), message)

        with self.assertRaises(ValueError) as excep:
            Rect_test.update(width=-9, id=1, height=98)
        message = "width must be > 0"
        self.assertEqual(str(excep.exception), message)

        with self.assertRaises(ValueError) as excep:
            Rect_test.update(width=9, height=1, id=98, x=-4)
        message = "x must be >= 0"
        self.assertEqual(str(excep.exception), message)

        with self.assertRaises(ValueError) as excep:
            Rect_test.update(id=9, x=1, width=98, height=4, y=-8)
        message = "y must be >= 0"
        self.assertEqual(str(excep.exception), message)

        with self.assertRaises(ValueError) as excep:
            Rect_test.update(id=9, x=1, width=98, height=4, y=-8)
        message = "y must be >= 0"
        self.assertEqual(str(excep.exception), message)

# -----------------Tests: task 13---------------------------------

    def test_dictionary(self):
        """Test dictionary"""
        with self.assertRaises(TypeError) as excep:
            Rectangle.to_dictionary()
        message = "to_dictionary() missing 1 required \
positional argument: 'self'"
        self.assertEqual(str(excep.exception), message)

        Rect_test = Rectangle(5, 78)
        dic = {'id': 1, 'y': 0, 'height': 78, 'width': 5, 'x': 0}
        self.assertEqual(Rect_test.to_dictionary(), dic)

        Rect_test = Rectangle(5, 78, 5, 2, 9)
        dic = {'id': 9, 'y': 2, 'height': 78, 'width': 5, 'x': 5}
        self.assertEqual(Rect_test.to_dictionary(), dic)

        Rect_test1 = Rectangle(1, 4, 5, 6, 2)
        Rect_test1_dic = Rect_test1.to_dictionary()
        Rect_test2 = Rectangle(4, 8, 7, 90, 3)
        Rect_test2.update(**Rect_test1_dic)
        self.assertEqual(str(Rect_test1), str(Rect_test2))

        Rect_test.update(12, 5, 67, 4, 8)
        dic = {'height': 67, 'x': 4, 'id': 12, 'width': 5, 'y': 8}
        self.assertEqual(Rect_test.to_dictionary(), dic)


if __name__ == "__main__":
    unittest.main()
