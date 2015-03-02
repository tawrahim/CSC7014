#!/usr/bin/env python
# Tawheed Raheem
# Practice of a computer programmer
# Midterm
# This program displays the day of the week based
# on some inputs that the user provides us
# tabdulra@student.fitchburgstate.edu
# Problem 2
# Known bugs: the math that I am using appears to be off 

import math

# Hash map containing days of the week
days_of_week = {
                0: "Saturday",
                1: "Sunday",
                2: "Monday",
                3: "Tuesday",
                4: "Wednesday",
                5: "Thursday",
                6: "Friday"
               }

def print_day_of_the_week(y, m, d):
    if (m == 1):
        pass
    if (m == 2):
        pass
    #q = d
    #term_1 = (26 * (m+1))/10
    #j = y / 100
    #k = y % 100
    h = (d + ((26 * (m+1))/10)+ (y % 100) + ((y % 100)/4) + ((y/100)/4) + (5 * (y/100))) % 7 
    #print(h)
    print("Day of is " + str(days_of_week[int(h)]))

y = int(input("Enter year: (e.g. 2008): "))
m = int(input("Enter month: 1-12: "))
d = int(input("Enter day of the month: 1-31: "))
print_day_of_the_week(y, m, d)