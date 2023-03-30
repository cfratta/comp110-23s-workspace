"""Practice question 17 for Quiz 02"""

def odd_and_even (list: list[int]) -> list[int]:
    new_list: list[int] = []
    i: int = 0

    while i < len(list):
        if i % 2 == 0 and list[i] % 2 == 1:
            new_list.append(list[i])
        i += 1
    return new_list

print(odd_and_even ([2 ,3 ,4 ,5]))
print(odd_and_even ([7 , 8 , 10 , 10 , 5 , 12 , 3 , 2 , 11 , 8]))