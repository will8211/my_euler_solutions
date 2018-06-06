#!/usr/bin/js

/*
Permuted multiples
Problem 52

It can be seen that the number, 125874, and its double, 251748, contain
exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits.
*/

function check(n, m) {
    var str1 = n.toString();
    var str2 = (n * m).toString();
    for (var i = 0, len = str1.length; i < len; i++) {
        if (str2.indexOf(str1[i]) === -1) {
            return false;
        }
    }
    for (var i = 0, len = str2.length; i < len; i++) {
        if (str1.indexOf(str2[i]) === -1) {
            return false;
        }
    }
    return true;
}

var done = false;
for (var i = 1; done === false; i++) {
    for (m = 2; m <= 6; m++) {
        var done = true;
        if (check(i, m) === false) {
            var done = false;
            break;
        }
    }
}

console.log("It's", i, "!");
