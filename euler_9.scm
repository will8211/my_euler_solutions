#!/usr/bin/csi -bq

#|
Special Pythagorean triplet
Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

    a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
|#

(define (e09 a b)
  (let ((c (- 1000 (+ a b))))
    (cond
      ((= (* c c) 
          (+ (* a a) 
             (* b b))) 
       (print a "^2 x " b "^2 = " c "^2")
       (* a b c))
      ((= 1 b) 
       (e09 (sub1 a) 999))
      (else 
       (e09 a (sub1 b))))))

(print (e09 999 999))

