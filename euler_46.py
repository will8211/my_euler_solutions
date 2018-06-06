#!/usr/bin/env python3

'''
Goldbach's other conjecture
Problem 46

It was proposed by Christian Goldbach that every odd composite number can be 
written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a 
prime and twice a square?

'''

from math import sqrt

primes = set()
composites = set()

def check_type(x):
    x = abs(x)
    if x in primes:
        return 'p'
    elif x in composites:
        return 'c'
    else:
        root = sqrt(x)
        for i in range(2, int(root)+1):
            if x % i == 0:
                composites.add(x)
                return 'c'
        primes.add(x)
        return 'p'

for n in range(2,1000000):
    n_type = check_type(n)
    if n_type == 'c' and n % 2:
        proved = False
        for p in primes:
            if sqrt((n-p)/2) % 1 == 0:
                proved = True
                break
        if not proved:
            print('Answer:', n)
            break



