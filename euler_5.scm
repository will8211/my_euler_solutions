#!/usr/bin/csi -bq

#|
Smallest multiple
Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
|#

;n -> number to check
;m -> multiple to jump by
;f -> factor to check

(define (e05 n m f)
  (cond
    ((> f 20)             n)
    ((zero? (modulo n f)) (e05 n n (add1 f)))
    (else                 (e05 (+ n m) m f))))

(display (e05 1 1 1))
