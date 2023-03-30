"""Practice question 19 Quiz 02"""

def short_words(list: list[str]) -> list[str]:
    new_list: list[str] = []
    for item in list:
        if len(item) < 5:
            new_list.append(item)
        elif len(item) >= 5:
            print(f"{item} is too long!")
    return new_list