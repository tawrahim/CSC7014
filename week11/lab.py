#!/usr/bin/env python
# Tawheed Raheem
# Practice of a computer programmer
# Lab 11
# tabdulra@student.fitchburgstate.edu
# This program checks reads in two files and then stores them in different set
# We perform various sets operations on our two files like union, intersection,
# Symmetric Difference and also a diff on the two sets
# known bugs: None

import re
import sys

gettysburg_set = set()
independence_declaration_set = set()


def process_line(line, flag):
    words_in_line = line.strip().lower().split(" ")
    for word in words_in_line:
        cleaned_word = re.sub("[^a-zA-Z]+", "", word)

        if cleaned_word:
            if len(cleaned_word) > 3:
                add_word(cleaned_word, flag)


def add_word(word, flag):
    if flag == "gettysburg_set":
        gettysburg_set.add(word)
    elif flag == "independence_set":
        independence_declaration_set.add(word)


def pretty_print():
    print("Count of unique words of length 4 or greater:")
    print("Gettsyburg Address: " + str(len(gettysburg_set)) + ", Declaration of Independence: "
          + str(len(independence_declaration_set)) + "\n")

    print("Operation                      Count")
    print("------------------------------------")
    print("Union                            " + str(len(gettysburg_set.union(independence_declaration_set))))
    print("Intersection                     " + str(len(gettysburg_set.intersection(independence_declaration_set))))
    print("Symmetric Difference             " +
          str(len(gettysburg_set.symmetric_difference(independence_declaration_set))))
    print("GA-DoI                           " + str(len(gettysburg_set - independence_declaration_set)))
    print("DoI-GA                           " + str(len(independence_declaration_set - gettysburg_set)))

    print()
    print("Common Words to both")
    print("--------------------")

    count = 0
    max_spaces = 15
    for word in gettysburg_set.intersection(independence_declaration_set):
        if count % 5 == 0:
            print()
        sys.stdout.write(word + str(" "*(max_spaces - len(word))))
        count += 1


def main():
    # The file array holds a tuple with file name as well the set that
    # we are going to be adding
    file_array = [("GettysburgAddress.txt", "gettysburg_set"),
                  ("DeclarationOfIndependence.txt", "independence_set")]

    for file_name in file_array:
        data_file = open(file_name[0], "r")
        for line in data_file:
            process_line(line, file_name[1])
    pretty_print()


if __name__ == '__main__':
    main()