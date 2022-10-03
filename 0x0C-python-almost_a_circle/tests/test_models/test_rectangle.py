#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
from models.base import Base
import io
import contextlib
"""
Module for unittests for the Rectangle class
"""


class TestRectangleClassCreation(unittest.TestCase):
    """Test class for Rectangle class instantiation tests"""

    def test_no_args(self):
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_height_only(self):
        with self.assertRaises(TypeError):
            r = Rectangle(3)

    def test_height_width(self):
        r = Rectangle(3, 4)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)

    def test_inf_input(self):
        with self.assertRaises(TypeError):
            Rectangle(float('inf'), 4, 5, 6)
        with self.assertRaises(TypeError):
            Rectangle(2, float('inf'), 5, 6)
        with self.assertRaises(TypeError):
            Rectangle(2, 3, float('inf'), 6)
        with self.assertRaises(TypeError):
            Rectangle(2, 3, 4, float('inf'), 6)

    def test_neg_inf_input(self):
        with self.assertRaises(TypeError):
            Rectangle(float('-inf'), 4, 5, 6)
        with self.assertRaises(TypeError):
            Rectangle(2, float('-inf'), 5, 6)
        with self.assertRaises(TypeError):
            Rectangle(2, 3, float('-inf'), 6)
        with self.assertRaises(TypeError):
            Rectangle(2, 3, 4, float('-inf'), 6)

    def test_nan_input(self):
        with self.assertRaises(TypeError):
            Rectangle(float('nan'), 4, 5, 6)
        with self.assertRaises(TypeError):
            Rectangle(2, float('nan'), 5, 6)
        with self.assertRaises(TypeError):
            Rectangle(2, 3, float('nan'), 6)
        with self.assertRaises(TypeError):
            Rectangle(2, 3, 4, float('nan'), 6)

    def test_width_height_x(self):
        r = Rectangle(3, 4, 5, 6)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 6)
        self.assertIsNotNone(id)

    def test_check_int_creation(self):
        with self.assertRaises(TypeError):
            r = Rectangle('f', 4, 5, 6, 7)
        with self.assertRaises(TypeError):
            r = Rectangle(2, 'f', 5, 6, 7)
        with self.assertRaises(TypeError):
            r = Rectangle(2, 3, 'f', 6, 7)
        with self.assertRaises(TypeError):
            r = Rectangle(2, 3, 5, 'f', 7)

    def test_check_int(self):
        with self.assertRaises(TypeError):
            Rectangle.check_int('f', int)
        with self.assertRaises(TypeError):
            Rectangle.check_int([], int)
        with self.assertRaises(TypeError):
            Rectangle.check_int(float('nan'), int)

    def test_check_gr_0_creation(self):
        with self.assertRaises(ValueError):
            r = Rectangle(0, 4, 5, 6, 7)
        with self.assertRaises(ValueError):
            r = Rectangle(2, -1, 5, 6, 7)

    def test_check_gr_eq_0_creation(self):
        with self.assertRaises(ValueError):
            r = Rectangle(3, 4, -1, 5, 6)
        with self.assertRaises(ValueError):
            r = Rectangle(3, 4, 3, -5, 6)


class TestAreaMethod(unittest.TestCase):
    """Test area method for Rectangle class"""

    def test_area_creation(self):
        r = Rectangle(3, 4, 3, 5, 6)
        self.assertEqual(r.area(), 12)


class TestDisplayMethod(unittest.TestCase):
    """Test display method for Rectangle class"""

    def setUp(self):
        self.r1 = Rectangle(4, 6)
        self.p1 = "####\n####\n####\n####\n####\n####\n"
        self.r2 = Rectangle(2, 2)
        self.p2 = "##\n##\n"
        self.r3 = Rectangle(2, 3, 2, 2)
        self.p3 = "\n\n  ##\n  ##\n  ##\n"
        self.r4 = Rectangle(3, 2, 1, 0)
        self.p4 = " ###\n ###\n"

    def test_display_1(self):
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            self.r1.display()
        ret = f.getvalue()
        self.assertEqual(self.p1, ret)

    def test_display_2(self):
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            self.r2.display()
        ret = f.getvalue()
        self.assertEqual(self.p2, ret)

    def test_display_offset_3(self):
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            self.r3.display()
        ret = f.getvalue()
        self.assertEqual(self.p3, ret)

    def test_display_offset_4(self):
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            self.r4.display()
        ret = f.getvalue()
        self.assertEqual(self.p4, ret)


class TestStrMethod(unittest.TestCase):
    """Test __str__  method for Rectangle class"""

    def test_str_output(self):
        r = Rectangle(3, 4, 5, 6, 4)
        r_string = '[Rectangle] (4) 5/6 - 3/4'
        self.assertEqual(r_string, r.__str__())


class TestUpdateMethod(unittest.TestCase):
    """Test update method of the Rectangle class"""

    def test_no_input(self):
        r = Rectangle(3, 4, 5, 6, 4)
        r.update()
        self.assertEqual(r.id, 4)

    def test_one_input(self):
        r = Rectangle(3, 4, 5, 6, 4)
        r.update(9)
        self.assertEqual(r.id, 9)

    def test_two_inputs(self):
        r = Rectangle(3, 4, 5, 6, 4)
        r.update(9, 20)
        self.assertEqual(r.width, 20)

    def test_three_inputs(self):
        r = Rectangle(3, 4, 5, 6, 4)
        r.update(9, 20, 23)
        self.assertEqual(r.height, 23)

    def test_four_inputs(self):
        r = Rectangle(3, 4, 5, 6, 4)
        r.update(9, 20, 23, 32)
        self.assertEqual(r.x, 32)

    def test_five_inputs(self):
        r = Rectangle(3, 4, 5, 6, 4)
        r.update(9, 20, 23, 32, 83)
        self.assertEqual(r.y, 83)

    def test_kargs_skipped(self):
        r = Rectangle(3, 4, 5, 6, 4)
        r.update(9, 20, 23, 32, 83, id=4, y=8, width=10)
        self.assertEqual(r.id, 9)
        self.assertEqual(r.y, 83)
        self.assertEqual(r.width, 20)

    def test_kargs(self):
        r = Rectangle(3, 4, 5, 6, 4)
        r.update(id=4, x=5, y=8, width=10, height=20)
        self.assertEqual(r.id, 4)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 8)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)


class TestToDictMethod(unittest.TestCase):
    """Testcases for rectangle dictionary method"""

    def test_correct_output_str_(self):
        Rectangle.reset_id()
        r1 = Rectangle(10, 2, 1, 9)
        self.assertEqual(str(r1), '[Rectangle] (1) 1/9 - 10/2')

    def test_isinstance(self):
        Rectangle.reset_id()
        r1 = Rectangle(10, 2, 1)
        rd = r1.to_dictionary()
        self.assertIsInstance(rd, dict)

    def test_correct_dict(self):
        Rectangle.reset_id()
        r1 = Rectangle(10, 2, 1, 9)
        rd = r1.to_dictionary()
        cd = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(rd, cd)

    def test_update_dict_kwargs(self):
        Rectangle.reset_id()
        r1 = Rectangle(10, 2, 1, 9)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle(1, 1)
        r2.update(**r1_dict)
        self.assertEqual(str(r2), '[Rectangle] (1) 1/9 - 10/2')

    def test_update_dict_changes_object(self):
        Rectangle.reset_id()
        r1 = Rectangle(10, 2, 1, 9, 3)
        rd = r1.to_dictionary()
        r2 = Rectangle(1, 1)
        r2.update(**rd)
        self.assertTrue(r1 != r2)


if __name__ == '__main__':
    unittest.main()
