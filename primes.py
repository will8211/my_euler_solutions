#!/usr/bin/env python3

from math import sqrt

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
