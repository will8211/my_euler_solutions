#!/usr/bin/js

/*
Distinct primes factors
Problem 47

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors. 
What is the first of these numbers?
*/

var primesL = []

function checkPrimeness(x) {
    x = Math.abs(x);
    root = Math.floor(Math.sqrt(x));
    for (var i = 2; i < root+1; i++) {
        if (x % i === 0) {
            return false;
        }
    }
    primesL.push(x)
    return true;
}

var targetRun = 4;
var upperBound = 10000000;
var run = 0
var checkPrimes = true

for (var n = 2; n < upperBound; n++) {
    hits = 0;
    if (n % 10000 === 0) {
        console.log('\nn:', n);
    }
    for (var i in primesL) {
        var p = primesL[i];
        if (n % p === 0) {
            hits++;
        }
    }
    if (hits >= targetRun) {
        run++;
    } else {
        run = 0;
    }
    if (run === targetRun) {
        console.log('Answer:', n-targetRun+1)
        break;
    }
    if (checkPrimes === true) {
        checkPrimeness(n);
    }
    if (primesL.length > 1000) {
        checkPrimes = false;
    }
}
