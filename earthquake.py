# initialise the input values
magnitude = float(input('please enter richter scale readings')) 
# if input values fall into the first case:
#     compute outputs according to the first case
if magnitude < 4.0:
    output = 'That is a minor earthquake.'
# otherwise if inputs fall into the second case:
#     compute outputs according to the second case
elif magnitude >= 4.0 and magnitude < 6.0:
    output = 'That is a moderate earthquake.'
# otherwise if input falls into third case:
#     compute outputs according to the third case
elif magnitude >= 6.0 and magnitude < 7.0:
    output = 'That is a strong earthquake.'
# otherwise if input falls into forth case:
#     compute outputs according to the forth case
elif magnitude >= 7.0 and magnitude < 8.0:
    output = 'That is a major earthquake.'
# otherwise:
#	 compute outputs according to the last case
else:
    output = 'That is a great earthquake.'
# print the outputs
print (output)




