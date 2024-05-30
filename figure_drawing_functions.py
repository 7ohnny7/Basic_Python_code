# figure_drawing_functions

from turtle import *

# Triangle
def draw_triangle():
    """Draw an equilateral triangle with sides of length 40 units"""
    for sides in range(0,3):
        forward(40)
        left(120)

# Triangle with choice of length
from turtle import *

def draw_triangle_of_length(length):
    """Draw an equilateral triangle with sides of length units"""
    for sides in range(0,3):
        forward(length)
        left(120)
    return length

# function for conversion from Celsius to Fahrenheit

def fahrenheit(celsius):
    """Convert degrees Celsius to Fahrenheit"""
    return ((9 * celsius) / 5) + 32
