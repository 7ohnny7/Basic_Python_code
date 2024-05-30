# (aggregation)
#problem: compute the sum of a list of numbers

# input: numbers (possibly empty list of numbers)
numbers_list = [2.0, 3.0, -2.5]


# output: initialise the aggregator with a suitable value
total = 0

# for each number in the list:
for item in numbers_list :
          
#    update the aggregator according to the value of the number
    total = total + item

print(total)
