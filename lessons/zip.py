"""Challenge Question 04 - Dict Function Writing"""

___author___ = "730566852"


def zip(str_list: list[str], int_list: list[int]) -> dict[str, int]:
    """Return dictionary assigning the keys the elements of first list and the values the elements of the second list"""
    combo_dict: dict[str, int] = {}
    i: int = 0

    if len(str_list) != len(int_list):  # if lists are different lengths
        return combo_dict
    
    if len(str_list) == 0 or len(int_list) == 0:  # if lists are empty
        return combo_dict
    
    while i < len(str_list):
        combo_dict[str_list[i]] = int_list[i]  # keys are assigned first list's elems and values are assigned second list's elems
        i += 1

    return combo_dict