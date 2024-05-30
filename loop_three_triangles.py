# Draw three equilateral triangles with sides of length 40 units - using a loop
from turtle import *

# Draw triangle, using a loop
for side in range(3) :
    forward(40)
    left(120)

# Move turtle to start of next triangle
penup()
forward(100)
pendown()

# Draw triangle, using a loop
for side in range(3) :
    forward(40)
    left(120)

# Move turtle to start of next triangle
penup()
left(180)
forward(100)
right(90)
forward(100)
right(90)
pendown()

# Draw triangle, using a loop

for side in range(3) :
    forward(40)
    left(120)

