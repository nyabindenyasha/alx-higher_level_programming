#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class for test"""

    def test_numbers(self):
        """Test with numbers"""
        self.assertEqual(max_integer([]), None)

    def test_1(self):
        """Test with numbers"""
        self.assertEqual(max_integer([752]), 752)

    def test_2(self):
        """Test with numbers"""
        self.assertEqual(max_integer(), None)

    def test_3(self):
        """Test with numbers"""
        self.assertEqual(max_integer([5, -15843, 7, 9456, 752]), 9456)

    def test_4(self):
        """Test with numbers"""
        self.assertEqual(max_integer([-5, -15843, -7, -9456, -752]), -5)

    def test_5(self):
        """Test with numbers"""
        self.assertEqual(max_integer([0, -15843, 7, 9456, 752]), 9456)

    def test_6(self):
        """Test with numbers"""
        self.assertEqual(max_integer([3, 3, 3, 3, 3]), 3)

    def test_7(self):
        """Test with numbers"""
        self.assertEqual(max_integer('zapato'), 'z')

    def test_8(self):
        """Test with numbers"""
        self.assertEqual(max_integer([]), None)

    def test_9(self):
        """Test with numbers"""
        with self.assertRaises(TypeError):
            max_integer([(1, 67, 3, 5), "hello"])

    def test_A(self):
        """Test with numbers"""
        with self.assertRaises(TypeError):
            max_integer([[5, 5], [79], '89', [75]])

    def test_B(self):
        """Test with numbers"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_C(self):
        """Test with numbers"""
        with self.assertRaises(TypeError):
            max_integer([5, 5, 79, '89', 75])

    def test_D(self):
        """Test with numbers"""
        self.assertEqual(max_integer([0, -15, 7, 94, 752, 645631]), 645631)


if __name__ == '__main__':
    unittest.main()
