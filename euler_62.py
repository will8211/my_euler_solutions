#!/usr/bin/env python3

'''
Cubic permutations
Problem 62

The cube, 41063625 (345^3), can be permuted to produce two other cubes: 
56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube 
which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are 
cube.
'''

d = {}
i = 345

while True:
    cube = i**3
    s = ''.join(sorted(str(cube)))
    try:
        d[s] = d[s] + [cube]
    except KeyError:
        d[s] = [cube]
    if len(d[s]) == 5:
        print(d[s][0])
        exit()
    i += 1
