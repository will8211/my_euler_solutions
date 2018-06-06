#!/usr/bin/env python3

'''
Consecutive prime sum
Problem 50

The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below 
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, 
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most 
consecutive primes?
'''

from primesieve import generate_primes

limit = 1000000
primes = generate_primes(limit)
primes_set = set(primes)
best = 0

for i, n in enumerate(primes):
    current = n
    my_sum = n
    count = 1
    while my_sum <= limit:
        my_sum += primes[i+count]
        count += 1
        if count > best and my_sum in primes_set:
            best_prime = my_sum
            best = count
    if count < best:
        break

print(best_prime, '-->', best)
