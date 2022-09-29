#!/usr/bin/python3
"""Module 10-base_geometry"""


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
        """Init"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Find the Area"""
        return self.__width * self.__height

    def __str__(self):
        """Overcharge __str__"""
        string = "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
        return string


class Square(Rectangle):
    """Class Square"""

    def __init__(self, size):
        """Init Square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Find the area"""
        return self.__size ** 2
