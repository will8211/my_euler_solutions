#!/usr/bin/env python3

'''
Counting rectangles
Problem 85 

By counting carefully it can be seen that a rectangular grid measuring 3 by 2 
contains eighteen rectangles:

  X--  XX-  XXX
  ---  ---  ---
   6    4    2

  X--  XX-  XXX
  X--  XX-  XXX
   3    2    1

Although there exists no rectangular grid that contains exactly two million 
rectangles, find the area of the grid with the nearest solution.
'''

TARGET_RECTANGLES = 2000000

def count_rectangles(grid_width, grid_height):

    rectangles = 0

    for x in range(1, grid_width+1):
        for y in range(1, grid_height+1):
            horizontals = grid_width - x + 1
            verticals = grid_height - y + 1
            rectangles += horizontals * verticals

    return rectangles


solved = False
grid_width = 1
grid_height = 1
results = []

while len(results) < 1000:

    #print(grid_width, 'x', grid_height)
    size = grid_width * grid_height
    count = count_rectangles(grid_width, grid_height)
    if count > TARGET_RECTANGLES:
        results.append(size)
        if size == 2772: print(grid_width, 'x', grid_height)

    if grid_width < grid_height:
        grid_width += 1
    else:
        grid_width = 1
        grid_height += 1

    previous = count

print(min(results))
