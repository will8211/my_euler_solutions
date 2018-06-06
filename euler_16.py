#!/usr/bin/env python3

'''
Power digit sum
Problem 16

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''

n = str(2**1000)
my_sum = 0

for digit in n:
    my_sum += int(digit)

print(my_sum)
