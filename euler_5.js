#!/usr/bin/js

/*
Smallest multiple
Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the 
numbers from 1 to 20?
*/

/*
for (n = 20;; n++) {
    var ok = true;
    for (f = 20; f > 0; f--) {
        if (n % f !== 0) {
            ok = false;
            break;
        }
    }
    if (ok === true) {
        console.log(n);
        break;
    }
}
*/

var n = 1 //number to check
var m = 1 //multiple to jump by
var f = 1 //factor to check

while (f <= 20) {
    if (n % f == 0) {
        f += 1;
        m = n;
    } else {
        n += m;
    }
}

console.log(n)
