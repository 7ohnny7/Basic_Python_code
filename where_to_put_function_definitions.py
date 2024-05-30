# function definition error example
test_list = ['a', 'b']

length_test_list = list_length(test_list)

print('The list', test_list, 'contains', length_test_list, 'items.')

def list_length(a_list):
    length = 0
    for item in a_list:
        length = length + 1
    return length


