#!/usr/bin/python3
"""Module 4-inherits_from"""


def inherits_from(obj, a_class):
    """Check if an obj is a subclass"""
    if type(obj) != a_class:
        return issubclass(type(obj), a_class)
    else:
        return False
