#!/usr/bin/js

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

// 21x21 2d array (column [0] and row [0] won't be used, just for convenience)
var a = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]];

// Returns number of paths for dimention x,y; also saves it to 2d array
function compute(x, y) {
    var x_paths = 0;
    var y_paths = 0;

    if (a[x][y] > 0) {
        return a[x][y];
    }

    if (x == 0) {
        return 1;
    } else {
        x_paths = compute(x-1, y);
    }

    if (y == 0) {
        return 1;
    } else {
        y_paths = compute(y-1, x);
    }

    var paths = x_paths + y_paths;
    a[x][y] = paths;

    return paths;
}

// Main loop: Call compute for each dimention
for (var i = 1; i <= 20; i++) {
    compute(i, i);
}

// Pritty print results
for (var x = 1; x <= 20; x++) {
    for (var y = 1; y <= 20; y++) {
        if (a[x][y] > 0) {
            console.log(" '%2x%d': %d", x, y, a[x][y]);
        }
    }
}
console.log("%d\n", a[20][20]);
