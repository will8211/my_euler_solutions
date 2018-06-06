#!/usr/bin/csi -bq

#|
Largest palindrome product
Problem 4

A palindromic number reads the same both ways. The largest palindrome made 
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
|#

(define (pal? n)
  (define s (string->list (number->string n)))
  (equal? s (reverse s)))

(define (pals a b)
  (cond
    ((= b 900)      (pals (sub1 a) 999))
    ((= a 900)      '()) 
    ((pal? (* a b)) (cons (* a b) (pals a (sub1 b))))
    (else           (pals a (sub1 b)))))

(display (apply max (pals 999 999)))
