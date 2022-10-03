#!/usr/bin/python3
"""Module 100-my_int"""


class MyInt(int):
    """Class MyInt"""

    def __init__(self, value):
        """Init method"""
        self.value = value

    def __eq__(self, other):
        """Rebel equal"""
        if isinstance(other, MyInt):
            return self.value == other.value
        return False

    def __ne__(self, other):
        """Rebel not equal"""
        return not self.__eq__(other)
