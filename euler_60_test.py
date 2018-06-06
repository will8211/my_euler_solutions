#!/usr/bin/env python3

'''
Prime pair sets
Problem 60

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes 
and concatenating them in any order the result will always be prime. For 
example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four 
primes, 792, represents the lowest sum for a set of four primes with this 
property.

Find the lowest sum for a set of five primes for which any two primes 
concatenate to produce another prime.
'''

from primesieve import generate_primes

d = {}

def check(n):
    if not n in d:
        test = generate_primes(n, n)
        d[n] = len(test)
    return d[n]

limit = 30000
primes = generate_primes(limit)
singles = [[x] for x in primes if x <= 20 ]

def next_set(prev_set, current, lim):
    for n in primes:
        if n > lim:
            break
        for s in prev_set:
            okay = True
            for m in s:
                if (n > m) and (n+m < limit):
                    str_n = str(n)
                    str_m = str(m)
                    a = int(str_n + str_m)
                    b = int(str_m + str_n)
                    if not (check(a) and check(b)):
                        okay = False
                        break
                else:
                    okay = False
                    break
            if okay:
                current.append(s + [n])

pairs = []
next_set(singles, pairs, limit/4)
print('Pairs:', pairs)

triplets = []
next_set(pairs, triplets, limit/3)
print('\nTriples:', triplets)

quads = []
next_set(triplets, quads, limit/2)
print('\nQuads:', quads)

quints = []             
next_set(quads, quints, limit)
print('\nQUINTS:', quints)

print('\nSUMS:', list(map(sum, quints)))
