#!/usr/bin/csi -bq

#|
Even Fibonacci numbers
Problem 2

Each new term in the Fibonacci sequence is generated by adding the previous 
two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.
|#

(define (e02 m n)
  (cond
    ((> n 4e6) 0)
    ((even? n) (+ n (e02 n (+ m n))))
    (else      (e02 n (+ m n)))))

(display (e02 1 1))
