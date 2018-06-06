#!/usr/bin/env python3

'''
Largest palindrome product
Problem 4

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

l = []

for i in reversed(range(900, 1000)):
    for j in reversed(range(900, 1000)):
        n = i*j
        if str(n) == str(n)[::-1]:
            l.append(n)

print(max(l))
