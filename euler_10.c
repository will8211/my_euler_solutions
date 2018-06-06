/*
Summation of primes
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
*/

#include <stdio.h>
#include <math.h>

long checkPrimeness(long x)
{
    for (long i = 2; i <= floor(sqrt(x)); i++) {
        if (x % i == 0) {
            return 0;
        }
    }
    return 1;
}

int main()
{
    long mySum = 2;

    for (long i = 3; i < 2000000; i = i+2) {
        if (checkPrimeness(i)) {
            mySum += i;
        }
    }
    printf("%li\n", mySum);
}
