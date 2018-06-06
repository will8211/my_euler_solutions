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

full_primes = generate_primes(100000000)
p_set = set(full_primes)

primes = generate_primes(674, 10000000)
four = [3, 7, 109, 673]

for n in primes:
    print(n)
    okay = True
    for m in four:
        str_n = str(n)
        str_m = str(m)
        a = int(str_n + str_m)
        b = int(str_m + str_n)
        if not ((a in p_set) and (b in p_set)):
            print(n, m, 'is not okay!!!')
            okay = False
            break
        print(n, m, 'is alright')
        input()
    if okay:
        print(sum(four+[n]))
        print(n)
        exit()

