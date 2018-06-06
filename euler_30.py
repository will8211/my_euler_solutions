#!/usr/bin/env python3

'''
Digit fifth powers
Problem 30

Surprisingly there are only three numbers that can be written as the sum of 
fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers 
of their digits.

'''

expt = 5
limit = (9**expt)*6
hits = []
for i in range(2, limit):
    my_sum = 0
    for d in str(i):
        my_sum += int(d)**expt
    if my_sum == i:
        hits.append(i)
print(hits)
print(sum(hits))
    
