#!/usr/bin/env python
# Tawheed Raheem
# Practice of a computer programmer
# Lab 8
# tabdulra@student.fitchburgstate.edu
# This program analyzes the contents of a file
# hands
# known bugs: None


import re


def get_word_list():
    data_file = open("GettysburgAddress.txt", "r")
    word_list = []

    for x in data_file:
        line = x.strip().lower().split(" ")
        for w in line:
            cleaned_word = re.sub("[^a-zA-Z]+", "", w)

            # Handle case where we have an empty string
            if cleaned_word:
                word_list.append(cleaned_word)
    return word_list


def make_unique_words(speech_list):
    unique = []
    for word in speech_list:
        if word not in unique:
            unique.append(word)
    return unique


def main():
    speech_list = get_word_list()
    print("Speech Length: ", len(speech_list))

    unique_words = make_unique_words(speech_list)
    print("Unique Length: ", len(unique_words))
    print(unique_words)


# Entry point of the program
if __name__ == "__main__":
    main()