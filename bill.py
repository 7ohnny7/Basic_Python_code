# Compute total bill for given party size

# Input: the bill, in any currency, before any surcharges
bill = 65

# Input: the people in the party, a positive integer
people = 7

# Input: the service charge, a percentage
charge = .10

# Output: the total bill, in the same currency
if people > 6:
    total = bill + bill * charge
else:
    total = bill

print('The total bill is', total)
