#!/usr/bin/python3


def read_lines(filename="", nb_lines=0):
    with open(filename, mode="r", encoding="utf-8") as myfile:
        counter = 0
        for line in myfile:
            if counter == nb_lines and nb_lines > 0:
                break
            print(line, end="")
            counter += 1
    myfile.close()
