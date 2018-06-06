/*
10001st prime
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
*/

#include <stdio.h>
#include <math.h>

int checkPrimeness(int x)
{
    for(int i = 2; i <= floor(sqrt(x)); i++) {
        if (x % i == 0) {
            return 0;
        }
    }

    return 1;
}

int main()
{
    int counter = 2;
    int number = 3;

    while (counter < 10001) {
        number += 2;
        if (checkPrimeness(number)) {
            counter += 1;
            //printf("%d\n", counter);
        }
    }

    printf("Prime number #%d is %d!\n", counter, number);
}
