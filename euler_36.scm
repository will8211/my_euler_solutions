#!/usr/bin/csi -bq

#|
Double-base palindromes
Problem 36

The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in 
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include 
leading zeros.)
|#

(define (sum l)
  (cond
    ((null? l) 0)
    (else (+ (car l) (sum (cdr l))))))

(define (dec->bin n)
  (cond ((zero? n) '())
        (else (cons (remainder n 2) (dec->bin (quotient n 2))))))

(define (number->list n)
  (string->list (number->string n)))

(define (e36 n)
  (cond
    ((zero? n) '())
    ((equal? (number->list n) (reverse (number->list n)))
             (cond
               ((equal? (dec->bin n) (reverse (dec->bin n)))
                        (cons n (e36 (sub1 n))))
               (else (e36 (sub1 n)))))
    (else (e36 (sub1 n)))))

(define answer (e36 1000000)) 
(print answer)
(print (sum answer))
