#!/usr/bin/csi -bq

#|
Cubic permutations
Problem 62

The cube, 41063625 (345^3), can be permuted to produce two other cubes: 
56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube 
which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are 
cube.
|#

(use srfi-1)
(use srfi-69)
(define h (make-hash-table))

(define (e62 n)
  (let* ((cube (expt n 3))
         (s    (sort (string->list (number->string cube)) char<?)))
    (hash-table-set! h s (cons cube (hash-table-ref/default h s '())))  
    (cond
      ((eq? 5 (length (hash-table-ref h s))) 
       (print (last (hash-table-ref h s))))
      (else
       (e62 (add1 n))))))

(e62 345)

