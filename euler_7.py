#!/usr/bin/env python3

'''
10001st prime
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
'''

from math import sqrt

def check_primeness(x):
    for i in range(2, int(sqrt(x))+1):
        if (x % i == 0):
            return False
    return True

counter = 2
number = 3

while counter < 10001:
    number += 2
    if check_primeness(number):
        counter += 1
        #print(counter)

print("Prime number #%d is %d!" % (counter, number))
