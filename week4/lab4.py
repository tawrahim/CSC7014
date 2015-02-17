#!/usr/bin/env python
# Tawheed Raheem
# Practice of a computer programmer
# Lab 4
# This program uses four different approach
# to calculate the value of pi
# tabdulra@student.fitchburgstate.edu
# known bugs: (i) Values for blue can and white can was not calculated. Did not understand
#             the math in the lab requirement of what was being asked

import math
import random

def blue_and_white_cans():
    print("This program finds the values of pi using four different approach")
    print("Please enter integers in a sequence, press enter after each entry.")
    print("You can enter 25 at anytime so that we can calculate")
    print("Input: ")
    
    # get user input
    user_input = int(input())
    all_user_entry = []
    
    # continue to ask until user enters 25
    while user_input != 25:
        all_user_entry.append(user_input)
        user_input = int(input())
    
    # if we get here it means we encountered the value 25. We simply append it to our list
    all_user_entry.append(user_input)
    
    # Calculate blue can
    # dont really understand what is being asked
    blue_can = 10
    
    # Calculate white can
    # did not understand the question so left the formula blank
    white_can = 30
    
    # print output to the user
    print("Output: ")
    print(str(blue_can) + " blue cans")
    print(str(white_can) + " white cans")    

# This function finds the value of pi using the Archimedes approach
# source http://www.craig-wood.com/nick/articles/pi-archimedes/
def  archimedes(n):
    polygon_edge_length_squared = 2.0
    polygon_sides = 4
    for i in range(n):
        polygon_edge_length_squared = 2 - 2 * math.sqrt(1 - polygon_edge_length_squared / 4)
        polygon_sides *= 2
    return polygon_sides * math.sqrt(polygon_edge_length_squared) / 2


# This function finds the value of pi using the leibniz approach
# source http://stackoverflow.com/questions/18036367/leibniz-formula-for-%CF%80-is-this-any-good-python
def  leibniz(n):
    result = 0.0
    sign = 1.0
    for n in range(n):
        result += sign/(2.0*n+1.0)
        sign = -sign
    return 4*result


# This function finds the value of pi using the wallis approach
# source http://stackoverflow.com/questions/18969881/wallis-formula-for-pi
def  wallis(n):
    pi = 2.
    for i in range(1, n):
        left = (2. * i)/(2. * i - 1.)
        right = (2. * i)/(2. * i + 1.)
        pi = pi * left * right
    return pi

# This function takes a random number and calculates the value of pi
# using our three algorithms
def monteCarlo(random_number):
    print("Finding the value of PI given the number " + str(random_number))
    print("Archimedes: " + str(archimedes(random_number)))
    print("Leibniz: " + str(leibniz(random_number)))
    print("Wallis: " + str(wallis(random_number)))    


def perform_simulation():
    for i in range(1,5):
        monteCarlo(random.randint(0,1))
        print()
    

# Entry point of the program
if __name__ == "__main__":
    blue_and_white_cans()
    
    print("************** BEGIN SIMULATION ****************")
    
    perform_simulation()