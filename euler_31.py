#!/usr/bin/env python3

'''
Coin sums
Problem 31

In England the currency is made up of pound, £, and pence, p, and there are 
eight coins in general circulation:
1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:
1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?

'''
def euler_30(coins, total):
    if total == 200 or coins[0] == 1:
        return 1
    if total < 200:
        hits = 0
        for i, c in enumerate(coins):
            hits += euler_30(coins[i:], total+c)
        return hits
    return 0

print(euler_30([200, 100, 50, 20, 10, 5, 2, 1], 0))
