#!/usr/bin/env python
# Tawheed Raheem
# Practice of a computer programmer
# Lab 8
# tabdulra@student.fitchburgstate.edu
# This program checks and see if two words are anagrams
# hands
# known bugs: None


def anagram_test():
    user_input = input("Enter two words separated by a space: ")
    if not user_input:
        return

    if len(user_input.split(" ")) < 2:
        print("You must enter two words")
        return

    word1 = user_input.split(" ")[0]
    word2 = user_input.split(" ")[1]

    if not word2:
        print("Please enter a value for the second word")
        return

    if word1 == word2[::-1]:
        print(word1 + " and " + word2 + " are anagrams of each other")
    else:
        print(word1 + " and " + word2 + " are not anagrams of each other")

# Entry point of the program
if __name__ == "__main__":
    anagram_test()

