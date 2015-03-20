#!/usr/bin/env python
# Tawheed Raheem
# Practice of a computer programmer
# Lab 5
# This program does the following:
#  (a) Checks if the backward of a given string is a palindrome
#  (b) Converts a word to pig latin
# tabdulra@student.fitchburgstate.edu
# known bugs: none

import re


def findPalindrome():
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
    

def pigLatin():
    print("\n\n ********** Pig Latin Program **********")
    print("This program prompts for an English word and prints its Pig Latin equivalent.")
    
    while True:
        user_input = str(input("Please enter an English word to convert into Pig Latin or enter . to quit: "))
        
        if user_input == ".":
            print("Thank you and have a great day!")
            break
        
        if not user_input:
            continue
    
        english_vowels = "aieou"
        first_letter = user_input[0].lower()
        
        if first_letter in english_vowels:
            print(user_input + " converted into Pig Latin is " + user_input + "yay")
        else:
            endString = ""
            for x in user_input:
                if x not in english_vowels:
                    endString += x
                else:
                    break
            print(user_input + " converted into Pig Latin is " + user_input[len(endString):] + endString + "ay")

def main():
    findPalindrome()
    pigLatin()

# Entry point of the program
if __name__ == "__main__":
    main()