#!/usr/bin/env python3

'''
Digit cancelling fractions
Problem 33

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in 
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is 
correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than 
one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, 
find the value of the denominator.

'''

hits = []

for num in range(10, 100):
    for den in range(num+1, 100):
        frac = num/den
        s_num = str(num)
        s_den = str(den)
        for char in s_num:
            if char != '0':
                try:
                    new_num = int(s_num.replace(char, ''))
                    new_den = int(s_den.replace(char, ''))
                    if new_num / new_den == frac:
                        hits.append(((num, den), (new_num, new_den)))
                except (ValueError, ZeroDivisionError):
                    continue

a_num = 1
a_den = 1

for i in hits:
    print(i[0][0], '/', i[0][1], '=', i[1][0], '/', i[1][1])
    a_num *= i[1][0]
    a_den *= i[1][1]

print(a_num, '/', a_den)

# Simplify fractions!

for div in range(2, max(a_num, a_den)):
    if a_num % div == 0 and a_den % div == 0:
        a_num /= div
        a_den /= div

print(int(a_num), '/', int(a_den))
