def test_list_length():
    """test the list_length() function"""
    assert list_length([]) == 0

    assert list_length([1]) == 1
    assert list_length([1,1]) == 2
    assert list_length([1,1,3]) == 3	

    test_list_length()
