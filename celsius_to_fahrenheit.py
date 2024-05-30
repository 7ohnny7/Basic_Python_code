# list transformation
# Set celsius_temp to -99.9 to 99.9 degrees (floating-point)

celsius_temp_list = [-20, -10, -5]

# Set fahrenheit_list to an empty list

fahrenheit_list = []

#   transform the celsius_value into a fahrenheit_value

for position in celsius_temp_list:
    position = (position * 1.8) + 32 


#   append the fahrenheit_value to the fahrenheit_list

    fahrenheit_list = fahrenheit_list + [position]
 
# Print the fahrenheit_list

print(fahrenheit_list)
