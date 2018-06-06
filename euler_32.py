#!/usr/bin/env python3

'''
Pandigital products
Problem 32

We shall say that an n-digit number is pandigital if it makes use of all the 
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 
through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing 
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can 
be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only 
include it once in your sum.

'''

digits = '123456789'
perm_set = set()
prod_set = set()
my_sum = 0

def make_set(s='', current=''):
    if len(s) == 5:
        perm_set.add(s)
        return
    for d in digits:
        if ((d not in s) and (current not in s)) or (current == ''):
            make_set(s + current, d)

make_set()
for i in perm_set:
    for n in 1, 2:
        p_int = int(i[:n])*int(i[n:])
        p = str(p_int)
        value = False
        if (len(p) == 4) and ('0' not in p):
            value = True
            for d in i:
                if d in p:
                    value = False
                    break
            for j in range(len(p)):
                if p[j] in p[j+1:]:
                    value = False
                    break
        if value == True:
            print(int(i[:n]), 'x', int(i[n:]), '=', p_int)
            prod_set.add(p_int)

for prod in prod_set:
    my_sum += int(prod)

print(prod_set)
print(my_sum)
