# Compute module grade

# initialise marks to a list of 4 integers from 0 to 100
marks = [39, 38, 40, 0]

# Determine the lowest of the 4 marks (retrieval: find best)
lowest = marks[0]

# Compute the mean of the best 3 marks (aggregation problem)
for grade in marks:
    if grade < lowest :
        lowest = grade

total = 0

# Compute the sum of the 4 marks (aggregation problem)
for grade in marks:

    total = total + grade

# Subtract the lowest mark (formula problem)
total = total - lowest

# Divide the result by 3 (formula problem)
mean = total / 3

# Compute the grade for that mean (case analysis)
if mean < 30 :

    mark = 'fail'

elif mean < 40:

        mark = 'resit'

else:

    mark = 'pass'

print(mark)

