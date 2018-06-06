#!/usr/bin/csi -bq

#|
Sum square difference
Problem 6

The sum of the squares of the first ten natural numbers is,

    1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

    (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural 
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred 
natural numbers and the square of the sum.
|#

(define (sum-of-sqrs n)
  (if (zero? n)
      0
      (+ (expt n 2)
         (sum-of-sqrs (sub1 n)))))

(define (sum n)
  (if (zero? n)
      0
      (+ n (sum (sub1 n)))))

(display (- (expt (sum 100) 2)
            (sum-of-sqrs 100)))
