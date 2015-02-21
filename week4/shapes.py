#!/usr/bin/env python
# Tawheed Raheem
# Practice of a computer programmer
# Assignment 4 - Shapes.py
# This program does the following:
# (a)draws a number of basic geometric shapes on the screen
# tabdulra@student.fitchburgstate.edu
# known bugs: none

import turtle

# Make drawing faster
turtle.speed(10)


turtle.up()
turtle.back(70)
turtle.down()

def triangle(size):
    for _ in range (3):
        turtle.forward(size)
        turtle. left(120)

def triangles():
    for size in range(10, 71, 20):
        triangle(size)


def square(size):
    for _ in range (4):
        turtle.forward(size)
        turtle.left(90)
        
        
def squares():
    for size in range(10, 71, 20):
        square(size)

def polygon(size, sides):
    turnAngle = 360 / sides
    for _ in range(sides):
        turtle.forward(size)
        turtle.left(turnAngle)

def heptagon():
    for size in range(10, 71, 20):
        polygon(size, 7)
        
def main():
    turtle.setup()
    turtle.color("red")
    triangles()
    turtle.color("green")
    turtle.up()
    turtle.forward(100)
    turtle.down() 
    squares()
    turtle.color("blue")
    turtle.up()
    turtle.forward(150)
    turtle.down() 
    heptagon()
    turtle.done()

main()