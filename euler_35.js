#!/usr/bin/js

/*
Circular primes
Problem 35

The number, 197, is called a circular prime because all rotations of the 
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 
73, 79, and 97.

How many circular primes are there below one million?
*/

primes = {}

function checkPrimeness(x) {
    if (x in primes) {
        return primes[x];
    }
    for (var i = 2; i < Math.floor(Math.sqrt(x))+1; i++) {
        if (x % i === 0) {
            primes[x] = false;
            return false;
        }
    }
    primes[x] = true;
    return true;
}

var hits = []

for (var i = 2; i < 1000000; i++) {
    if (checkPrimeness(i)) {
        var s = i.toString();
        var match = true;
        for (j = 1; j < s.length; j++) {
            var s2 = s.slice(j) + s.slice(0, j);
            if (checkPrimeness(Number(s2)) === false) {
                match = false;
                break;
            }
        }
        if (match === true) {
            hits.push(i);
        }
    }
}

console.log(hits)
console.log(hits.length)
