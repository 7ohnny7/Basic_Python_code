# call using python shell, list_length([])
def list_length(a_list):
    """return the length of a list."""
    length = 0
    for item in a_list:
        length = length + 1
    return length
