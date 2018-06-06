#!/usr/bin/env python3

'''
Square digit chains
Problem 92

A number chain is created by continuously adding the square of the digits in a 
number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless 
loop. What is most amazing is that EVERY starting number will eventually arrive 
at 1 or 89.

How many starting numbers below ten million will arrive at 89?
'''

tally = 0
d = {(1,): False, (8, 9,): True}

for i in range(1, 10000000):
    if not i % 250000:
        print(i/1000000, 'Million')
    sq_sum = i
    seen = []
    while sq_sum not in (1, 89):
        #print(sq_sum)
        t = tuple(map(int, sorted(str(sq_sum))))
        try:
            if d[t]:
                sq_sum = 89
            else:
                sq_sum = 1
            break
        except KeyError:
            seen.append(t)
        #print('summing...')
        #input()
        sq_sum = sum([int(d)**2 for d in str(sq_sum)])
    if sq_sum == 89:
        #print('TRUE')
        tally += 1
        for t in seen:
            d[t] = True
    else:
        #print('FALSE')
        for t in seen:
            d[t] = False

print(tally)
