#!/usr/bin/python3
"""
Module that holds square class
"""
Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle):
    """Class for Square"""

    def __init__(self, size):
        """Initiate a square with attributes"""
        BaseGeometry.integer_validator(self, name="size", value=size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of an object"""
        return(self.__size * self.__size)

    def __str__(self):
        """Return the string representation of an object"""
        return("[Square] {}/{}".format(self.__size, self.__size))
