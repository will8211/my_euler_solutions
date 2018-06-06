#!/usr/bin/js

/*
Summation of primes
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
*/

function checkPrimeness(x) {
    for (var i = 2; i <= Math.floor(Math.sqrt(x)); i++) {
        if (x % i === 0) {
            return false;
        }
    }
    return true;
}

var mySum = 2;

for (var i = 3; i < 2000000; i = i+2) {
    if (checkPrimeness(i)) {
        mySum += i;
    }
}

console.log(mySum);
