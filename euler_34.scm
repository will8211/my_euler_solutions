#!/usr/bin/csi -bq

#|
Digit factorials
Problem 34

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of 
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
|#

(define (factorial n)
  (cond
    ((zero? n) 1)
    (else (* n (factorial (sub1 n))))))

(define (number->list n)
  (string->list (number->string n)))

(define (fact-sum l)
  (cond
    ((null? l) 0)
    (else (+ (factorial (string->number (string (car l)))) 
             (fact-sum (cdr l))))))

(define (e34 n)
  (cond
    ((eq? n 3) 0)
    ((eq? n (fact-sum (number->list n))) 
     (print n)
     (+ n (e34 (sub1 n))))
    (else (e34 (sub1 n)))))

(print "= " (e34 100000))

