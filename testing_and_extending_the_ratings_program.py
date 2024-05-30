#getting the avarage (mean) of a products star rating

# Book A
numbers = [9, 27, 26, 19, 12, 7]
total = 0
for rating in range(6):
   product = rating * numbers[rating]
   total = total + product
average = total / 100
print('average rating =', average)

# Book B
numbers = [4, 21, 30, 25, 18, 2]
total = 0
for rating in range(6):
   product = rating * numbers[rating]
   total = total + product
average = total / 100
print('average rating =', average)


