#!/usr/bin/env python3

'''
Integer right triangles
Problem 39

If p is the perimeter of a right angle triangle with integral length sides, 
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?

'''

from math import sqrt

d = {n: [] for n in range(1, 1001)}

for a in range(1, 501):
    for b in range(a+1, 501):
        c = sqrt(a**2 + b**2)
        per = a+b+c
        if c % 1 == 0 and per <= 1000:
            d[int(per)].append((a, b, int(c)))

l = [(len(v), k) for k, v in d.items()]
a = max(l)

print(a[1], 'with', a[0], 'possibilities:')
for p in d[a[1]]:
    print(p)
