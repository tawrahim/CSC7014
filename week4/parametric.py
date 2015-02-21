#!/usr/bin/env python
# Tawheed Raheem
# Practice of a computer programmer
# Assignment 4
# This program does the following:
#     plots a parametric curve where the x and y
#     positions are derived from a single parameter
#     in an interesting way
# tabdulra@student.fitchburgstate.edu
# known bugs: none
import turtle
import math

turtle.speed(10)

def line(x1, y1, x2, y2):
    turtle.penup()
    turtle.goto (x1, y1)
    turtle.pendown()
    turtle.goto (x2, y2)
    turtle.penup()
    
def axes():
    line(-200, 0, 200, 0)
    line(0 , -200, 0, 200)

def plot():
    for scale in range(0, int(2*math.pi*1000), 10):
        turtle.penup()
            
        # Draw parametic shape
        
        turtle.penup()

def main():
    turtle.setup()
    turtle.up()
    turtle.color("blue")
    axes()
    turtle.color("red" )
    plot()
    turtle.done()

main ()
