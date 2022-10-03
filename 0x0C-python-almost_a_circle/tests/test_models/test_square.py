#!/usr/bin/python3
"""
Module for unittests for the Square class
"""
import unittest
from models.square import Square
from models.base import Base


class TestSquareClassCreation(unittest.TestCase):
    """Test class for Square class instantiation tests"""

    def test_no_args(self):
        with self.assertRaises(TypeError):
            r = Square()

    def test_size(self):
        r = Square(3)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.width, 3)

    def test_inf_input(self):
        with self.assertRaises(TypeError):
            Square(float('inf'), 5, 6)
        with self.assertRaises(TypeError):
            Square(2, float('inf'), 5)
        with self.assertRaises(TypeError):
            Square(2, 3, float('inf'))

    def test_neg_inf_input(self):
        with self.assertRaises(TypeError):
            Square(float('-inf'), 5, 6)
        with self.assertRaises(TypeError):
            Square(2, float('-inf'), 5)
        with self.assertRaises(TypeError):
            Square(2, 3, float('-inf'))

    def test_nan_input(self):
        with self.assertRaises(TypeError):
            Square(float('nan'), 5, 6)
        with self.assertRaises(TypeError):
            Square(2, float('nan'), 5)
        with self.assertRaises(TypeError):
            Square(2, 3, float('nan'))

    def test_width_height_x(self):
        r = Square(3, 5, 6)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 6)
        self.assertIsNotNone(id)

    def test_check_int_creation(self):
        with self.assertRaises(TypeError):
            r = Square('f', 5, 6, 7)
        with self.assertRaises(TypeError):
            r = Square(2, 'f', 5, 6)
        with self.assertRaises(TypeError):
            r = Square(2, 3, 'f', 6)

    def test_check_int_creation_list(self):
        with self.assertRaises(TypeError):
            r = Square([], 5, 6, 7)
        with self.assertRaises(TypeError):
            r = Square(2, [], 5, 6)
        with self.assertRaises(TypeError):
            r = Square(2, 3, [], 6)

    def test_check_int_creation_dict(self):
        with self.assertRaises(TypeError,
                               msg="width must be an integer"):
            r = Square({}, 6, 7)
        with self.assertRaises(TypeError):
            r = Square(2, {}, 6)
        with self.assertRaises(TypeError):
            r = Square(2, 3, {})

    def test_str_(self):
        Square.reset_id()
        r = Square(3, 2, 4)
        self.assertEqual(str(r), "[Square] (1) 2/4 - 3")


class TestSquareSetterGetter(unittest.TestCase):
    """Testcases for square setter and getter"""

    def test_size_setter(self):
        s = Square(5)
        self.assertEqual(s.size, 5)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            s = Square('f')


class TestUpdateMethod(unittest.TestCase):
    """Testcases for the square update method"""

    def test_update(self):
        s1 = Square(5, 0, 0, 1)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        s1.update(10)
        self.assertEqual(str(s1), "[Square] (10) 0/0 - 5")
        s1.update(1, 2)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 2")
        s1.update(1, 2, 3)
        self.assertEqual(str(s1), "[Square] (1) 3/0 - 2")
        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (1) 3/4 - 2")
        s1.update(x=12)
        self.assertEqual(str(s1), "[Square] (1) 12/4 - 2")
        s1.update(size=7, y=1)
        self.assertEqual(str(s1), "[Square] (1) 12/1 - 7")
        s1.update(size=7, id=89, y=1)
        self.assertEqual(str(s1), "[Square] (89) 12/1 - 7")


class TestToDictionaryMethod(unittest.TestCase):
    """Testcases for the to dictionary method"""

    def setUp(self):
        Base.reset_id()
        self.s1 = Square(10, 2, 1)
        self.s1_dictionary = self.s1.to_dictionary()
        self.s2 = Square(1, 1)
        self.s2.update(**self.s1_dictionary)

    def test_isinstance(self):
        self.assertIsInstance(self.s1_dictionary, dict)

if __name__ == '__main__':
    unittest.main()
