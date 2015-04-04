#!/usr/bin/env python
# Tawheed Raheem
# Practice of a computer programmer
# Lab 10
# tabdulra@student.fitchburgstate.edu
# This program checks the word of frequency
# of the words in Lincoln’s Gettysburg address
# known bugs: None

import re
import operator

all_words = {}


def process_line(line):
    words_in_line = line.strip().lower().split(" ")
    for word in words_in_line:
        cleaned_word = re.sub("[^a-zA-Z]+", "", word)

        if cleaned_word:
            add_word(cleaned_word)


def add_word(word):
    if word in all_words:
        all_words[word] += 1
    else:
        all_words[word] = 1


def pretty_print():
    print("# of unique unique words in the Gettysburg address: " + str(len(all_words)))
    print("Word            Count")
    print("---------------------")

    sorted_list = sorted(all_words.items(), key=operator.itemgetter(1))

    max_spaces = 18
    for word_tuple in reversed(sorted_list):
        word = word_tuple[0]
        count = word_tuple[1]
        print(str(word) + str(" "*(max_spaces - len(word))) + str(count))


def main():
    data_file = open("GettysburgAddress.txt", "r")
    for line in data_file:
        process_line(line)
    pretty_print()


if __name__ == '__main__':
    main()