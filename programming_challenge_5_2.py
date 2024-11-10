'''
Author: Abigail Michael
Date: 6 November 2024
Task: Programming Challenge 5, Part I: Drawinig Regular Polygons via Trigonometric Functions
'''

from turtle import *
import math
import random

# set up drawing screen
width = 800
height = 800
setup(width,height)
setworldcoordinates(-2,-2,2,2)

# assign radius
radius = 0.9

# Acquire user input for number of sides
number_of_sides = int(input("Enter the number of sides of a polygon: "))

# sentinel loop to calculate variables and draw a polygon
while (number_of_sides>0):
    if (number_of_sides>2):
        # establishing color
        r = random.uniform(0.0,1.0)
        g = random.uniform(0.0,1.0)
        b = random.uniform(0.0,1.0)
        pencolor(r,g,b)
        # Calculate theta
        theta = 360/number_of_sides
        # calculate side length
        side_length = 2*radius*math.sin(math.radians(theta/2.0))
        # position turtle and starting angle
        start_x,start_y = 0, -radius
        penup()
        setpos(start_x,start_y)
        right(theta/2.0)
        # Draw polygon by iterating through number of sides
        pendown()
        for _ in range(0, number_of_sides):
            left(theta)
            forward(side_length)
        penup()
        left(theta/2.0)

    else:
        print("Polygon can be drawn with number of sides greater than 2")
        break

    number_of_sides = int(input("Enter the number of sides of a polygon: "))

print("Program Terminated")