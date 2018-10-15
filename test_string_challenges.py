def linear_search(random_list, val):
    """ Returns the index of a value 'val' if found in a random list using linear search algorithm """
    index = 0
    while index < len(random_list):
        if random_list[index] == val:
            return index
        index += 1
    return None


def test_linear_search_text():
    my_list = [1, "a", 20]
    assert linear_search(my_list, "a") == 1


def test_linear_search_number():
    my_list = [1, "a", 20]
    assert linear_search(my_list, 20) == 2


def test_linear_search_not_found():
    my_list = [1, "a", 20]
    assert linear_search(my_list, 0) is None
