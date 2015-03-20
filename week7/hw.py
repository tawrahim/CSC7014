#!/usr/bin/env python
# Tawheed Raheem
# Practice of a computer programmer
# Home work problem
# tabdulra@student.fitchburgstate.edu
# This program solves a puzzle from a dictionary
# hands
# known bugs: None


def get_word_list():
    data_file = open("wordlist.txt", "r")
    word_list = []

    for word in data_file:
        word_list.append(word.strip().lower())
    return word_list


# Helper function to determine whether a given word is uncapitalized and unhyphenated
def is_uncapitalized_unhyphenated(word):
    # check if word does not contain hyphen
    if "-" in word:
        return True

    # Make sure that the word is uncapitalized
    if word[0].isupper():
        return True

    return False


# Find all uncapitalized, unhyphenated  word that contains all but one of the
# letters of the alphabet from “l” to “v” (“lmnopqrstuv”)
def solution_1(word):
    criteria = "lmnopqrstuv"
    match_list = []

    if is_uncapitalized_unhyphenated(word):
        return False

    if len(word) < len(criteria):
        return False

    for w in word:
        if w in criteria:
            if w not in match_list:
                match_list.append(w)

    if len(match_list) != 10:
        return False

    missing_from_list = []
    for x in criteria:
        if x not in match_list:
            missing_from_list.append(x)

    return len(missing_from_list) == 1


# Find all uncapitalized, seven-letter words, where each word contains
# just a single vowel and does not have the letter ‘s’ anywhere within it.
def solution_2(word):
    vowels = "aeiou"
    number_of_vowels = 0
    found_vowels = []

    if len(word) != 7:
        return False

    if is_uncapitalized_unhyphenated(word):
        return False

    if "s" in word:
        return False

    for x in word:
        if x in vowels:
            found_vowels.append(x)
            number_of_vowels += 1

    return number_of_vowels == 1


# The word mimeographs contains all the letters of memphis at least once.
# Find other words that also contain all the letters of  memphis
def solution_3(word):
    memphis = "memphis"
    m_count = 0  # the letter m is special because it appears twice
    match = []

    if is_uncapitalized_unhyphenated(word):
        return False

    if len(word) < len(memphis):
        return False

    for x in word:
        if x in memphis:
            if x == "m":  # m is a special case so we treat it seperately
                if m_count < 2:
                    match.append(x)
                    m_count += 1
            if x not in match:
                match.append(x)

    if len(match) != 7:
        return False

    for x, y in zip(sorted(memphis), sorted(match)):
        if x != y:
            return False

    return True


def aux(word, matcher):
    count = 0
    for _ in word:
        if len(word[count:]) < len(matcher):
            return False
        elif word[count:count + len(matcher)] == matcher:
            return True
        count += 1
    return False


# Find all words that contain the string ‘tantan”
def solution_4(word):
    return aux(word, "tantan")


# The word marine consists of five consecutive, overlapping state postal abbreviations:
# Massachusetts (MA), Arkansas(AR), Rhode Isalnd(RI), Indiana(IN), and Nebraska(NE).
# Find all seven letter words that have the same property.
def solution_5(word):
    if len(word) != 7:
        return False
    return aux(word, "marine")


# When you are writing a script, there are four letters of the alphabet that cannot be
# completed in one stroke: ‘i’ and ‘j’ (which require dots) and ‘t’ and ‘x’
# (which require crosses).  Find all words that use each of these letters exactly once.
def solution_6(word):
    criteria = ['i', 'j', 't', 'x']
    builder = []
    for w in word:
        if w in builder:
            return False
        if w in criteria:
            builder.append(w)

    if len(builder) != len(criteria):
        return False

    temp = []
    for x in builder:
        if x in temp:
            return False
        temp.append(x)

    return True


# Find all words that contain the consecutive letters “nacl”.
def solution_7(word):
    return aux(word, "nacl")


# Find all words that contain the vowels a, e, i, o, and u in that order.
def solution_8(word):
    vowel = ['a', 'e', 'i', 'o', 'u']
    builder = []
    for x in word:
        if x in vowel:
            builder.append(x)

    if len(vowel) != len(builder):
        return False

    for a, b in zip(vowel, builder):
        if a != b:
            return False

    return True


