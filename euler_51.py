#!/usr/bin/env python3

'''
Prime digit replacements
Problem 51

By replacing the 1st digit of the 2-digit number *3, it turns out that six of 
the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit 
number is the first example having seven primes among the ten generated 
numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 
56993. Consequently 56003, being the first member of this family, is the 
smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not 
necessarily adjacent digits) with the same digit, is part of an eight prime 
value family.
'''

from primesieve import generate_primes

primes = []
bin_mask = 1
limit = 1
quota = 8

def find_first(s):
    prime_set = set(primes)
    for n in range(10):
        to_check = s.replace('*', str(n))
        if int(to_check) in prime_set:
            print("It's", to_check)
            exit()

while True:
    print('Checking up to', limit*10)
    primes = generate_primes(limit, limit*10)
    for i in range(1, bin_mask*2-1):
        hits = {}
        mask = str("{0:b}".format(i)).zfill(len(str(limit)))
        for p in primes:
            s = ''
            digit = None
            for i, d in enumerate(str(p)):
                fail = False
                if mask[i] == '1':
                    if d == digit or digit == None:
                        s += '*'
                        digit = d
                    else:
                        fail = True
                        break
                else:
                    s += d
            if not fail:
                try:
                    hits[s] += 1
                except KeyError:
                    hits[s] = 1
                if hits[s] == quota:
                    find_first(s)
    bin_mask *= 2
    limit *= 10
