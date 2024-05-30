# A list of lists
table = [[9, 27, 26, 19, 12, 7],
         [4, 21, 30, 25, 18, 2]]

# finding the avarage (mean) of each row - using a loop
for row in table:
    numbers = row 

# nested loop 
    total = 0 
    for rating in range(6):
        product = rating * numbers[rating]
        total = total + product
    average = total / 100 
    print('average rating =', average)

