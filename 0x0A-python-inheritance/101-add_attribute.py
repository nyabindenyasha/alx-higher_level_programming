#!/usr/bin/python3
"""Module that holds add_attribute function"""


def add_attribute(obj, attr_name, attr_value):
    """
    A function that adds a new attribute to an object
    if it's possible
    """

    if hasattr(obj, '__dict__'):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
