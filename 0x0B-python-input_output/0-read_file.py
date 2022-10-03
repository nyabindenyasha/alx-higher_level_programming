#!/usr/bin/python3
"""Module 0"""


def read_file(filename=""):
    """Read a file"""
    with open(filename, mode="r", encoding="utf-8") as myfile:
        print(myfile.read(), end="")
