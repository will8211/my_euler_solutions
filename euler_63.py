#!/usr/bin/env python3

'''
Powerful digit counts
Problem 63

The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit 
number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
'''

d = {}
tally = 0

for n in range(100):
    in_range = True
    i = 1
    d[n] = []
    while in_range:
        p = i**n
        if 10**(n-1) <= p < 10**n:
            d[n].append(p)
            tally += 1
        elif p >= 10**exp:
            in_range = False
        i += 1

print(d)
print('Answer:', tally)
