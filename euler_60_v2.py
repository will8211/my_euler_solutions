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

friends_d = {}
limit = 10000
primes = generate_primes(limit)
primes_d = {x: True for x in primes}
depth = 5

def prime_check(n):
    if not n in primes_d:
        test = generate_primes(n, n)
        primes_d[n] = len(test)
    return primes_d[n]

def cat_check(n, m):
    str_n = str(n)
    str_m = str(m)
    a = int(str_n + str_m)
    b = int(str_m + str_n)
    return (prime_check(a) and prime_check(b))

for i, n in enumerate(primes):
    friends = []
    for m in primes[i+1:]:
        if cat_check(n, m):
            friends.append(m)
    friends_d[n] = friends

def deeper(n, so_far=[]):
    if len(so_far) == depth-1:
        print(so_far + [n], sum(so_far + [n]))
    if len(so_far) < depth:
        for f in friends_d[n]:
            if f in friends_d:
                compat = True
                for m in so_far:
                    if not f in friends_d[m]:
                        compat = False
                if compat:
                    deeper(f, so_far+[n])

new_primes = sorted([x for x in friends_d])

for n in new_primes:
    deeper(n)


'''
d = {}

def check(n):
    if not n in d:
        test = generate_primes(n, n)
        d[n] = len(test)
    return d[n]

limit = 30000
primes = generate_primes(limit)
singles = [[x] for x in primes if x <= limit/5 ]

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
'''
