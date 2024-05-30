""" Data analysis program 14
"""


from table_utils import *

# Load geog_1.txt data into table0
table1 = load('geog_1.txt')

# Add code here to output the name of the authority
# that the greatest percentage people in this "Very High" category (column 7).

table2 = filter_by('K02', 0, table1)

table3 = sort_by(7,to_float(table2))

print(table3)





