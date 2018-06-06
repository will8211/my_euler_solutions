#!/usr/bin/env python3

'''
Powerful digit sum
Problem 56

A googol (10^100) is a massive number: one followed by one-hundred zeros; 
100^100 is almost unimaginably large: one followed by two-hundred zeros. 
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the 
maximum digital sum?
'''

d = {}

for a in range(100):
    for b in range(100):
        my_sum = 0
        for dig in str(a**b):
            my_sum += int(dig)
        d[my_sum] = (a, b)

ans = d[max(d)]
print(ans[0], '^', ans[1], ' --> ', max(d), sep='')
