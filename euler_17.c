/*
Number letter counts
Problem 17

If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?

Note: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with
British usage.
*/

#include <stdio.h>

int letterCounter(int n)
{
    int ones[10];
    ones[1] = 3; //one
    ones[2] = 3; //two
    ones[3] = 5; //three
    ones[4] = 4; //four
    ones[5] = 4; //five
    ones[6] = 3; //six
    ones[7] = 5; //seven
    ones[8] = 5; //eight
    ones[9] = 4; //nine

    int teens[10];
    teens[0] = 3; //ten
    teens[1] = 6; //eleven
    teens[2] = 6; //twelve
    teens[3] = 8; //thirteen
    teens[4] = 8; //fourteen
    teens[5] = 7; //fifteen
    teens[6] = 7; //sixteen
    teens[7] = 9; //seventeen
    teens[8] = 8; //eighteen
    teens[9] = 8; //nineteen

    int tens[10];
    tens[2] = 6; //twenty
    tens[3] = 6; //thirty
    tens[4] = 5; //forty
    tens[5] = 5; //fifty
    tens[6] = 5; //sixty
    tens[7] = 7; //seventy
    tens[8] = 6; //eighty
    tens[9] = 6; //ninety

    int total = 0;
    if (n == 1000) {
        total += 11; //onethousand
        return total;
    }
    if (n >= 100) {
        total += ones[n / 100];
        total += 7; //hundred
        if (n % 100 == 0)
            return total;
        total += 3; //and
    }
    int m = n % 100;
    if (m >= 20) {
        total += tens[m / 10];
        if (m % 10 == 0)
            return total;
    } else if (m >= 10) {
        total += teens[m - 10];
        return total;
    }
    int o = n % 10;
    total += ones[o];
    return total;
}

int main()
{
    int sum = 0;
    for (int i = 1; i < 1001; i++)
        sum += letterCounter(i);
    printf("%d\n", sum);
}
