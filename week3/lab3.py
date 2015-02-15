#!/usr/bin/env python
# Tawheed Raheem
# Practice of a computer programmer
# Lab 3
# tabdulra@student.fitchburgstate.edu
# The program does ...
# known bugs: None

import turtle
import numbers
import time

# Print title 
print("This program draws squares of many colors. \n")

# function to display messages on bad input
def display_retry_message():
    print("The number must be an integer and at least 1.")
    print("Please try again \n")

# prompt before starting to draw
# We must make sure that the user provides a valid input
invalid_user_input = True
number_of_squares = 0
while invalid_user_input:
    try:
        number_of_squares = int(input("Enter the number of squares to draw: "))
        if number_of_squares < 1: display_retry_message()
        if (isinstance(number_of_squares, numbers.Integral) and number_of_squares > 0):
            invalid_user_input = False
    except ValueError:
        display_retry_message()

# Draw the circles
for x in range(number_of_squares):
    print("dd")

def draw_rectangle(x, y, w, h, pen, color):
    """draw a rectangle"""
    pen.fillcolor(color)
    pen.setheading(0)
    pen.up()
    pen.goto(x, y)
    pen.down()
    pen.begin_fill()
    pen.goto(x+w,y)
    pen.goto(x+w,y+h)
    pen.goto(x,y+h)
    pen.goto(x,y)
    pen.end_fill()
    
draw_rectangle(-100, 0, 50, 80, turtle, 'green')    
draw_rectangle(-105, 5, 55, 85, turtle, 'yellow')    

# let's pause for 5 seconds
time.sleep(50)

turtle.bye()
