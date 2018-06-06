#!/usr/bin/js

/*
10001st prime
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
*/

function checkPrimeness(x) {
    for(i = 2; i <= Math.floor(Math.sqrt(x)); i++) {
        if (x % i === 0) {
            return false;
        }
    }
    return true;
}

var counter = 2;
var number = 3;

while (counter < 10001) {
    number += 2;
    if (checkPrimeness(number)) {
        counter += 1;
        //console.log(counter);
    }
}

console.log("Prime number #" + counter + " is " + number + "!")
