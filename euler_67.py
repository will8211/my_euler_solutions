#!/usr/bin/env python3
#
# Project Euler Problem 67
#

triangle = []

# Build triangle from text file
with open("p067_triangle.txt") as f:
    for line in f:
        integers = list(map(int, line.split()))
        triangle.append(integers)

# Copied from Problem 18
for level in reversed(range(0, len(triangle)-1)):
    for block in range(len(triangle[level])):
        left = triangle[level+1][block]
        right = triangle[level+1][block+1]
        if left > right:
             triangle[level][block] += left
        else:
             triangle[level][block] += right

print(triangle[0][0])
