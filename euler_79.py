#!/usr/bin/env python3

'''
Passcode derivation
Problem 79

A common security method used for online banking is to ask the user for three 
random characters from a passcode. For example, if the passcode was 531278, 
they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 
317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the 
file so as to determine the shortest possible secret passcode of unknown 
length.
'''

keys = []
with open("p079_keylog.txt") as f:
    for line in f:
        keys.append(line[:-1])

d = {}
for n in range(10):
    d[str(n)] = set(), set()

for k in keys:
    d[k[0]][1].add(k[1])
    d[k[0]][1].add(k[2])
    d[k[1]][0].add(k[0])
    d[k[1]][1].add(k[2])
    d[k[2]][0].add(k[0])
    d[k[2]][0].add(k[1])

l = []
for k in d:
    if len(d[k][0]) or len(d[k][1]):
        l.append((len(d[k][0]), k))

s = ''
for t in sorted(l):
    s += t[1]

print(s)
