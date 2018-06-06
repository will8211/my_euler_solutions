#!/usr/bin/js

/*
Power digit sum
Problem 16

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
*/
var bigInt = require("/usr/lib/node_modules/big-integer");

var n = bigInt(2).pow(1000)
var my_sum = 0;

//for digit in n:
//    my_sum += int(digit)

console.log(n)
