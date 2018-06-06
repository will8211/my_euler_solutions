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

to_check = [x for x in range(2, 20) if sqrt(x) % 1]

x = 2
D = 2
working = True
while working:
    y = 1
    while 1 < D <= 20:
        print(x, y)
        D = (x**2-1)/y**2
        print('D', D)
        #-(D*y**2) = x**2 + 1 
        #x**2 – D*y**2 = 1
        if D in to_check:
            to_check.remove(D)
            print(x)
        y += 1
        input()
    if not len(to_check):
        working = False
    x += 1














y = 2
high = 0
searching = True
to_go = 'many'

while to_go:
    done = []
    for D in to_check:
        x = sqrt(y**2*D + 1)
        while not x.is_integer():
            x+=x
        if True: #x.is_integer():
            done.append(D)
            if x > high:
                print('D:', D, 'x:', x, 'y:', y)
                print('~', to_go, 'to go')
                high = x
    for n in done:
        to_check.remove(n)
    y += 1
    if not y % 100:
        to_go = len(to_check)

'''
D: 698 x: 51999603
'''
