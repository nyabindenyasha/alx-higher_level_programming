#!/usr/bin/python3
"""Module 1"""


class MyList(list):
    """Class MyList"""
    def print_sorted(self):
        """Print a sorted list"""
        tmp = self.copy()
        print(sorted(tmp))
