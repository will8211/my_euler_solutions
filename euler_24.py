#!/usr/bin/env python3

'''
Lexicographic permutations
Problem 24

A permutation is an ordered arrangement of objects. For example, 3124 is one 
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations 
are listed numerically or alphabetically, we call it lexicographic order. The 
lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 
6, 7, 8 and 9?
'''

n = ''
l = list('0123456789')
counter = 0

def permutator(n, l):
    global counter
    if len(l) == 0:
        counter += 1
        if counter == 1000000:
            print(n)
            exit()
    else:
        for i, number in enumerate(l):
            n2 = n + number
            l2 = l[:i] + l[i+1:]
            permutator(n2, l2)

permutator(n, l)
    
