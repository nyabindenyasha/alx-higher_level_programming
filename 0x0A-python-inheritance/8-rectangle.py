#!/usr/bin/python3
"""
Module that holds rectangle class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class for Rectangle"""

    def __init__(self, width, height):
        """Initiate an instance with attritubtes"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
