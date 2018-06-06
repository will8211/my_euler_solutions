#!/usr/bin/env python3
#
# Debugging for Project Euler Problem 17
#

ones = [None, 'one ', 'two ', 'three ', 'four ', 'five ', 'six ', 'seven ', 
        'eight ', 'nine']

teens = ['ten ', 'eleven ', 'twelve ', 'thirteen ', 'fourteen ', 'fifteen ', 
        'sixteen ', 'seventeen ', 'eighteen ', 'nineteen ']

tens = [None, None, 'twenty ', 'thirty ', 'forty ', 'fifty ', 'sixty ', 
        'seventy ', 'eighty ', 'ninety ']

def speller(n):
    word = ''
    if n == 1000:
        word = word + 'one thousand '
        return word
    if n >= 100:
        word = word + ones[int(n/100)] + 'hundred '
        if n%100 == 0:
            return word
        word = word + 'and '
    m = n%100
    if m >= 20:
        word = word + tens[int(m/10)]
        if m%10 == 0:
            return word
        else:
            word = word[0:-1] + '-'
    elif m >= 10:
        word = word + teens[m-10]
        return word
    o = n%10
    word = word + ones[o]
    return word

for i in range(1, 1001):
    print(speller(i))

