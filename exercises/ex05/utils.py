"""EX05 - `list` Utility Functions."""

__author__ = "730566852"


def only_evens(xs: list[int]) -> list[int]:
    """Return even elements of an integer list."""
    even: list[int] = list()
    for elem in xs:
        if elem % 2 == 0:  # check if even number
            even.append(elem)
    return even


def concat(list1: list[int], list2: list[int]) -> list[int]:
    """Concatinate two integer lists."""
    concated: list[int] = list()
    for elem in list1:  # add all of the elements of the first list to new list
        concated.append(elem)
    for elem in list2:  # add all of the elements of the second list to the new list, right after first list
        concated.append(elem)
    return concated


def sub(xs: list[int], start: int, stop: int) -> list[int]:
    """Return a new list based on given indexes on old list."""
    sub_list: list[int] = list()
    
    if start < 0:  # start is a negative number
        start = 0
            
    if stop > len(xs):  # stop is greater than the length of the list
        stop = len(xs)
    
    if len(xs) == 0 or start >= len(xs) or stop <= 0:  # start is >= length of the list, or the end is at most 0, return the empty list
        return sub_list
    
    for idx in range(start, stop):  # go through each element in given index range
        sub_list.append(xs[idx])
    return sub_list