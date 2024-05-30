# Draw a house
from turtle import *

# Draw a triangle (Roof)
for side in range(3) :
    forward(90)
    left(120)

# Change orientation
right(90)

# Draw a square (front of house)
for side in range(4):
    forward(90)
    left(90)

# change position                        
penup()
forward(90)
left(90)
forward(10)
left(90)
pendown()

# Draw a rectangle (door)
forward(40)
right(90)
forward(25)
right(90)
forward(40)

# change position                        
penup()
left(90)
forward(10)
left(90)
forward(45)
pendown()

# Draw a Square (window)
for side in range(4):
    forward(35)
    right(90)
