#!/usr/bin/env python3

'''
Truncatable primes
Problem 37

The number 3797 has an interesting property. Being prime itself, it is possible 
to continuously remove digits from left to right, and remain prime at each 
stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 
379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to 
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

'''

import re
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

hits = []
n = 23

while len(hits) < 11:
    s = str(n)
    value = True
    if re.match('[2357][0-9]*[2357]', s) and check_primeness(n):
        for i in range(1, len(s)):
            if (not check_primeness(int(s[:i])) or 
                not check_primeness(int(s[i:]))):
                value = False
                break
    else:
        value = False
    if value == True:
        print(n)
        hits.append(n)
    n += 2

print('\n->', sum(hits))
