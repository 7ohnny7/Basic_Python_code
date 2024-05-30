# Draw triangles with sides length 70,80,90 units. - using function deinitions 

from turtle import *

def draw_triangle_of_length(length):
    """Draw an equilateral triangle with sides of length units"""
    for sides in range(0,3):
        forward(length)
        left(120)

# Draw a triangle with sides of 70
draw_triangle_of_length(70)

# Move to position for second triangle
penup ()
forward (100)
pendown()

# Draw a triangle with sides of 80
draw_triangle_of_length(80)

# Move to position for third triangle
penup()
left (180)
forward (100)
right (90)
forward (100)
right (90)
pendown ()

# Draw a triangle with sides of 90
draw_triangle_of_length(90)
