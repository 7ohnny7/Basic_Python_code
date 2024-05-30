# Generate the monthly outstanding mortgage

# Input: annual interest rate, a floating-point percentage
rate = 4.98

# Input: monthly payment, a positive integer in a currency
payment = 1023.10

# Input/Output: mortgage, a positive number, same currency
mortgage = 185000.00

# Output: list of monthly outstanding mortgage amounts
outstanding = []

outstanding = outstanding + [mortgage]


while(mortgage > 0):
    interest = mortgage * rate / 12
    mortgage = mortgage + interest - payment
   
    outstanding = outstanding + [mortgage]

print('Outstanding mortgage, month by month:' , outstanding)
