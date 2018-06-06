#!/usr/bin/env python3

'''
Path sum: two ways
Problem 81 

In the 5 by 5 matrix below, the minimal path sum from the top left to the 
bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.

 [131] 673   234   103    18
 [201] [96] [342]  965   150
 630   803  [746] [422]  111
 537   699   497  [121]  956
 805   732   524   [37] [331]

Find the minimal path sum, in matrix.txt, a 31K text file containing a 80 by 80 
matrix, from the top left to the bottom right by only moving right and down.

'''

mat = [[131, 673, 234, 103, 18 ],
     [201,  96, 342, 965, 150],
     [630, 803, 746, 422, 111],
     [537, 699, 497, 121, 956],
     [805, 732, 524,  37, 331]]


mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

from pprint import pprint

'''
mat = []
with open('p081_matrix.txt') as f:
    for line in f:
        mat.append([int(x) for x in line.split(',')])
'''

mins = [[False] * len(mat[0])] * len(mat)

move_count = len(mat) + len(mat[0]) - 2
path_count = 2**move_count
sums = []

for i in range(path_count):

    total = mat[0][0]
    x, y = 0, 0

    move_bin = "{0:b}".format(i).zfill(move_count)
    move_list = [int(x) for x in list(move_bin)]
    move_sum = sum(move_list)

    if move_sum == len(mat[0])-1:
        for move in move_list:
            if move == 1:
                x, y = x+1, y
            else:
                x, y = x, y+1
            total += mat[y][x]
            print('setting (', x, y, ') to', total)
            mins[y][x] = total
            pprint(mins)

        sums.append(total)

print(min(sums))
