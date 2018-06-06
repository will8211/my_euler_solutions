#!/usr/bin/env python3

'''
Champernowne's constant
Problem 40

An irrational decimal fraction is created by concatenating the positive 
integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the 
following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
'''

#terse:

s,n,p,d,l='',0,1,1,1000000
while len(s)<=l:s+=str(n);n+=1
while d<=l:p*=int(s[d]);d*=10
print(p)

#pretty:

s = ''
n = 0
p = 1
d = 1
l = 1000000

while len(s) <= l: 
    s += str(n)
    n += 1

while d <= l:
    p *= int(s[d])
    d *= 10

print(p)
