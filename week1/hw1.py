# Tawheed Raheem
# Practice of a computer programmer
# Assignment 1
# tabdulra@student.fitchburgstate.edu
# This program calculates the material needed for building an
# ornamental garden
# known bugs: The formular I used to calculate plants for the circle does not seem right

import math


print('Calculate Garden requirements')
print('-----------------------------')

length_of_side = float(input('Enter length of side of garden (feet): '))
spacing_of_garden = float(input('Enter spacing between plants (feet): '))
depth_of_garden = float(input('Enter depth of garden soil (feet): '))
depth_of_fill = float(input('Enter depth of fill (feet): '))

# Converts feet to yards
def feet_to_yard(feet):
    return feet / 3 

area = math.floor((math.pi * (1/16) * length_of_side * length_of_side) * (spacing_of_garden * 12))
soil_for_garden_in_yards = round(math.pi * (1/16) * feet_to_yard(length_of_side) * feet_to_yard(length_of_side) * feet_to_yard(depth_of_garden), 1)

#zz = (length_of_side/4) * (length_of_side/4)
#area = math.pi * zz
#vodo = (144 * area) / (spacing_of_garden * 12) * (spacing_of_garden * 12)
print()
print('-----------------------------')
print('Requirements \n')

print('Plants for each semicircle garden: ' + str(area // 2))
print('Plants for the circle garden: ' + str(area))
print('Total plants for garden: ' + str(area * 3))
print('Soil for each semicircle garden: ' + str(round(soil_for_garden_in_yards/2, 1)) + ' cubic yards')
print('Soil for the circle garden: ' + str(soil_for_garden_in_yards) + ' cubic yards')
print('Total soil for the garden: ' + str(round(soil_for_garden_in_yards * 3, 1)) + ' cubic yards')
