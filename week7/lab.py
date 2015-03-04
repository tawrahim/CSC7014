#!/usr/bin/env python
# Tawheed Raheem
# Practice of a computer programmer
# Lab 7
# tabdulra@student.fitchburgstate.edu
# This program
# known bugs: None


def count_total_hands_in_file():
    print("Total hands in file: ")


def hands_count_by_rank_number():
    print("Hand counts by rank number: ")


def probability():
    print("Probability: ")


def prompt_user_for_data():
    while True:
        try:
            file_name = input("Enter a file name: ")
            with open(file_name, 'r') as f:
                read_data = f.read()

            count_total_hands_in_file()

            hands_count_by_rank_number()

            probability()
            break
        except IOError:
            print("Error opening file: ", file_name)


def main():
    prompt_user_for_data()

# Entry point of the program
if __name__ == "__main__":
    main()