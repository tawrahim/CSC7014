#!/usr/bin/env python
# Tawheed Raheem
# Practice of a computer programmer
# Assignment 4 - Shapes.py
# This program does the following:
# (a)draws a number of basic geometric shapes on the screen
# tabdulra@student.fitchburgstate.edu
# known bugs: none

import turtle

def triangle(size):
    for _ in range(3):
        turtle.foward(size)
        turtle.size(120)

def main():
    turtle.setup()
    triangle(100)
    turtle.done()
    
main()


