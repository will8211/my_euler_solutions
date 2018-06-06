#!/usr/bin/csi -bq

#|
Digit fifth powers
Problem 30

Surprisingly there are only three numbers that can be written as the sum of 
fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers 
of their digits.
|#

(define (number->list n)
  (string->list (number->string n)))

(define (sum-powers l e)
  (cond
    ((null? l) 
     0)
    (else 
     (+ (expt (string->number (string (car l))) e) 
        (sum-powers (cdr l) e)))))

(define (euler30 n e)
  (cond
    ((eq? n 1) 
     0)
    ((eq? (sum-powers (number->list n) e) n) 
     (print n)
     (+ (sum-powers (number->list n) e)
        (euler30 (sub1 n) e)))
    (else
     (euler30 (sub1 n) e))))

(print "A: "(euler30 1000000 5))
