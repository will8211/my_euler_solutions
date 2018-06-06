#!/usr/bin/env python3

'''
Pandigital multiples
Problem 38

Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will 
call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 
5, giving the pandigital, 918273645, which is the concatenated product of 9 and 
(1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the 
concatenated product of an integer with (1,2, ... , n) where n > 1?

'''


#91..98 range(91, 99)
#9876...9182 range(9876, 9183)

hits = []
hits2 = []

def e_37(i):
    s = ''
    mult = 1
    value = True
    while len(s) < 9 and value:
        prod = str(i*mult)
        for d in prod:
            if d in s:
                value = False
                break
        if value:
            s += prod
        mult += 1
    if len(s) == 9:
        hits.append(s)

for i in range(91, 99):
    e_37(i)

for i in range(9182, 9877):
    e_37(i)

#for i in range(1, 10000):
#    e_37(i)

for i, h in enumerate(hits):
    value = True
    for j, d in enumerate(h):
        if d in h[j+1:] or '0' in h:
            value = False
            break
    if value == True:
        hits2.append(int(h))
        
print(sorted(hits2))
print(max(hits2))
