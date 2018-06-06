#!/usr/bin/csi -bq

#|
Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
|#

;;;Why does this work???

(define (pfactor x i)
  (print "Now running on " i " for " x)
  (cond
    ((eq? i x) 
     (print i " == " x) #f)
    ((zero? (modulo x i)) 
     (define factor (quotient x i))
     (if (pfactor factor 2)
         (print "The answer is " factor "!") 
         #f))
    (else 
     (pfactor x (add1 i)))))


(pfactor 600851475143 2)
;(pfactor 13195 2)

