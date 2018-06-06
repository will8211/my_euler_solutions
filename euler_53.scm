#!/usr/bin/csi -bq

#|
Combinatoric selections
Problem 53

There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,

nCr = n!/r!(n−r)! ,where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.

It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are
greater than one-million?
|#

(define (factorial n)
    (if (zero? n) 1
        (* n (factorial (- n 1)))))

(define (e53 n r)
  (cond
    ((zero? n) 0)
    ((zero? r) (e53 (sub1 n) (- n 2)))
    ((> (calc-combos n r) 1000000)
     (add1 (e53 n (sub1 r))))
    (else (e53 n (sub1 r)))))

(define (calc-combos n r)
  (/ (factorial n)
     (* (factorial r) (factorial (- n r)))))

(print (e53 100 99))
