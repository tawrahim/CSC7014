#!/usr/bin/env python
# Tawheed Raheem
# Practice of a computer programmer
# Assignment 2
# tabdulra@student.fitchburgstate.edu
# This program generates some arithmetic examples
# It also finds perfect numbers, abundant numbers and deficient 
# numbers
# known bugs: None

# print numbers
def print_number_sequence_1():
    prev = ""
    for val in range(1, 10):
        prev += str(val)
        current_value = int(prev)
        print(str(current_value) + " * 8 + " + str(val) + " = " + str(current_value * 8 + val)) 
    print()

def print_number_sequence_2():
    prev = ""
    for val in range(1,10):
        prev += str(val)
        current_value = int(prev)
        print(str(current_value) + " * 9 + " + str(val+1) + " = " + str(current_value * 9 + val+1)) 
    print()

def print_number_sequence_3():
    base_number = 10
    prev = ""
    for val in reversed(range(0, 8)):
        base_number -= 1
        prev += str(base_number)
        print( prev + " * 9 + " + str(prev) + " = " + str(int(prev) * 9 + val)) 
    print()

def print_number_sequence_4():
    prev = ""
    for val in range(1,10):
        prev += str(1)
        print(prev + " * " + prev + " = " + str(int(prev) * int(prev)))
    print()


# helper function to check if a number is a perfect number
# source https://www.daniweb.com/software-development/python/threads/261804/printing-perfect-numbers
def is_a_perfect_number(n):
    count = 0
    for i in range(1, n):
        if (n % i == 0):
            count += i
    if (count == n):
        return True
    else:
        return False
    return True

# helper function to check if number is an abundant number
# source http://codereview.stackexchange.com/questions/39946/optimizing-solution-for-project-euler-problem-23-non-abundant-sums
def is_a_abundant_number(n):
    max_divisor = int(n / 2) + 1
    sum = 0
    for x in range(1, max_divisor):
        if (n % x == 0):
            sum += x  
    return sum > n

def finding_perfect_and_abundant_and_deficient_numbers():
    print("Given an upper bound of a given number, we would find the perfect square")
    print()

    upper_bound_number = int(input("What is the upper number for the range: (must be a valid integer): "))

    perfect_number_count = 0
    abundant_number_count = 0
    deficient_number_count = 0
    total = 0
    for index, value in enumerate(range(2, upper_bound_number+1)):
        total += 1
        if is_a_perfect_number(value):
            perfect_number_count += 1
            print(str(value) + " is a perfect number")
        elif is_a_abundant_number(value):
            abundant_number_count += 1
        else: 
            deficient_number_count += 1

    print()
    print("In the range 2 - 1000  there are ")
    print(str(perfect_number_count) + " perfect numbers")
    print(str(abundant_number_count) + " abundant numbers")
    print(str(deficient_number_count) + " deficient numbers")

# Entry point of the program
if __name__ == "__main__":
    print("The following is a nice arithmetic examples")
    print_number_sequence_1()
    print_number_sequence_2()
    print_number_sequence_3()
    print_number_sequence_4()
    finding_perfect_and_abundant_and_deficient_numbers()
