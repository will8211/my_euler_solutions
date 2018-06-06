#!/usr/bin/js

/*
Largest palindrome product
Problem 4

A palindromic number reads the same both ways. The largest palindrome made 
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
*/

var l = [];

for (var i = 999; i >= 900; i--) {
    for (var j = 999; j >= 900; j--) {
        var n = i*j;
        var s = String(n);
        if (s === s.split("").reverse().join("")) {
            l.push(n);
        }
    }
}

console.log(Math.max.apply(0, l));
