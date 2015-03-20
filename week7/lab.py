#!/usr/bin/env python
# Tawheed Raheem
# Practice of a computer programmer
# Lab 7
# tabdulra@student.fitchburgstate.edu
# This program counts finds the probabilty of poker
# hands
# known bugs: None


def count_total_hands_in_file(file):
    count = 0
    for _ in file:
        count += 1
    return count


def hands_count_by_rank_number(file):
    total_hands = 0
    for line in file:
        arr = line.split(",")
        if int(arr[len(arr) - 1]) == 1:
            total_hands += 1
    return total_hands


def probability(a, b):
    return (a / b) * 100


def prompt_user_for_data():
    while True:
        try:
            file_name = input("Enter a file name: ")
            with open(file_name, 'r') as f:
                read_data = f.readlines()

            count = count_total_hands_in_file(read_data)

            print("Total hands in file: " + str(count))

            hands_rank = hands_count_by_rank_number(read_data)

            print("Hand counts by rank number: " + str(hands_rank))

            p = probability(hands_rank, count)

            print("Probability of pair: " + str(p) + "%")

            break
        except IOError:
            print("Error opening file: ", file_name)


def main():
    prompt_user_for_data()

# Entry point of the program
if __name__ == "__main__":
    main()