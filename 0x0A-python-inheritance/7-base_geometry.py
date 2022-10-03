#!/usr/bin/python3
"""
Module that holds base geometry class
"""


class BaseGeometry:
    """Class for Base Geometry"""

    def area(self):
        """Returns the area of an object"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Raises an exception if the the value doesn't pass tests"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if type(value) == bool:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
