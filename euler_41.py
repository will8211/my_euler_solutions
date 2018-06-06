#!/usr/bin/env python3

'''
Pandigital prime
Problem 41

We shall say that an n-digit number is pandigital if it makes use of all the 
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is 
also prime.

What is the largest n-digit pandigital prime that exists?
'''

from math import sqrt
from itertools import permutations

primes = {0:False, 1:False}
def check_primeness(x):
    x = abs(x)
    if x in primes:
        return primes[x]
    else:
        root = sqrt(x)
        for i in range(2, int(root)+1):
            if x % i == 0:
                primes[x] = False
                return False
        primes[x] = True
        return True

for length in reversed(range(4, 11)):
    digits = reversed(range(1, length))
    for p in permutations([x for x in digits]):
        s = map(str, p)
        n = int(''.join(list(s)))
        if check_primeness(n):
            print(n)
            exit()
