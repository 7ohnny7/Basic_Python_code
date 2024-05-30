# Triangle with choice of length
from turtle import *

def draw_triangle_of_size(length):
    """Draw an equilateral triangle with sides of length length"""
    for sides in range(0,3):
        forward(length)
        left(120)
    return length

# write the code below in the shell 

draw_triangle_of_size(70)
draw_triangle_of_size(80)
draw_triangle_of_size(90)
