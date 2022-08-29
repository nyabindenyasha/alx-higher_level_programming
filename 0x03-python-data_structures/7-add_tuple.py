#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    temp = ()
    for x in range(2):
        if x < len(tuple_a) and x < len(tuple_b):
            temp += (tuple_a[x] + tuple_b[x],)
        elif x >= len(tuple_b) and x < len(tuple_a):
            temp += (tuple_a[x],)
        elif x >= len(tuple_a) and x < len(tuple_b):
            temp += (tuple_b[x],)
        else:
            temp += (0, )
    return temp
