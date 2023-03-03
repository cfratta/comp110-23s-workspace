"""EX05 - `list` Utility Functions"""

__author__ = "730566852"


def only_evens(xs: list[int]) -> list[int]:
    """Return even elements of an integer list"""
    even: list[int] = []
    for elem in xs:
        if elem % 2 == 0:  # check if even number
            even.append(elem)
    return even


def concat(list1: list[int], list2: list[int]) -> list[int]:
    """Concatinate two integer lists"""
    concated: list[int] = []
    for elem in list1:  # add all of the elements of the first list to new list
        concated.append(elem)
    for elem in list2:  # add all of the elements of the second list to the new list, right after first list
        concated.append(elem)
    return concated


def sub(xs: list[int], start: int, stop: int) -> list[int]:
    """Return a new list based on given indexes on old list"""
    sub_list: list[int] = []
    for idx in range(start, stop):  # go through each element in given index range
        sub_list.append(xs[idx])
    return sub_list