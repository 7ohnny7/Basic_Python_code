""" Data analysis program 6
"""

import csv

file = open('happ_1.txt', 'r')
table =[]
reader = csv.reader(file)
for row in reader:
    table.append(row)

from table_utils import *

table2 = rows(table, 1, 11)
table3 = cols(table2, 1, 4)
table4 = flip(table3)
table5 = to_float(table4)
print(table5)


for row in table5:
    numbers = row 
    total = 0 
    for rating in range(11):
        product = rating * numbers[rating]
        total = total + product
    average = total / 100 
    print('average rating =', average)

# Happiness seems to be increasing slightly!
# Our figures agree with those from the ONS, except some of them are displayed
# to a meaningless number of decimal places.
# In the next activity you will do something about this.
