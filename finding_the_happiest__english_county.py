

""" Data analysis program 10
"""



from table_utils import *

# Load geog_1.txt data into table1
table1 = load('geog_1.txt')


table2 = filter_by('E10', 0, table1)

table3 = sort_by(8,to_float(table2))

print(table3)

