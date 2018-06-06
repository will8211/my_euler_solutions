#!/usr/bin/csi -bq

#|
Pandigital products
Problem 32

We shall say that an n-digit number is pandigital if it makes use of all the 
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 
through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing 
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can 
be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only 
include it once in your sum.
|#

(use combinatorics)

(define (conc-nums lst)
  (string->number (apply conc lst)))

(define *products* '())

(define (1x4 lst)
  (let ((a (* (car lst)))
        (b (conc-nums (cdr lst))))
    (check-pandig a b)))

(define (2x3 lst)
  (let ((a (conc-nums `(,(car lst) ,(cadr lst)))) 
        (b (conc-nums (cddr lst))))
    (check-pandig a b)))
                  
(define (check-pandig a b)
  (define prod (* a b))
  (define full-equasion (conc (conc-nums `(,a ,b)) prod))
  (cond
    ((and (< prod 10000)
          (not (member #\0 (string->list (number->string prod))))
          (equal? (string->list full-equasion)
                  (delete-duplicates (string->list full-equasion))))
     (print a " x " b " = " prod)
     prod)
    (else 
     0)))

(define (add-prods lst)
  (set! *products* (cons (1x4 lst) *products*))
  (set! *products* (cons (2x3 lst) *products*)))
  
(ordered-subset-for-each add-prods '(1 2 3 4 5 6 7 8 9) 5)
(print "\nAnswer -> " (apply + (delete-duplicates *products*)))
