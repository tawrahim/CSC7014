# Tawheed Raheem
# Practice of a computer programmer
# Lab 1
# tabdulra@student.fitchburgstate.edu
# This program tests the fundamentals of programming
# known bugs: None

import math
import time

height = float(input('Please enter the height of the room'))
width = float(input('Please enter the width of the room'))
tile_size = float(input('Please enter tile size'))
amount_of_tiles_needed = (height * width) / tile_size
print('The amount of tiles needed is ' + str(amount_of_tiles_needed))

number_of_people_in_your_class = float(input('How many people are in your class: ')) - 1
total_handshake = ((number_of_people_in_your_class * number_of_people_in_your_class) + number_of_people_in_your_class)/ 2
print('The total hand shake would be ' + str(total_handshake))

how_many_people_are_Around_you = int(input('How many people are around you: '))
sum_of_ages = 0
for count in range(how_many_people_are_Around_you):
    sum_of_ages += int(input("Please enter the age of person " + str(count + 1) + " "))

print('The average age is ' + str(sum_of_ages // how_many_people_are_Around_you))


radius = float(input('Please enter the radius '))
total = (4/3) * (math.pi * math.pow(radius, 3))
print('The sphere is : ' + str(total))

miles_away = 2.9 * (5.878 * math.pow(10, 21))
print('The miles away is the Andromeda galaxy is ' + str(miles_away))

print(' 2 to the 120th is ' + str(math.pow(2, 120)))

print('The factorial is ' + str(math.factorial(13)))
print ('Today’s date is: ' + time.strftime('%Y-%m-%d'))
