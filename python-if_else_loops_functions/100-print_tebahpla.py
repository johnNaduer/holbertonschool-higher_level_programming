#!/usr/bin/env python3
x = ord('z')
y = ord('Y')
while x >= ord('a') and y >= ord('A'):
    print("{}{}".format(chr(x),chr(y)),end="")
    x = x - 2
    y = y - 2
