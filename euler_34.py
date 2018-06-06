#!/usr/bin/env python3

'''
Digit factorials
Problem 34

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of 
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

'''

from math import factorial

l = []

for i in range(3, 100000):
    my_sum = 0
    for d in str(i):
        my_sum += factorial(int(d))
        if my_sum > i:
            break
    if i == my_sum:
        l.append(i)
        print(i)

print('=', sum(l))
