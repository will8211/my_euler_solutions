#!/usr/bin/env python3

'''
Concealed Square
Problem 206

Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.
'''

from math import sqrt

a = int(sqrt(1020304050607080900))
b = int(sqrt(1929394959697989990))


def determine_steps():
    previous = 0
    for i, n in enumerate(range(a, b)):
        sqr = n**2
        if 79999 < (sqr % 100000) < 90000 and sqr % 1000 > 899 and sqr % 10 == 0:
            #print(i, sqr)
            print(i-previous)
            previous = i
            input()

#determine_steps()

steps = [300, 100, 860, 100, 300, 840]
n = a+660
i = 0
while n <= b:
    sqr = n**2
    s = str(sqr)
    if s[2] == '2' and \
       s[4] == '3' and \
       s[6] == '4' and \
       s[8] == '5' and \
       s[10] == '6' and \
       s[12] == '7':
        print('%d^2 = %d' % (n, sqr))
        exit()
    n += steps[i%6]
    i += 1
