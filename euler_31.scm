#!/usr/bin/csi -bq

#|
Coin sums
Problem 31

In England the currency is made up of pound, £, and pence, p, and there are 
eight coins in general circulation:
1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:
1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
|#

(define (e30 l tot)
  (cond
    ((= 1 (car l)) 
     1)                         ;don't count pennies, just tally a hit
    ((> (+ tot (car l)) 200)
     (e30 (cdr l) tot))         ;if the car's too big, move on to smaller coins
    ((= (+ tot (car l)) 200) 
     (add1 (e30 (cdr l) tot)))  ;tally a hit, keep going with smaller coins
    (else 
     (+ (e30 l (+ tot (car l)))
        (e30 (cdr l) tot)))))   ;in under the count, keep adding same coins

(display (e30 '(200 100 50 20 10 5 2 1) 0))
