#!/usr/bin/csi -bq

#|
Champernowne's constant
Problem 40

An irrational decimal fraction is created by concatenating the positive 
integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the 
following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
|#


(define (num->list n)
  (string->list (number->string n)))
  
(define (char->num char)
  (string->number (string char)))

(define (hit? dig char tally)
  (cond
    ((eq? dig 10000000) #f)
    ((eq? tally dig) (print "d" dig " -> " char) #t)
    (else (hit? (* dig 10) char tally))))
  
(define (champer n to-add tally)
  (cond
    ((> tally 1000000) '())
    ((null? to-add) (champer (add1 n) (num->list n) tally))
    ((hit? 1 (car to-add) tally)
     (cons (char->num (car to-add)) (champer n (cdr to-add) (add1 tally))))
    (else (champer n (cdr to-add) (add1 tally)))))

(define answer-list (champer 0 '() 0))
(print answer-list)
(print (apply * answer-list))
