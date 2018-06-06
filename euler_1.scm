#!/usr/bin/csi -bq

; Multiples of 3 and 5
; Problem 1
;
; If we list all the natural numbers below 10 that are multiples of 3 or 5, we
; get 3, 5, 6 and 9. The sum of these multiples is 23.
;
; Find the sum of all the multiples of 3 or 5 below 1000.


(define (e01 n)
  (cond
    ((zero? n)
     0)
    ((or (zero? (modulo n 3))
         (zero? (modulo n 5)))
     (+ n (e01 (sub1 n))))
    (else
     (e01 (sub1 n)))))

(display (e01 999))
