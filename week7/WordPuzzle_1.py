#!/usr/bin/env python
# Tawheed Raheem
# Practice of a computer programmer
# Lab 7
# tabdulra@student.fitchburgstate.edu
# This program looks in a text file that contains dictionary words
# and then finds out if each of the word has vowels in the order 'aeiou'
# known bugs: None


vowels = 'aeiou'


# takes a word and strips the whitespace characters
#  and converts it to lowercase and returns it
def clean_word(word):
    return word.lower().strip()


# takes word and returns a string of vowels in that word in the order
#  in which they appear. (For example getVowelsInWord(“vowels”)
# should return “oe” and getVowelsInWord(“hehiho”)
def get_vowels_in_word(word):
    result = ""
    for char in word:
        if char in vowels:
            result += char
    return result


def main():
        try:
            with open("dictionary.txt", 'r') as f:
                read_data = f.readlines()
            print("Find words containing vowels 'aeiou' in that order: ")
            for word in read_data:
                cleaned_word = clean_word(word)
                if len(cleaned_word) > 6 and get_vowels_in_word(cleaned_word) == vowels:
                    print(cleaned_word)

        except IOError:
            print("Error opening file: ", "dictionary.txt")


# Entry point of the program
if __name__ == "__main__":
    main()