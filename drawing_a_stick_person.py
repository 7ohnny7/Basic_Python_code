# Draw a stickman
from turtle import *

# Draw a square for a head
for side in range (1, 5):
    forward(40)
    right(90)

# Move to start of next part (torso)
penup()
forward(20)
right(90)
forward(40)
pendown()

# Draw a line for (torso)
forward(120)

# Draw a line for (right leg)
right(45)
forward(70)

# Move to start next part (left leg)
penup()
right(180)
forward(70)
right(90)
pendown()

# Draw a line for (left leg)
forward(70)

# Move to start next part (left arm)
penup()
right(180)
forward(70)
right(45)
forward(60)
right(120)
pendown()

# Draw a line for (left arm)
forward(45)
right(180)

# Move to start next part (right arm)
penup()
forward(45)
left(60)
pendown()

# Draw a line for (right arm)
forward(45)

