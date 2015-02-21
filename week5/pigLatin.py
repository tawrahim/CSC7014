#!/usr/bin/env python
# Tawheed Raheem
# Practice of a computer programmer
# Lab 5
# This program does the following:
# If a word begins with a vowel, it appends "yay" to the end of the word.
# If a word begins with a consonant, remove all the consonants from the beginning up to 
# the first vowel and append them to the end of the word. Finally, append "ay" to the end of the word.
# tabdulra@student.fitchburgstate.edu
# known bugs: none

    
def main():
    print("********** Pig Latin Program **********")
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

# Entry point of the program
if __name__ == "__main__":
    main()