#!/usr/bin/csi -bq

#|
Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
|#

(define (prime? x i)
  (cond
    ((eq? i x) 
     #t)
    ((zero? (modulo x i)) 
     (print "Factor " x " is not prime") #f)
    (else 
     (prime? x (add1 i)))))

(define (pfactor x i)
  (cond
    ((eq? i x) 
     #f)
    ((zero? (modulo x i)) 
     (define factor (quotient x i))
     (cond 
       ((prime? factor 2) 
        (print "The answer is " factor "!") 
        #t)
       (else 
        (pfactor x (add1 i)))))
    (else 
     (pfactor x (add1 i)))))

(pfactor 600851475143 2)


