# Generate the monthly outstanding mortgage



# Input: annual interest rate, a floating-point percentage

rate = 0.0874

percentage = '{:.0%}'.format(rate)




# Input: monthly payment, a positive integer in a currency

payment = 468.45


# Input/Output: mortgage, a positive number, same currency

mortgage = 41026.04

print('Outstanding mortgage:\t', round(mortgage, 2))

while not (mortgage == 0 or mortgage < 0):
    interest = mortgage * rate // 12
    mortgage = mortgage + interest - payment
    print('Outstanding mortgage:\t', round(mortgage, 2))


print(percentage)

print(rate)
