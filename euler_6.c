/*
Sum square difference
Problem 6

The sum of the squares of the first ten natural numbers is,

    1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

    (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
*/

#include <stdio.h>
#include <math.h>

int main()
{
    int sum1 = 0;
    int sum2 = 0;

    for (int i = 1; i < 101; i++) {
        sum1 += pow(i, 2);
        sum2 += i;
    }

    sum2 = pow(sum2, 2);

    int n = sum2 - sum1;
    printf("%d\n", n);
}
