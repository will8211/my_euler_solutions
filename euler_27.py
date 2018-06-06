#!/usr/bin/env python3

'''
Quadratic primes
Problem 27

Euler discovered the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values 
n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible 
by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

The incredible formula  n² − 79n + 1601 was discovered, which produces 80 
primes for the consecutive values n = 0 to 79. The product of the coefficients, 
−79 and 1601, is −126479.

Considering quadratics of the form:

    n² + an + b, where |a| < 1000 and |b| < 1000

    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |−4| = 4

Find the product of the coefficients, a and b, for the quadratic expression 
that produces the maximum number of primes for consecutive values of n, 
starting with n = 0.
'''

from math import sqrt

# Prime checking

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

# When n is 0, b must be prime for the total to be a prime

b_primes = []
for b in range(2, 1000):
    if check_primeness(b):
        b_primes.append(b)

# Make a dictionary. Key: (a, b), Value: length of prime sequence

d = {}
for a in range(-999, 1000):
    for b in b_primes:
        prime = True
        n = 0
        while prime:
            if check_primeness(n**2 + a*n + b):
                n += 1
            else:
                prime = False
                d[(a, b)] = n

# Find the longest sequence

answer = max(d, key=d.get)
print('a = %d and b = %d with %d primes.' % (answer[0], answer[1], d[answer]))
print("Answer: %d" % (answer[0]*answer[1]))
