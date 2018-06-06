#!/usr/bin/js

/*
Special Pythagorean triplet
Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

    a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
*/

for (a = 1; a < 1000; a++) {
    for (b = a+1; b < 1000; b++) {
        c = 1000 - (a+b);
        if (a*a + b*b == c*c) {
            console.log(a +"^2 +", b + "^2 =", c + "^2");
            console.log(a*b*c);
            process.exit()
        }
    }
}
