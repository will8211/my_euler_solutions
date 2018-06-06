/*
Power digit sum
Problem 16

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
*/

#include <stdio.h>
#include <math.h>

int main()
{
    double n = pow(2, 1000);
    int len = floor(log10(fabs(n))) + 1; // number of digits in x

    char str[len];
    sprintf(str, "%.0f", n);

    int sum = 0;
    for (int i = 0; i < len; i++) {
        sum += str[i]-48;
    }
    printf("%d\n", sum);
}
