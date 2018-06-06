#!/usr/bin/env python3

'''
Reciprocal cycles
Problem 26

A unit fraction contains 1 in the numerator. The decimal representation of the 
unit fractions with denominators 2 to 10 are given:

1/2 =   0.5
1/3 =   0.(3)
1/4 =   0.25
1/5 =   0.2
1/6 =   0.1(6)
1/7 =   0.(142857)
1/8 =   0.125
1/9 =   0.(1)
1/10 =  0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be 
seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle 
in its decimal fraction part.
'''

from decimal import Decimal, getcontext
getcontext().prec = 8000

# Build list of decimal strings
l = []
for denominator in range(2, 1000):
    n = str(1 / Decimal(denominator))
    l.append(n[12:]) #Throwing out short strings and non-recurring beginnings

# Build dictionary of denominator and the length of their recurring cycle
d = {}
for i, n in enumerate(l):
    if n != '':
        for rep in range(1, 2400):
            if int(n[0:rep]) == int(n[rep:rep*2]) == int(n[rep*2:rep*3]):
                d[i+2] = rep #l[0] being data about number 2
                break

# Find longest recurring cycle
winner = max(d, key=d.get)
print('The winner is number %d with a recurring cycle of %d digits!' 
      % (winner, d[winner]))
