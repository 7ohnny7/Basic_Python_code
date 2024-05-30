print(0)
def list_length(a_list):
    print(1)
    length = 0
    print(2)
    for item in a_list:
        print(3)
        length = length + 1
        print(4)
    return length
print(6)	
test_list = ['a', 'b']

print(7)
length_test_list = list_length(test_list)
print(8)
print('The list', test_list, 'contains', length_test_list, 'items.')
print(10)
