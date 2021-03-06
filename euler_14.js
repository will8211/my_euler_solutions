#!/usr/bin/js

/*
Longest Collatz sequence
Problem 14

The following iterative sequence is defined for the set of positive integers:

    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
*/


function collatz(n) {
    if (n == 1) {
        return 1;
    } else if (a[n] > 0) {      //answer is already in array
        return a[n];
    } else if (n % 2 == 0) {    //calculate even
        return 1+collatz(n/2);
    } else {                    //calculate odd
        return 1+collatz(3*n+1);
    }
}

var a = []; //array to save results for each starting number
var ans;
var len = 0;

for (var n = 2; n < 1e6; n++) {
    a[n] = collatz(n);
    if (a[n] > len) {
        len = a[n];
        ans = n;
    }
}

console.log(ans);
