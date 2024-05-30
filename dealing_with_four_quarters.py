# Produce graph for glove sales
from turtle import *

# Set up gloves variables
gloves1 = 10
gloves2 = 8
gloves3 = 3
gloves4 = 5

# Produce x axis
goto(80,0)

# Produce y axis
goto(0,0)
goto(0,100)

# Plot data
goto(0,0)
goto(20,gloves1 * 10)
goto(40,gloves2 * 10)
goto(60,gloves3 * 10)
goto(80,gloves4 * 10)

# create a list to use with a loop

# list
gloves =[10,8,3,5]

# loop
total = 0
for index in range(0, len(gloves)):
    total = total + gloves [index] 
