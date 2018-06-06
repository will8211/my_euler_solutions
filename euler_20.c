/*
Factorial digit sum
Problem 20

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
*/

#include <stdio.h>
#include <string.h>
#include <gmp.h>

int main() {

    mpz_t factorial;
    mpz_init_set_str(factorial, "1", 10);
    for (int n = 100; n > 0; n--)
        mpz_mul_ui(factorial, factorial, n);

    char str[200];
    gmp_sprintf(str, "%Zd", factorial);
    int answer = 0;
    for (int i = 0; i < strlen(str); i++)
        answer += str[i]-48;

    printf("%d\n", answer);
}
