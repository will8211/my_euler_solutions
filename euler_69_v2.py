#!/usr/bin/env python3

'''
Totient maximum
Problem 69

Euler's Totient function, φ(n) [sometimes called the phi function], is used to 
determine the number of numbers less than n which are relatively prime to n. 
For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively 
prime to nine, φ(9)=6.

n   Relatively Prime    φ(n)    n/φ(n)      Inverse
2   1                   1       2           
3   1,2                 2       1.5         
4   1,3                 2       2           2
5   1,2,3,4             4       1.25        
6   1,5                 2       3           2 3 4
7   1,2,3,4,5,6         6       1.1666...   
8   1,3,5,7             4       2           2   4   6
9   1,2,4,5,7,8         6       1.5           3     6
10  1,3,7,9             4       2.5         2   4 5 6 8

It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
'''

from pprint import pprint
from math import ceil
from primesieve import generate_primes

limit = 1000000
inverses = { key: 0 for key in range(2, limit+1) }
primes = generate_primes(limit)

#def check_prime(n):
#    return len(generate_primes(n, n))

for p in primes:
    for n in range(p*2, limit+1, p):
        inverses[n] += int((n-1)/p)
        #if n == 90: print('added', int((n-1)/p), 'multiple(s) of', p, 'to N', n)

pprint(inverses[90])

numbers = {}
for key, value in inverses.items():
    #print('N', key)
    sigma = key-1-value
    #print('sigma', sigma, '\n')
    try:
        n_over_sigma = key/sigma
    except ZeroDivisionError:
        n_over_sigma = 0
    numbers[n_over_sigma] = key
    #print('n', key, 'sigma', sigma, 'n/s', n_over_sigma)

#pprint(numbers)

print(numbers[max(numbers)], '->', max(numbers))
