#!/usr/bin/env python
# Tawheed Raheem
# Practice of a computer programmer
# Homework 3
# This program uses the python module to print
# zip code
# tabdulra@student.fitchburgstate.edu
# known bugs: None

import turtle
import numbers

map_of_postal_codes =  {
    0: [200, 200, 100, 100, 100],
    1: [100, 100, 100, 200, 200],
    2: [100, 100, 200, 100, 200],
    3: [100, 100, 200, 200, 100],
    4: [100, 200, 100, 100, 200],
    5: [100, 200, 100, 200, 100],
    6: [100, 200, 200, 100, 100],
    7: [200, 100, 100, 100, 200],
    8: [200, 100, 100, 200, 100],
    9: [200, 200, 100, 100, 100]
}

def draw_postal_code():
    # we are not doing any error checking as we assume that the user would enter valid data
    user_input = raw_input("Please enter a zip code in the format XXXXX-XXXX and it would drawn for you: ")

    for x in user_input:
        try:
            value_of_x = int(x)
            print(map_of_postal_codes[value_of_x])
        except:
            print(False)

def drawBar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()               # start filling this shape
    t.left(90)
    t.forward(height)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()                 # stop filling this shape

def fillColor(t,height):
    drawBar(t,height)
    if height >=200:
        t.fillcolor("red")
    elif height >= 100 and height < 200:
        t.fillcolor("yellow")
    else:
        t.fillcolor("green")

xs = [48,117,200,700,220, 48,117,200,240,220, 48,117,200,240,220, 48,117,200,240,220, 48,117,200,240,220]  # here is the data
maxheight = max(xs)
numbars = len(xs)
border = 5

'''
tess = turtle.Turtle()           # create tess and set some attributes

wn = turtle.Screen()             # Set up the window and its attributes
wn.setworldcoordinates(0-border,0-border,40*numbars+border,maxheight+border)

screen = turtle.Screen()
move_factor = 2
for i in xs:
    fillColor(tess,i)


wn.exitonclick()
'''
# Entry point of the program
if __name__ == "__main__":
    draw_postal_code()
