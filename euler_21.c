/*
Amicable numbers
Problem 21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n).

If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71
and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
*/

#include <stdio.h>
#include <math.h>

int main() {

    int dict[10000] = {0};
    int answer = 0;

    for (int n = 2; n < 10000; n++) {
        int sum = 1;
        float root = sqrt(n);
        int intRoot = (int)root;
        for (int i = 2; i < intRoot-1; i++) {
            if (n % i == 0)
                sum += i + n/i;
        }
        if (intRoot == root)
            sum += intRoot;
        dict[n] = sum;
    }

    for (int i = 0; i < 10000; i++) {
        int val = dict[i];
        if ((0 < val && val < 10000) && (val != i) && (dict[val] == i)) {
            answer += val;
            printf("%d is amicable to %d\n", val, dict[val]);
        }
    }
    printf("%d\n", answer);
}
