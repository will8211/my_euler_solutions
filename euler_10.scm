#!/usr/bin/csi -bq

#|
Summation of primes
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
|#


(load "./primes.scm")

(define primes (prime-sieve 2000000))

(define (e10 lst)
  (cond
    ((null? lst) 0)
    ((+ (car lst) (e10 (cdr lst))))))

(display (e10 primes))
