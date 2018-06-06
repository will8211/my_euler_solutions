#!/usr/bin/csi -bq

#|
Coded triangle numbers
Problem 42

The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so 
the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its 
alphabetical position and adding these values we form a word value. For 
example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value 
is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file 
containing nearly two-thousand common English words, how many are triangle 
words?
|#

(use utils srfi-1 srfi-69)

(define alpha 
  (string->list "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

(define (letter->num char offset alpha)
  (cond
    ((eq? char (car alpha)) (add1 offset))
    (else (letter->num char (add1 offset) (cdr alpha)))))

(define words 
  (delete "," (string-split (read-all "p042_words.txt") "\"")))

(define (find-triangles start)
  (cond
    ((> start 700) '())
    (else (cons (inexact->exact (* (/ start 2) (+ start 1))) 
                (find-triangles (add1 start))))))

(define triangles 
  (find-triangles 1))

(define (triangular? n) 
  (member n triangles))

(define (calc-word l)
  (cond
    ((null? l) 0)
    (else (+ (letter->num (car l) 0 alpha) (calc-word (cdr l))))))

(define (e42 l)
  (cond
    ((null? l) (newline) 0)
    ((triangular? (calc-word (string->list (car l)))) 
     (print (car l) " " (calc-word (string->list (car l))))
     (add1 (e42 (cdr l))))
    (else (e42 (cdr l)))))

(print "Total words: " (e42 words))
