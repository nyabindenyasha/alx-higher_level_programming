#!/usr/bin/python3
""" Module 8-base_geometry"""


class BaseGeometry:
    """Class BaseGeometry"""
    def area(self):
        """Area method"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """integer_validator function"""
        if type(value) != int:
            raise TypeError(name + ' must be an integer')
        if value <= 0:
            raise ValueError(name + ' must be greater than 0')


class Rectangle(BaseGeometry):
    """Class BaseGeometry"""

    def __init__(self, width, height):
        """Init method"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
