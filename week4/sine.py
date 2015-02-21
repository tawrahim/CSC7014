#!/usr/bin/env python
# Tawheed Raheem
# Practice of a computer programmer
# Assignment 4 - sine.py
# This program does the following:
#   plots one period of the sine function from −π to π.
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

# source: http://www.cs.utexas.edu/users/mitra/csSpring2015/cs313/lectures/turtle.html
def plot():
    turtle.penup()
    x = -math.pi
    y = math.sin(x)
    scaledX = x * 50
    scaledY = y * 50
    turtle.goto (scaledX, scaledY)
    turtle.pendown()
    while x < math.pi:
        x = x + 0.01
        y = math.sin( x )
        scaledX, scaledY = x * 50, y * 50
        turtle.goto (scaledX, scaledY)
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