#!/usr/bin/js

/*
Even Fibonacci numbers
Problem 2

Each new term in the Fibonacci sequence is generated by adding the previous 
two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed 
four million, find the sum of the even-valued terms.
*/

var my_sum = 0;
var a = 0; //before last fib no
var b = 1; //last fib no
var c = 1; //current fib no

while (c <= 4000000) {
    if (c % 2 === 0) {
        my_sum += c;
    }
    c = a + b;
    a = b;
    b = c;
}

console.log(my_sum);

