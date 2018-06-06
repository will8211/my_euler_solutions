#!/usr/bin/env python3

'''
Lattice paths
Problem 15

Starting in the top left corner of a 2×2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

    XXXXXXXXX    XXXXX---+    XXXXX---+
    |   |   X    |   X   |    |   X   |
    +---+---X    +---XXXXX    +---X---+
    |   |   X    |   |   X    |   X   |
    +---+---X    +---+---X    +---XXXXX

    X---+---+    X---+---+    X---+---+
    X   |   |    X   |   |    X   |   |
    XXXXXXXXX    XXXXX---+    X---+---+
    |   |   X    |   X   |    X   |   |
    +---+---X    +---XXXXX    XXXXXXXXX

How many such routes are there through a 20×20 grid?
'''

from pprint import pprint

my_dict = {}

def compute(x, y):
    name = str(x).zfill(2)+"x"+str(y).zfill(2)
    x_paths = 0
    y_paths = 0
    if name in my_dict:
        return my_dict[name]
    if x == 0:
        return 1
    else:
        x_paths = compute(x-1, y)
    if y == 0:
        return 1
    else:
        y_paths = compute(y-1, x)
    paths =  x_paths + y_paths
    my_dict[name] = paths
    return paths

for dimentions in range(1, 21):
    compute(dimentions, dimentions)

pprint(my_dict)
print(my_dict["20x20"])
