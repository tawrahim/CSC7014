#!/usr/bin/env python
# Tawheed Raheem
# Practice of a computer programmer
# Lab 2
# tabdulra@student.fitchburgstate.edu
# This program has two parts:
#  (i) First we find the product by using the Russian Peasant algorithm
#  (ii) We implementthe hailstone formula
# known bugs: None


''' This algorithm first asks the user for two
    integers "A" and "B" to be multipled
    we repeatedly multiply A by 2 and divide B by 2, 
    until B cannot be divided any further, that is until its 
    value becomes 0.  During each step, whenever B is 
    an odd number, we add the corresponding 
    A value to the product we are generating.  
'''
def russuian_peasant_algorithm():
    number_a_value = int(input("Please enter a value for A: "))
    number_b_value = int(input("Please enter a value for B: "))
    total_sum = 0
    while number_b_value >= 1:
        if number_b_value % 2 != 0:
            total_sum += number_a_value
        number_b_value = number_b_value // 2
        number_a_value = number_a_value * 2

    print("The sum is " + str(total_sum))

'''
    We repeatedly ask the user if they want to try with
    two different numbers. The first time that the program runs
    we set the user_input value to 'Y'
'''
user_input = 'Y'
while user_input == 'Y':
    russuian_peasant_algorithm()
    user_input = input("Do you want to do it again [Y/N]: ")

hailstone_value = int(input("Please enter a hailstone value: "))
sequence_count = 1 # count starts at 1 because user input is part of sequence
sequence_string = str(hailstone_value) + ", " # Add user input to sequence
while hailstone_value > 1:
    sequence_count += 1
    if hailstone_value % 2 == 0:
        hailstone_value = hailstone_value // 2
    else:
        hailstone_value = (hailstone_value * 3) + 1
    sequence_string += str(hailstone_value) + ", "
print("The length of the sequence is: " + str(sequence_count))
print("The hailstone sequence is: " + sequence_string[:-2]) # we remove the last 2 letters since at each step we add a space and comma " , "

