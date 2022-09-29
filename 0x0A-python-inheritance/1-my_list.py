#!/usr/bin/python3
"""
This module contains the MyList class
"""


class MyList(list):
    """The Mylist class inherits from list and adds functionality"""

    def print_sorted(self):
        print(sorted(self))
