#!/usr/bin/env python3

'''
Summation of primes
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

from primesieve import primes

print(sum(primes(2000000)))

'''
from math import sqrt

def check_primeness(x):
    for i in range(2, int(sqrt(x))+1):
        if (x % i == 0):
            return False
    return True

my_sum = 0

for i in range(2, 2000000):
    if check_primeness(i):
        my_sum += i

print(my_sum)
'''
