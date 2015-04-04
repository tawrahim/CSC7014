#!/usr/bin/env python
# Tawheed Raheem
# Practice of a computer programmer
# Home work
# tabdulra@student.fitchburgstate.edu
# This program analyzes stock prices from google
# It finds the average based on a month, at the end it prints
# the top 6 and bottom 6
#
# known bugs: None


import csv
import operator


def get_data_list(file_name):
    data_list = []  # start with an empty list

    with open(file_name) as f:
        reader = csv.reader(f)
        next(reader, None)  # skip the headers

        for line in reader:
            data_list.append(line)

    return data_list


def get_monthly_averages(data_list):
    dictionary = {}
    monthly_average_map = {}

    for x in data_list:
        date = x[0].split("/")
        key = date[0] + "/" + date[2]
        if key in dictionary:
            dictionary[key] += x
        else:
            dictionary[key] = x

    for k, v in dictionary.items():
        #print("Processing " + str(k))
        start = 0
        end = 7

        running_sum_of_numerator = 0
        running_sum_of_denominator = 0

        for x in range(0, len(v), 7):
            block = v[start:end]
            #print(block)

            volume = int(block[5])
            adj_close = float(block[6])

            running_sum_of_numerator += (volume * adj_close)
            running_sum_of_denominator += volume

            start = end
            end += 7

        monthly_average_map[k] = (running_sum_of_numerator/running_sum_of_denominator)

    return monthly_average_map


def print_info(monthly_average_list):
    size = len(monthly_average_list)
    sorted_list = sorted(monthly_average_list.items(), key=operator.itemgetter(1))

    print("#############################################################")
    print("#                                                           #")
    print("#                                                           #")
    print("#                                                           #")
    print("#                                                           #")
    print("#     ANALYSIS OF STOCK PRICES FROM (2005 - 2015)           #")
    print("#                                                           #")
    print("#                                                           #")
    print("#                                                           #")
    print("#############################################################")

    counter = 0
    top_6 = []
    bottom_6 = []

    for x in sorted_list:
        if counter < 6:
            bottom_6.append(x)

        if counter >= size - 6:
            top_6.append(x)

        counter += 1

    # print top 6
    print("Printing the top 6 averages")
    print("MONTH    AVERAGE")
    for x in top_6:
        print(str(x[0]) + ":  " + "%.2f" % float(x[1]))

    # print bottom 6
    print()
    print("Printing the bottom 6 averages")
    print("MONTH    AVERAGE")
    for x in reversed(bottom_6):
        print(str(x[0]) + ":  " + "%.2f" % float(x[1]))

if __name__ == '__main__':
    res = get_data_list("GoogleStockPrices.csv")
    monthly_average_res = get_monthly_averages(res)
    print_info(monthly_average_res)