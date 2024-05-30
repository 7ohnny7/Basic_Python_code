#find best value
# Problem: find the lowest temperature of the week

# Input: a list of 7 numbers
temperatures = [5, 0, -3, 7, 8, 5, 0]

# Output: coldest, the lowest value in temperatures
best_position = 0

for position in temperatures:
    if position < best_position:
        best_position = position

print('The lowest of', temperatures, 'is', best_position)
