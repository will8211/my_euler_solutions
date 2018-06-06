#!/usr/bin/env python3

'''
Coded triangle numbers
Problem 42

The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so 
the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its 
alphabetical position and adding these values we form a word value. For 
example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value 
is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file 
containing nearly two-thousand common English words, how many are triangle 
words?
'''

with open('p042_words.txt') as f:
    for line in f:
        words = line[1:-1].split('","')

alpha_dict = {}
for i, l in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    alpha_dict[l] = i+1

triangles = []
x = y = 1
while y < 700:
    y = int((x/2)*(x+1))
    triangles.append(y)
    x += 1

hits = 0
for w in words:
    my_sum = 0
    for l in w:
        my_sum += alpha_dict[l]
    if my_sum in triangles:
        print(w, my_sum)
        hits += 1

print('\nTotal words:', hits)
