# Generate a pseudo-random sequence integers

# Input: first number, an integer from 0 to 7 inclusive
seed = 7
print(seed)

number = (seed * 9 + 5) % 8
print(number)
while number != seed:
    number = (number * 9 + 5) % 8
    print(number)





# The termination condition is when the generated value is equal to the seed.
# Since the first value in the sequence is the seed, the loop would immediately
# terminate and no further number generated.
# I must therefore generate and print the second number before the loop.
# In other words, because the sequence should stop when the seed appears again,
# it means that the sequence has at least two numbers, and I must generate them before the loop.
# The problem statement says explicitly that the seed is not negative, so the smallest input value is 0.
# To see if there is a highest value, I note that all numbers in the sequence are from 0 to 7.
# fact, the remainder of dividing by C is always a number from 0 to C-1, with C=8 in this problem.
# So, if the seed starts with a value of C or higher, none of the generated numbers
# will ever be the same as the seed and the loop won’t terminate.
