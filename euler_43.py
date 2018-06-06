#!/usr/bin/env python3

'''
Sub-string divisibility
Problem 43

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of 
each of the digits 0 to 9 in some order, but it also has a rather interesting 
sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note 
the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
'''

from itertools import permutations

my_dict = {17: []}

for p in permutations(range(10), 3):
    if not (p[0]*100 + p[1]*10 + p[2]) % 17:
        my_dict[17].append("%d%d%d" % (p[0], p[1], p[2]))

divisors = (17, 13, 11, 7, 5, 3, 2, 1)

for i, d in enumerate(divisors):
    if d != 17:
        my_dict[d] = []
        for s in my_dict[divisors[i-1]]:
            for digit in range(10):
                if str(digit) not in s:
                    new_string = str(digit)+s
                    if not int(new_string[:3]) % d:
                        my_dict[d].append(new_string)

print(sum([int(s) for s in my_dict[1]]))
