#!/usr/bin/env python
# Tawheed Raheem
# Practice of a computer programmer
# Homework 12
# tabdulra@student.fitchburgstate.edu
#
# This program checks the imdb database and reports information
# about what actors are in common in two movies
# Also given an actor it finds all the actors with whom he or she has acted
#
#
# known bugs: None

movies_dictionary = {}


def process_line(line):
    words_in_line = line.lower().split(",")
    movies_titles = words_in_line[1:]
    actor_name = words_in_line[0]
    for movie in movies_titles:
        add_movie(movie.lstrip(), actor_name)


def add_movie(key, value):
    if key in movies_dictionary:
        movies_dictionary[key].append(value)
    else:
        movies_dictionary[key] = [value]


def build_data_set():
    data_file = open("imdb_Data.txt", "r")
    for line in data_file:
        process_line(line.rstrip())


def main():
    build_data_set()

    print("Welcome to the movie lookup database")
    print("Please enter exit at anytime to quit the program e.g Meet Joe Black (1998)")

    while True:
        user_input_1 = input("Enter name of movie 1 (e.g Meet Joe Black (1998)): ")

        while not user_input_1:
            user_input_1 = input("Enter name of movie 1 (e.g Meet Joe Black (1998)): ")
        if user_input_1 == "exit":
            print("Good bye!")
            return

        user_input_2 = input("Enter name of movie 2 (e.g Meet Joe Black (1998)): ")
        while not user_input_2:
            user_input_2 = input("Enter name of movie 2 (e.g Meet Joe Black (1998)): ")

        if user_input_2 == "exit":
            print("Good bye!")
            return

        print()
        movie_1 = user_input_1.lower()
        movie_2 = user_input_2.lower()

        if movie_1 not in movies_dictionary and movie_2 not in movies_dictionary:
            print("The movies you entered does not exists")
            continue

        # Find all the actors in those movies
        movie_1_set = set()
        movie_2_set = set()
        for movie in movies_dictionary[movie_1]:
            movie_1_set.add(movie)

        for movie in movies_dictionary[movie_2]:
            movie_2_set.add(movie)

        print("All the actors in both movies")
        for actor in movie_1_set:
            print(actor)
        for actor in movie_2_set:
            print(actor)
        print()

        # Find the common actors in the two movies
        print("All actors common in the two movies")
        for actor in movie_1_set.intersection(movie_2_set):
            print(actor)
        print()

        # Find the actors who are in either of the movies but not both (use symmetric difference)
        print("All actors who are in either of the movies but not both")
        for actor in movie_1_set.symmetric_difference(movie_2_set):
            print(actor)
        print()

        # Given the actor’s name, find all the actors with whom he or she has acted
        print("Given an actor’s name, we want to find all the actors with whom he or she has acted")
        entered_actor_name = input("Please enter the name of an actor: ")

        while not entered_actor_name:
            entered_actor_name = input("Please enter the name of an actor: ")

        print(entered_actor_name + " has acted movies with the following other actors")
        for movie in movies_dictionary:
            actors = movies_dictionary[movie]
            if entered_actor_name.lower() in actors:
                for x in actors:
                    if x.lower() != entered_actor_name.lower():
                        print(x)

        print()
        print()

        if entered_actor_name == "exit":
            return

if __name__ == '__main__':
    main()