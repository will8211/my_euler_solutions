#!/bin/bash
#
# Runs command in $1 and times how long it took
#

x=$(date +%s.%N)
./$1
y=$(date +%s.%N)
z=$(echo "$y - $x" | bc)
echo "TIME: $z seconds"

