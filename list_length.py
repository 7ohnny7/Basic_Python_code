# Problem: compute the length of a list

# Input: a (possibly empty) list of items
items = [0, 1, 2, 3, 4, 5, 6]

# Output: the length of list, i.e. how many items it has
length = 0
for item in items:
    length = length + 1

print('The length of', items, 'is', length)
