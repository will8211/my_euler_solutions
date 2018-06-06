#!/usr/bin/env python3 

'''
Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

n = 600851475143

def check_primeness(x):
    for i in range(2, x):
        if (x % i == 0):
            print("Factor %d is not prime" % x)
            return False
    return True

for i in range(2, n):
    if (n % i == 0):
        factor = int(n/i)
        if check_primeness(factor):
            print("The answer is %d!" % factor)
            exit()


