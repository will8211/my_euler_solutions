#!/usr/bin/env python3

'''
Non-abundant sums
Problem 23

A perfect number is a number for which the sum of its proper divisors is 
exactly equal to the number. For example, the sum of the proper divisors of 28 
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n 
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest 
number that can be written as the sum of two abundant numbers is 24. By 
mathematical analysis, it can be shown that all integers greater than 28123 can 
be written as the sum of two abundant numbers. However, this upper limit cannot 
be reduced any further by analysis even though it is known that the greatest 
number that cannot be expressed as the sum of two abundant numbers is less than 
this limit.

Find the sum of all the positive integers which cannot be written as the sum of 
two abundant numbers.
'''

from math import sqrt

# Make list of perfect numbers
perfects = []
for n in range(2, 28123):
    my_sum = 1
    root = (sqrt(n))
    for i in range(2, int(root)+1):
        if n % i == 0 and i != root:
            my_sum += i + n/i
    if root % 1 == 0:
            my_sum += root
    if my_sum > n:
        perfects.append(n)

# Make list for 1 to 28123
l = list(range(1, 28123))

# Round-robin add perfect numbers, cross sums off of list
for i in perfects:
    for j in perfects:
        my_sum = i+j
        if my_sum < 28123:
            l[my_sum-1] = 0
    perfects = perfects[1:]

# Add up remaining list numbers
print(sum(l))
