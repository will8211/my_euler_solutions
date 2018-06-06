#!/usr/bin/env python3

'''
Prime permutations
Problem 49

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms 
increases by 3330, is unusual in two ways: (i) each of the three terms are 
prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, 
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this 
sequence?
'''

import primes as p

numbers = [n for n in range(1488, 10000) if p.check_primeness(n)]

for i, x in enumerate(numbers):
    for y in numbers[i+1:]:
        z = 2*y-x
        if z in numbers:
            a, b, c = str(x), str(y), str(z)
            ok = True
            for t in (a, b ,c), (b, c, a), (c, a, b):
                for d in t[0]:
                    if not d in t[1] or not d in t[2]:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                print(a, b, c, '-->', a+b+c)
                exit()
