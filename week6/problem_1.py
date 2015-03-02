#!/usr/bin/env python
# Tawheed Raheem
# Practice of a computer programmer
# Midterm
# This program is generates a lottery number
# and then based on some criteria we see whether or not a user won 
# tabdulra@student.fitchburgstate.edu
# Problem 1
# Known bugs: none


from random import randint


def generate_number():
    randomly_generated_number1 = str(randint(0, 9))
    randomly_generated_number2 = str(randint(0, 9)) 
    randomly_generated_number3 = str(randint(0, 9)) 
    return str(randomly_generated_number1 + randomly_generated_number2 + randomly_generated_number3)


user_input = input("Please enter a valid three digit number: ")
random_number = generate_number()

# checks for perfect streak
def perfect_streak():
    streak = 0
    looper = 0
    for x in random_number:
        if x == user_input[looper]:
            streak += 1
        looper += 1
    return streak == 3

def matches_in_some_order():
    matches = 0
    for x in user_input:
        if x in random_number:
            matches += 1
    return matches

print("The lottery number is " + random_number)

if perfect_streak():
    print("The award is $10,000")
elif matches_in_some_order() == 3:
    print("The award is $5000")
elif matches_in_some_order() == 2:
    print("The award is $3000")
elif matches_in_some_order() == 1:
    print("The award is $1000")
else:
    print("Sorry you made no money from the lottery try again later!")
    