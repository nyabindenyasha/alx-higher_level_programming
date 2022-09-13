#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    i = 0
    while (i < x):
        try:
            print(my_list[i], end='')
            counter += 1
        except:
            break
        i += 1
    print()

    return counter
