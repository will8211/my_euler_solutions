#!/usr/bin/env python3

'''
Diophantine equation
Problem 66

Consider quadratic Diophantine equations of the form:

    x^2 – Dy^2 = 1

For example, when D=13, the minimal solution in x is 649^2 – 13×180^2 = 1.

It can be assumed that there are no solutions in positive integers when D is 
square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the 
following:

    3^2 – 2×2^2 = 1
    2^2 – 3×1^2 = 1
    9^2 – 5×4^2 = 1
    5^2 – 6×2^2 = 1
    8^2 – 7×3^2 = 1

Hence, by considering minimal solutions in x for D ≤ 7, the largest x is 
obtained when D=5.

Find the value of D ≤ 1000 in minimal solutions of x for which the largest 
value of x is obtained.
'''

from math import sqrt

to_check = [x for x in range(2, 1001) if sqrt(x) % 1]

'''
x = sqrt(y**2*D + 1)
y = sqrt((x**2-1)/D)
D = (x**2-1)/y**2
D: 698 x:    51999603
'''

d = {}

y = 2
searching = True
while searching:
    done = []
    for D in to_check:
        x = sqrt(y**2*D + 1)
        if not x % 1: 
            d[int(x)] = D
            done.append(D)
    for n in done:
        to_check.remove(n)
    y += 1
    if not y % 10:
        print('D:', d[max(d)], '( x =', max(d),')')
        print(len(to_check))

'''
D: 991 x: 775587755
~ 67 to go
'''
