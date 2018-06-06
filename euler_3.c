/*
Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
*/

#include <stdio.h>

int checkPrimeness(long x)
{
    for (long i = 2; i < x; i++) {
        if (x % i == 0){
            printf("Factor %ld is not prime\n", x);
            return 0;
        }
    }
    return 1;
}

int main()
{
    long n = 600851475143;

    for (long i = 2; i < n; i++) {
        //printf("%d\n", i);
        if (n % i == 0) {
            long factor = n/i;
            if (checkPrimeness(factor)) {
                printf("The answer is %ld!\n", factor);
                break;
            }
        }
    }
}
