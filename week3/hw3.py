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

# This dictionary contains the pattern of each digit
# A 100 signifies a tall bar whiles a 50 represents
# a short bar
map_of_postal_codes =  {
    0: [100, 100, 50, 50, 50],
    1: [50, 50, 50, 100, 100],
    2: [50, 50, 100, 50, 100],
    3: [50, 50, 100, 100, 50],
    4: [50, 100, 50, 50, 100],
    5: [50, 100, 50, 100, 50],
    6: [50, 100, 100, 50, 50],
    7: [100, 50, 50, 50, 100],
    8: [100, 50, 50, 100, 50],
    9: [100, 100, 50, 50, 50]
}

def drawBar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()             
    t.left(90)
    t.forward(height)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
    t.forward(70)           

def draw_postal_code():
    # Ask the user for postal code input
    # we are not doing rigrous error checking as we assume that the user would enter valid data
    user_input = input("Please enter a zip code in the format XXXXX-XXXX and it would drawn for you: ")

    maxheight = 500
    numbars = 150
    border = 5
    running_sum = 0
    tess = turtle.Turtle()
    wn = turtle.Screen() 
    wn.setworldcoordinates(0-border,0-border,40*numbars+border,maxheight+border)
    
    # draw the initial frame bar
    drawBar(tess, 100)
    
    for x in user_input:
        try:
            value_of_x = int(x)
            running_sum += value_of_x
            for i in map_of_postal_codes[value_of_x]:
                drawBar(tess,i)
        except:
            pass
    
    # calculate the check digit
    remainder = running_sum % 10
    
    # draw the check digit
    if remainder != 0:
        #print("Check digit is " + str(10 - remainder))
        for x in map_of_postal_codes[10 - remainder]:
            drawBar(tess, x)
        
        
    # draw the last frame bar
    drawBar(tess, 100)
    
    wn.exitonclick()

# Entry point of the program
if __name__ == "__main__":
    draw_postal_code()