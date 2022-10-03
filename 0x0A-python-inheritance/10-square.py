#!/usr/bin/python3
"""
Module that holds square class
"""
Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle, BaseGeometry):
    """Class for Square"""

    def __init__(self, size):
        """Initiate a new square with attributes"""
        BaseGeometry.integer_validator(self, name="size", value=size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of a square"""
        return(self.__size * self.__size)
