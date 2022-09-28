#!/usr/bin/python3


def number_of_lines(filename=""):
    with open(filename, mode="r", encoding="utf-8") as myfile:
        counter = 0
        for line in myfile:
            counter += 1
    myfile.close()
    return counter
