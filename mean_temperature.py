# problem: compute the mean of daily temperatures

# problem: add the numbers in the list together (aggregation problem)
# input: numbers (possibly empty list of numbers)
daily_temp = [-2, -2, -2, 2, 2, 2]


# output: initialise the aggregator with a suitable value
total = 0

# for each number in the list:
for item in daily_temp :
          
#    update the aggregator according to the value of the number
    total = total + item




# Problem: compute the length of a list (counting problem)
# Input: daily_temp = [20, 30, 22, 28]


# Output: the length of list, i.e. how many items it has
length = 0
for item in daily_temp:
    length = length + 1



# problem: divide total by the length of the list (formula problem)

#input: Mean formula
mean = total / length

print(mean)







