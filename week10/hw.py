#!/usr/bin/env python
# Tawheed Raheem
# Practice of a computer programmer
# Assignment 8
# tabdulra@student.fitchburgstate.edu
# This program cleans up the US census data and provides
# an interface where the user can ask for the census year
# and we will return the minimum and maximum for that given year
# known bugs: None


list_of_states = [
        "Maine", "New Hampshire", "Vermont", "Massachusetts", "Rhode Island", "Connecticut", "New York", "New Jersey",
        "Pennsylvania", "Ohio",
        "Indiana", "Illinois", "Michigan", "Wisconsin", "Minnesota", "Iowa", "Missouri", "North Dakota", "South Dakota",
        "Nebraska",
        "Kansas", "Delaware", "Maryland", "District of Columbia", "Virginia", "West Virginia", "North Carolina",
        "South Carolina", "Georgia", "Florida",
        "Kentucky", "Tennessee", "Alabama", "Mississippi", "Arkansas", "Louisiana", "Oklahoma", "Texas", "Montana",
        "Idaho", "Wyoming", "Colorado", "New Mexico", "Arizona", "Utah", "Nevada", "Washington", "Oregon", "California",
        "Alaska", "Hawaii"
        ]

'''
We have 10 totals years that we are interested in
so we build up an array to hold that data.
index 1 represents entry for 1990, index 2 is for 1980 and so on...
The end array is in the format
  [
    [('Louisiana', '4219973'), ('New York', '17990455'), ('Idaho', '1006749'), ('Wyoming', '453588'), ('Iowa', '2776755'),
    ('New Mexico', '1515069'), ('Georgia', '6478216'), ('Vermont', '562758'), ('Washington', '4866692'),
    ('Tennessee', '4877185'), ('Colorado', '3294394'), ('Florida', '12937926'), ('District of Columbia', '606900'),
    ('Wisconsin', '4891769'), ('Michigan', '9295297'), ('Utah', '1722850'), ('Virginia', '6187358'),
    ('New Hampshire', '1109252'), ('Alaska', '550043'), ('Ohio', '10847115'), ('Arkansas', '2350725'),
    ('Oregon', '2842321'), ('Texas', '16986510'), ('Nevada', '1201833'), ('Alabama', '4040587'),
    ('West Virginia', '1793477'), ('Indiana', '5544159'), ('Nebraska', '1578385'), ('Delaware', '666168'),
    ('Maryland', '4781468'), ('Rhode Island', '1003464'), ('Illinois', '11430602'), ('North Carolina', '6628637'),
    ('South Carolina', '3486703'), ('Montana', '799065'), ('Massachusetts', '6016425'), ('Maine', '1227928'),
    ('California', '29760021'), ('South Dakota', '696004'), ('Minnesota', '4375099'), ('Arizona', '3665228'),
    ('Mississippi', '2573216'), ('Hawaii', '1108229'), ('Kentucky', '3685296'), ('Missouri', '5117073'),
    ('Pennsylvania', '11881643'), ('Connecticut', '3287116'), ('Kansas', '2477574'), ('New Jersey', '7730188'),
    ('North Dakota', '638800'), ('Oklahoma', '3145585')], ........
  ]
'''
def group_census_data_based_on_the_year(states_and_population_data):
    cleaned_up_census_data = [
        [], [], [], [], [], [], [], [], [], [],
    ]
    for item in states_and_population_data:
        census_values = states_and_population_data[item]
        index = 0
        for x in reversed(census_values):
            tup = (int(x.replace(",", "")), item)
            cleaned_up_census_data[index].append(tup)
            index += 1

    # write output to file
    for line in cleaned_up_census_data:
        with open('file_to_write.txt', 'a') as f:
            f.write(str(line))
            f.write("\n")

    return cleaned_up_census_data


def get_max_and_min_census_data_for_year(year, sanitized_census_data):
    mapping_of_year_and_index = {
        1990: 9,
        1980: 8,
        1970: 7,
        1960: 6,
        1950: 6,
        1940: 4,
        1930: 3,
        1920: 2,
        1910: 1,
        1900: 0
    }

    if year not in mapping_of_year_and_index:
        print("The year you entered is not valid")
        return

    # Find max and min value from the sanitized census data set
    year_index = mapping_of_year_and_index[year]
    data_for_requested_year = sanitized_census_data[year_index]

    min_population = data_for_requested_year[0][0]
    max_population = data_for_requested_year[0][0]
    max_tuple = ()
    min_tuple = ()
    for x in data_for_requested_year:
        if x[0] > max_population:
            max_tuple = x
            max_population = x[0]
        elif x[0] < min_population:
            min_tuple = x
            min_population = x[0]

    print("Minimum: " + str(min_tuple))
    print("Maximum: " + str(max_tuple))


def clean_up_data_set(year):
    lines = []
    states_and_population_data = {}

    data_file = open("urpop0090.txt", "r")
    for line in data_file:

        # remove new line
        cleaned_line = line.rstrip()

        # ignore empty lines
        if cleaned_line:

            for state in list_of_states:
                without_pre_spaces = line.lstrip()
                if without_pre_spaces.startswith(state):
                    splitter = without_pre_spaces[len(state):].split()

                    # some of the entries contain 'r *2 and *1' inside them, we want to go ahead and remove it
                    weird_characters = ["r", "*1", "*2"]

                    cleaned_list = []
                    for item in splitter:
                        if item not in weird_characters:
                            cleaned_list.append(item)

                    # The algorithm that actually builds a data set that we can actually use
                    # for meaningful data processing. It essentially builds up a hashmap for every state
                    # with all its population value
                    length_of_row = (len(cleaned_list) / 5)
                    start_index = 0
                    for index in range(0, int(length_of_row)):
                        total_population = str(cleaned_list[start_index])
                        start_index += 5

                        if state in states_and_population_data:
                            states_and_population_data[state].append(total_population)
                        else:
                            states_and_population_data[state] = [total_population]

                    lines.append(cleaned_list)
                    break

    sanitized_census_data = group_census_data_based_on_the_year(states_and_population_data)

    get_max_and_min_census_data_for_year(year, sanitized_census_data)


def main():
    user_input = input("Enter census year  1900  to  1990: ")

    if not user_input:
        print("Sorry but you must enter a valid input")
        return

    try:
        clean_up_data_set(int(user_input))
    except ValueError:
        print("Please enter all numbers")


if __name__ == '__main__':
    main()