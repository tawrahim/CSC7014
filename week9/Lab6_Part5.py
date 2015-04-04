#!/usr/bin/env python
# Tawheed Raheem
# Practice of a computer programmer
# Lab 9
# tabdulra@student.fitchburgstate.edu
# This program analyzes the contents of a file
#
# known bugs: None


import csv


def main():
    data_file = open("epaData_2008.csv", "r")
    lines = data_file.readline()
    print("There are " + str(len(lines.split(","))) + " fields in the file")

    print("Here are the lines with FERRARI in them")
    lines = data_file.readlines()[1:]
    for w in lines:
        if "FERRARI" in w:
            print(w.rstrip())


def create_mileage_list(file_pointer):
    mileage_list = []
    max_list = []
    min_list = []

    with open(file_pointer) as f:
        reader = csv.reader(f)
        next(reader, None)  # skip the headers

        for line in reader:
            if "VAN" not in line and "PICKUP" not in line:
                tup = (line[9], line[1], line[2])
                if int(line[9]) == 45:
                    max_list.append(str(tup[1] + " " + str(tup[2])))
                    pass
                elif int(line[9]) == 12:
                    min_list.append(str(tup[1] + " " + str(tup[2])))
                mileage_list.append(tup)

    print("Maximum and minimum Mileage: " + str(max(mileage_list)[0]) + " " + str(min(mileage_list)[0]))

    print("EPA car mileage")

    print("Maximum mileage cars: ")
    for x in max_list:
        print("\t" + x)

    print("Minimum mileage cars: ")
    for x in min_list:
        if "VAN" not in x and "PICKUP" not in x:
            print("\t" + x)


# Entry point of the program
if __name__ == "__main__":
    #main()
    create_mileage_list("epaData_2008.csv")