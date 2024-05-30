# produce graph for glove sales
from turtle import *

# set up gloves variables
Q1-2019 = 10
Q2-2019 = 8
Q3-2019 = 3
Q4-2019 = 5
Q1-2020 = 2
Q2-2020 = 8
Q3-2020 = 5
Q4-2020 = 7

# produce x axis
goto (400,0)

# produce y axis
goto (0,0)
goto (0,400)

# plot data
goto (0,0)
goto (20,Q1-2019 * 35)
goto (40,Q2-2019 * 35)
goto (60,Q3-2019 * 35)
goto (80,Q4-2019 * 35)
goto (110,Q1-2020 * 35)
goto (120,Q2-2020 * 35)
goto (140,Q3-2020 * 35)
goto (160,Q4-2020 * 35)

