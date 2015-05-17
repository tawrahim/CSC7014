#!/usr/bin/env python
# Tawheed Raheem
# Practice of a computer programmer
# Assignment 9
# tabdulra@student.fitchburgstate.edu
# This program
# known bugs: None

import csv


def main():
    file_object = open("Periodic_Table.csv", "rU")
    reader = csv.reader(file_object)
    for row in reader:
        print(row)


if __name__ == '__main__':
    main()