"""EX07 - Dictionary Functions."""

__author__ = "730566852"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Invert the keys and values in a dictionary."""
    invert: dict[str, str] = {}

    for key in input:
        
        if input[key] in invert:  # check if key already exists in new dictionary.
            raise KeyError("Key already in dictionary!")
        
        invert[input[key]] = key

    return invert


def favorite_color(input: dict[str, str]) -> str:
    """Return which color appears the most often in a given dictionary."""
    fav: str = ""
    poll: dict[str, int] = {}
    i: int = 0

    for key in input:
        if input[key] in poll:  # color appears another time, increment value by one in poll.
            poll[input[key]] += 1
        
        else:  # if new color, add new key:value pair to poll.
            poll[input[key]] = 1

    for key in poll:

        if i == 0:  # check first key in poll.
            fav = key
            i += 1

        if poll[fav] < poll[key]:  # check for highest value number for most common color.
            fav = key
    return fav


def count(input: list[str]) -> dict[str, int]:
    """Create a dictionary that tracks how many times each elements appeared in a given list."""
    counter: dict[str, int] = {}

    for elem in input:
        if elem in counter:  # if list item already exists, increase the value in the dictionary by one.
            counter[elem] += 1
        else:
            counter[elem] = 1  # if the item is new, create a new key:value pair and set it to one.
    return counter