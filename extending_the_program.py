# in the shell, enter the lines of code below (including the import)
# one after another.

""" Data analysis program 5
"""



import csv

file = open('happ_1.txt', 'r')
table =[]
reader = csv.reader(file)
for row in reader:
    table.append(row)
print(table)





# in the shell, enter the lines of code below (including the import)
# one after another.

# from table_utils import *

# table2 = rows(table, 1, 11)
# table3 = cols(table2, 1, 4)
# table4 = flip(table3)
# table5 = to_float(table4)
# print(table5)


# after inputting the code into shell
# The unwanted rows and columns will have been removed, the table flipped,
# and the values all converted to numbers.
