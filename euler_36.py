#!/usr/bin/env python3

'''
Double-base palindromes
Problem 36

The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in 
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include 
leading zeros.)

'''

hits = []

for i in range(1, 1000000):
    d = str(i)
    d_rev = ''.join([x for x in reversed(d)])
    if d == d_rev:
        b = str(bin(i))[2:]
        b_rev = ''.join([x for x in reversed(b)])
        if b == b_rev:
            hits.append(i)

print(hits)
print(sum(hits))
