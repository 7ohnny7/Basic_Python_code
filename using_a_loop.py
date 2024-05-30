# produce graph for glove sales - using a loop with the turtle
from turtle import *

# sales data input list
gloves = [10, 8, 3, 5, 9, 11, 5, 6, 10, 7, 5, 7]


# loop
total = 0
for index in range (0, len(gloves)):
    total = total + gloves [index]

# produce x axis
goto (250,0)

# produce y axis
goto (0,0)
goto (0,125)

# plot data
goto (0,0)

# plot data loop 
for index in range (0, len(gloves)):
    goto (20 + (20 * index), gloves[index] * 10)

print (gloves)
