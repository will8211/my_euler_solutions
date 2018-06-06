#!/usr/bin/env python3

'''
Amicable numbers
Problem 21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n).

If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71
and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

from math import sqrt

my_dict = {}
amicables = []

for n in range(2, 10000):
    my_sum = 1
    root = (sqrt(n))
    for i in range(2, int(root)-1):
        if n % i == 0:
            my_sum += i + n/i
    if root % 1 == 0:
        my_sum += root
    if my_sum > 1:
        my_dict[n] = int(my_sum)

for k, v in my_dict.items():
    if (v != k) and (v in my_dict.keys()) and (my_dict[v] == k):
        amicables.append(v)
        print('%d is amicable to %d' % (v, my_dict[v]))

print(sum(amicables))
