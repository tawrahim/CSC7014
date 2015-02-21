#!/usr/bin/env python
# Tawheed Raheem
# Practice of a computer programmer
# Lab 5
# This program does the following:
#  (a) Checks if the backward of a given string is a palindrome
# tabdulra@student.fitchburgstate.edu
# known bugs: none

import re

def main():
    print("***** Check to see if a string is palindrome *****")
    
    # while True:
    user_input = str(input("Input a string: or enter return to quit: "))
    if not user_input:
        return
    
    stripedString = re.sub('[^A-Za-z0-9]+', '', user_input)
    print("The original string is: {}".format(user_input))
    print("The modified string is: {}".format(stripedString.lower()))
    print("The reversal is: {}".format(stripedString[::-1].lower()))
    
    if stripedString.lower() == stripedString[::-1].lower():
        print("String is palindrome")
    else:
        print("String is not palindrome")
    

# Entry point of the program
if __name__ == "__main__":
    main()