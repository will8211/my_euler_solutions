#!/usr/bin/js

/*
Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
*/

var n = 600851475143;

function check_primeness(x) {
    for (var i = 2; i < x; i++) {
        if (x % i === 0) {
            console.log("Factor", x, "is not prime");
            return false;
        }
    }
    return true;
}

for (var i = 2; i < n; i++) {
    if (n % i === 0) {
        var factor = Math.floor(n/i);
        if (check_primeness(factor)) {
            console.log("The answer is", factor + "!");
            break;
        }
    }
}