# Consider the word sure.  If I asked you to add two pairs of doubled letters to it to
# make an eight-letter word, you could add p’s and s’s to make suppress.  Find an
# eight-letter word resulting from adding two pairs of doubled letters to rate
def solution_9(word):

    if len(word) != 8:
        return False

    if "rate" not in word:
        return False

    # check if the first two and last two letters are similar
    return word[0:2] == word[-2:]


# Two U.S. state capitals have a prefix that is the name of the month.  Find them.
def solution_10():
    result = []

    state_capitals = [
        "Montgomery", "Juneau", "Phoenix", "Little Rock", "Sacramento", "Denver", "Hartford", "Dover", "Tallahassee",
        "Atlanta",
        "Honolulu", "Boise", "Springfield", "Indianapolis", "Des Moines", "Topeka", "Frankfort", "Baton Rouge",
        "Augusta", "Annapolis",
        "Boston", "Lasing", "St. Paul", "Jackson", "Jefferson City", "Helena", "Lincoln", "Carson City", "Concord",
        "Trenton",
        "Santa Fe", "Albany", "Raleigh", "Bismarck", "Columbus", "Oklahoma City", "Salem", "Harrisburg", "Providence",
        "Columbia",
        "Pierre", "Nashville", "Austin", "Salt Lake City", "Montpelier", "Richmond", "Olympia", "Charleston", "Madison",
        "Cheynne"
    ]

    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    for capital in state_capitals:
        for month in months:
            if len(capital) >= len(month):
                if capital.startswith(month):
                    result.append(capital)

    return result


def puzzle(word_list):
    solution_1_array = []
    solution_2_array = []
    solution_3_array = []
    solution_4_array = []
    solution_5_array = []
    solution_6_array = []
    solution_7_array = []
    solution_8_array = []
    solution_9_array = []

    for word in word_list:
        if solution_1(word):
            solution_1_array.append(word)
        if solution_2(word):
            solution_2_array.append(word)
        if solution_3(word):
            solution_3_array.append(word)
        if solution_4(word):
            solution_4_array.append(word)
        if solution_5(word):
            solution_5_array.append(word)
        if solution_6(word):
            solution_6_array.append(word)
        if solution_7(word):
            solution_7_array.append(word)
        if solution_8(word):
            solution_8_array.append(word)
        if solution_9(word):
            solution_9_array.append(word)

    # Print puzzles
    if solution_1_array:
        print("***** All uncapitalized, unhyphenated  word that contains all but one of the "
              "letters of the alphabet from “l” to “v” (“lmnopqrstuv”) *****")
        for x in solution_1_array:
            print(x)

    if solution_2_array:
        print("***** All uncapitalized, seven-letter words, where each word contains"
              "just a single vowel and does not have the letter ‘s’ anywhere within it. *****")
        for x in solution_2_array:
            print(x)

    if solution_3_array:
        print("***** All uncapitalized, seven-letter words, where each word contains"
              "just a single vowel and does not have the letter ‘s’ anywhere within it. *****")
        for x in solution_3_array:
            print(x)

    if solution_4_array:
        print("***** All words that contain the string 'tantan' *****")
        for x in solution_4_array:
            print(x)

    if solution_5_array:
        print("***** The word marine consists of five consecutive, overlapping state postal "
              "abbreviations: Massachusetts (MA), Arkansas(AR), Rhode Isalnd(RI), Indiana(IN), and Nebraska(NE). *****")
        print(" All seven letter words that have the same property. ****'")
        for x in solution_5_array:
            print(x)

    if solution_6_array:
        print("***** All words that use 'x' and 't' exactly once. *****")
        for x in solution_6_array:
            print(x)

    if solution_7_array:
        print("*****  All words that contain the consecutive letters “nacl” *****")
        for x in solution_7_array:
            print(x)

    if solution_8_array:
        print("***** All words that contain the vowels a, e, i, o, and u in that order. *****")
        for x in solution_8_array:
            print(x)

    if solution_9_array:
        print("***** An eight-letter word resulting from adding two pairs of doubled letters to rate *****")
        for x in solution_9_array:
            print(x)

    if solution_10():
        print("***** Two U.S. state capitals have a prefix that is the name of the month.  Find them. *****")
        for x in solution_10():
            print(x)

# Entry point of the program
if __name__ == "__main__":
    words = get_word_list()
    puzzle(words)