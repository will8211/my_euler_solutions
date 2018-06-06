#!/usr/bin/env python3

'''
Spiral primes
Problem 58

Starting with 1 and spiralling anticlockwise in the following way, a square 
spiral with side length 7 is formed.

[37] 36  35  34  33  32 [31]
 38 [17] 16  15  14 [13] 30
 39  18  [5]  4  [3] 12  29
 40  19   6   1   2  11  28
 41  20  [7]  8   9  10  27
 42  21  22  23  24  25  26
[43] 44  45  46  47  48  49

It is interesting to note that the odd squares lie along the bottom right 
diagonal, but what is more interesting is that 8 out of the 13 numbers lying 
along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral 
with side length 9 will be formed. If this process is continued, what is the 
side length of the square spiral for which the ratio of primes along both 
diagonals first falls below 10%?
'''

from primesieve import generate_primes

#primes = set(generate_primes(400000000))

def check(n):
    generate_primes(n, n)
    return d[n]

n = 1
i = 1
length = 1
solved = False
corners = [1]
prime_tally = 0
total_tally = 1

while not solved:
    for j in range(4):
        corner = n+(2*i)
        #print(corner)
        corners.append(corner)
        if generate_primes(corner, corner):
        #if corner in primes:
            prime_tally += 1
        total_tally += 1
        n += (2*i)
    length = (2*i)+1
    ratio = prime_tally/total_tally
    #print('Length:', length)
    #print(prime_tally, '/', total_tally, '=', ratio, '\n')
    if ratio < 0.1:
        solved = True
    i += 1

print('Length:', length)
print(prime_tally, '/', total_tally, '=', ratio, '\n')
    

'''

[5] 4 [3]
 6  1  2
[7] 8 [9]

2

 [17] 16  15  14 [13]
  18  [5]  4  [3] 12 
  19   6   1   2  11 
  20  [7]  8   9  10 
  21  22  23  24  25 

4

[37] 36  35  34  33  32 [31]
 38 [17] 16  15  14 [13] 30
 39  18  [5]  4  [3] 12  29
 40  19   6   1   2  11  28
 41  20  [7]  8   9  10  27
 42  21  22  23  24  25  26
[43] 44  45  46  47  48  49

6

'''
