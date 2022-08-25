#!/usr/bin/python3
for l in range(ord('z'), ord('a') - 1, -1):
    if (l % 2 != 0):
        l = l - 32
    l = chr(l)
    print("{}".format(l), end='')
