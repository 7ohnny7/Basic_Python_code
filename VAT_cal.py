from decimal import *

# Enter wholesale price
item = Decimal(1249.99)

# Tax at a 20% rate
rate = Decimal(0.20)

tax = item * rate
total = item + tax


print('Price:\t', '%.2f' % item)
print('VAT:\t', f'{tax:.2f}')
print('Total price (incl. VAT):\t', f'{total:.2f}')
