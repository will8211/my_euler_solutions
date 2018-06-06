#!/usr/bin/env python3

'''
Smallest multiple
Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
'''

# How did I figure this out?

n = 1 #number to check
m = 1 #multiple to jump by
f = 1 #factor to check

while f <= 20:
    if n % f == 0:
        f += 1
        m = n
    else:
        n += m

print(n)
