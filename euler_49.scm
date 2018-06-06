#!/usr/bin/csi -bq

#|
Prime permutations
Problem 49

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms 
increases by 3330, is unusual in two ways: (i) each of the three terms are 
prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, 
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this 
sequence?
|#

(define (prime? n)
  (let ((a (abs n)))
    (cond
      ((or (= a 0) (= a 1)) #f)
      (else (factor? a 2)))))

(define (factor? n m)
  (cond
    ((> m (floor (sqrt n))) #t)
    ((zero? (modulo n m)) #f)
    (else (factor? n (add1 m)))))

(define (list-primes first last)
  (cond
    ((> first last) '())
    ((prime? first) (cons first (list-primes (add1 first) last)))
    (else (list-primes (add1 first) last))))

(define numbers
  (list-primes 1488 9999))

(define (list-candidates n numbers)
  (let ((3rd (- (* 2 (car numbers)) n)))
    (cond
      ((null? (cdr numbers)) '())
      ((member 3rd numbers) 
       (cons `(,(string->list (number->string n)) 
               ,(string->list (number->string (car numbers))) 
               ,(string->list (number->string 3rd)))
             (list-candidates n (cdr numbers))))
      (else (list-candidates n (cdr numbers))))))

(define candidates 
  (list-candidates 1487 numbers))

(define (vet-candidates l)
  ;(print (car l))
  ;(print (caaar l))
  ;(print (cddr (car l)))
  (cond 
    ((and (member (caaar l) (cdr (car l)))
          (member (caaar l) (cddr (car l))))
     (car l))
    (else (vet-candidates (cdr l)))))


;;;NOT DONE!

(print candidates)
(print (vet-candidates candidates))
