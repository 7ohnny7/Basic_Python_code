# Problem: count how many days temperature was below zero
# initialise the temperature_list - (celsius)- [7 days]
temperature_list = [-3, -2 , -1, 0, 1, 2, 3]
# set a counter to zero
days = 0

# for each item in temperature_list :
for item in temperature_list :
    
    # if the item satisfies the condition :
    if item < 0 :
        
        # increment the counter, i.e. add 1 to it
        days = days + 1

# print the counter
print(days)

