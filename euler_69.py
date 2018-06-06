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
from primesieve import generate_primes

limit = 1000000
primes = generate_primes(limit)

inverses = { key: set() for key in range(2, limit+1) }

def check_prime(n):
    return len(generate_primes(n, n))

for p in primes:
    #print('\nADDING PRIME', p, '\n')
    #if check_prime(p):
        for n in range(p*2, limit+1, p):
            #print('adding', p, 'to n', n)
            for inverse in range(p, n-1, p):
                #print(inverse)
                inverses[n].add(inverse)

print('Done building inverses dict\n')

numbers = {}
for key, value in inverses.items():
    #print(key, value)
    sigma = key-1-len(value)
    #print('sigma', sigma, '\n')
    try:
        n_over_sigma = key/sigma
    except ZeroDivisionError:
        n_over_sigma = 0
    numbers[n_over_sigma] = key
    #print(key, sigma, n_over_sigma)


print('Done building sigma dict\n')

print(numbers[max(numbers)], '->', max(numbers))
    






'''
from math import sqrt, ceil
from pprint import pprint

def build_factors_dict(limit):
    limit += 1
    numbers = range(2, limit)
    factors = { key: set() for key in numbers }
    for x in numbers:
        for y in range(x, limit, x):
            factors[y].add(x)
    return factors

def test_coprime(n, m):
    print(n)
    """
    for x in range(2, m+1):
        if (not m % x) and (not n % x):
            return False
    return True
    """
    for x in factors[m]:
        if x in factors[n]:
            return False
    return True

def euler_69(limit):
    d = {}
    for n in range(2, limit+1):
        coprimes = [1]
        for m in range(2, n):
            if test_coprime(n, m):
                coprimes.append(m)
        d[n/len(coprimes)] = n
    print(d[max(d)], '->', max(d))


limit = 1000000
factors = build_factors_dict(limit)
#pprint(factors)

#print(test_coprime(10, 1))

euler_69(limit)

'''
