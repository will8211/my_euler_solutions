/*
Largest palindrome product
Problem 4

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
*/

#include <stdio.h>

int main()
{
    int answer = 0;

    for (int i = 999; i >= 900; i--) {
        for (int j = 999; j >= 900; j--) {
            int n = i*j;
            if (n/100000 == n%10) {
                if (n%100000/10000 == n%100/10) {
                    if (n%10000/1000 == n%1000/100) {
                        if (n > answer) {
                            answer = n;
                        }
                    }
                }
            }
        }
    }

    printf("%d\n", answer);
}
