"""EX04 - Utils!"""

__author__ = "730566852"


def all(given_list: list[int], given_int: int) -> bool:
    """Check if all the items in an integer list are equal to the given integer."""
    assert len(given_list) > 0  # check if list isn't empty
    idx: int = 0

    while idx < len(given_list):  # go through each item in the list
        if given_int != given_list[idx]:  # if given integer isn't the same as the item in the list
            return False
        idx += 1
    return True  # if given integer is equal to each item in the list


def max(input: list[int]) -> int:
    """Find and return the max integer in a list."""
    if len(input) == 0:  # empty list
        raise ValueError("max() arg is an empty List")
    
    max_int: int = input[0]  # start with assuming that the first item in the list in the max item / will compare against that
    idx: int = 0

    while idx < len(input) - 1:  # check the item at each index in the list
        if max_int < input[idx]:  # if current max int is actually less than another item in the list
            max_int = input[idx]
        idx += 1  # if current max int is still the max int
    return max_int


def is_equal(first_list: list[int], second_list: list[int]) -> bool:
    """Check if two lists are identical to each other, both with items and item orders, i.e. deep equality."""
    idx: int = 0

    assert len(first_list) > 0  # check for not an empty list
    assert len(second_list) > 0  # check for not an empty list
    assert len(first_list) == len(second_list)  # check that both lists are the same length

    while idx < len(first_list) and idx < len(second_list):  # quit if you run out of items to compare
        if first_list[idx] != second_list[idx]:  # item at one index is not the same as the item at the corresponding index in the other list
            return False
        idx += 1
    return True