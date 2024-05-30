""" Data analysis program 9
"""

def median(alist):
    """ Calculates the median of a list of numbers.
The list must not be empty.
"""

    number_of_values = len(alist)
    sorted_list = sorted(alist)

    # Two cases, depending on whether the number of values is odd or even.
    quotient = number_of_values // 2
    remainder = number_of_values % 2
 
    if (remainder == 1):
        result = sorted_list[quotient]
    else:
        result = (sorted_list[quotient - 1] + sorted_list[quotient]) / 2
    return result
        
    
def test_median():
    assert median([2]) == 2
    assert median([4, 3]) == 3.5
    assert median([3, 1, 8, 4, 7, 6, 4, 2, 5, 9]) == 4.5
    assert median([7, 2, 6, 2, 5, 3, 1, 0, 8, 6, 6, 4, 9]) == 5

test_median()


    
# Note that the function test_median() is an example of the automated
# testing introduced in Block 2 Part 4. The function contains a series
# of assert statements that check the results are as expected,
# and providing that is the case, nothing happens.
# Only if a result was wrong would we see output,
# in the form of an error message.
