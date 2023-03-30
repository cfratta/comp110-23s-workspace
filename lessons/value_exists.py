"""Practice question 18 Quiz 02"""

def value_exists (dict: dict[str, int], num: int) -> bool:
    for key in dict:
        if dict[key] == num:
            return True
    return False