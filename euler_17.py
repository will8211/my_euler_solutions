#!/usr/bin/env python3

'''
Number letter counts
Problem 17

If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with
British usage.
'''

ones = [None, 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
        'nine']

teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
        'sixteen', 'seventeen', 'eighteen', 'nineteen']

tens = [None, None, 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
        'eighty', 'ninety']

def speller(n):
    word = ''
    if n == 1000:
        word = word + 'onethousand'
        return word
    if n >= 100:
        word = word + ones[int(n/100)] + 'hundred'
        if n%100 == 0:
            return word
        word = word + 'and'
    m = n%100
    if m >= 20:
        word = word + tens[int(m/10)]
        if m%10 == 0:
            return word
    elif m >= 10:
        word = word + teens[m-10]
        return word
    o = n%10
    word = word + ones[o]
    return word

my_sum = 0

for i in range(1, 1001):
    my_sum += len(speller(i))

print(my_sum)
