# set up gloves variables
gloves1 = 10
gloves2 = 8
gloves3 = 3
gloves4 = 5

# add variables together and print total - (example 1)
total = (gloves1 + gloves2 + gloves3 + gloves4)

print (total)



# sales data put into list and print total - (example 2)
gloves = [10,8,3,5]
total = gloves[0] + gloves[1] + gloves[2] + gloves[3] 

print (total)




# loop which gets executed with values for index of 0,1,2 and 3 - (example 3)
gloves = [10,8,3,5]
total = 0
for index in range (0, len(gloves)):
    total = total + gloves [index]

print (total)


