#!/usr/bin/csi -bq

#|
10001st prime
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see 
that the 6th prime is 13.

What is the 10001st prime number?
|#

(define (prime? n)
  (define m (abs n))
  (cond
    ((= m 2) 
     #t)
    ((< m 2) 
     #f)
    (else
     (define lim (add1 (floor (sqrt m))))
     (check-factors m 2 lim))))

(define (check-factors n f lim)
  (cond
    ((> f lim) 
     #t)
    ((zero? (modulo n f)) 
     #f)
    (else 
     (check-factors n (add1 f) lim))))

(define (e07 n pos)
  (if (prime? n) 
      (if (eq? 2 pos)
          ((print n) (exit)) ;This throws an error if I just return 2. WHY!??
          (e07 (+ n 2) (sub1 pos)))
      ((e07 (+ n 2) pos))))

(e07 3 10001)
