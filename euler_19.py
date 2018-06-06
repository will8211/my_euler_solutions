#!/usr/bin/env python3

'''
You are given the following information, but you may prefer to do some
research for yourself.

• 1 Jan 1900 was a Monday.
• Thirty days has September,
  April, June and November.
  All the rest have thirty-one,
  Saving February alone,
  Which has twenty-eight, rain or shine.
  And on leap years, twenty-nine.
• A leap year occurs on any year evenly divisible by 4, but not on a century
  unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?
'''

lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_counter = 2 # Jan. 1, 1901 --> Tuesday
hit_counter = 0
year = 1901


while year <= 2000:

    if year % 4 == 0:
        lengths[1] = 29
        # For other centuries:
        #if (year % 100 == 0) and (year % 400 != 0):
            #lengths[1] = 28
    else:
        lengths[1] = 28

    for i in lengths:
        if day_counter % 7 == 0:
            hit_counter += 1
        day_counter += i

    year += 1

print(hit_counter)
