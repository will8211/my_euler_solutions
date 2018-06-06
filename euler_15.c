/*
Lattice paths
Problem 15

Starting in the top left corner of a 2×2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

    XXXXXXXXX    XXXXX---+    XXXXX---+
    |   |   X    |   X   |    |   X   |
    +---+---X    +---XXXXX    +---X---+
    |   |   X    |   |   X    |   X   |
    +---+---X    +---+---X    +---XXXXX

    X---+---+    X---+---+    X---+---+
    X   |   |    X   |   |    X   |   |
    XXXXXXXXX    XXXXX---+    X---+---+
    |   |   X    |   X   |    X   |   |
    +---+---X    +---XXXXX    XXXXXXXXX

How many such routes are there through a 20×20 grid?
*/

#include <stdio.h>

long a[21][21];

long compute(int x, int y)
{
    long x_paths = 0;
    long y_paths = 0;
    if (a[x][y] > 0)
        return a[x][y];
    if (x == 0)
        return 1;
    else
        x_paths = compute(x-1, y);
    if (y == 0)
        return 1;
    else
        y_paths = compute(y-1, x);
    long paths = x_paths + y_paths;
    a[x][y] = paths;
    return paths;
}

int main()
{
    for (int i = 1; i <= 20; i++)
        compute(i, i);

    for (int x = 1; x <= 20; x++)
        for (int y = 1; y <= 20; y++)
            if (a[x][y] > 0)
                printf(" '%02dx%02d': %li\n", x, y, a[x][y]);
    printf("%li\n", a[20][20]);
}
