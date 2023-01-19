"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730566852"

user_word: str = input("Enter a 5-character word: ")

if (len(user_word) != 5):
    print("Error: Word must contain 5 characters")
    exit()

user_letter: str = input("Enter a single character: ")

if (len(user_letter) != 1):
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + user_letter + " in " + user_word)

count_matching_chr: int = 0
if (user_word[0] == user_letter):
    print(user_letter + " found at index 0")
    count_matching_chr = count_matching_chr + 1
if (user_word[1] == user_letter):
    print(user_letter + " found at index 1")
    count_matching_chr = count_matching_chr + 1
if (user_word[2] == user_letter):
    print(user_letter + " found at index 2")
    count_matching_chr = count_matching_chr + 1
if (user_word[3] == user_letter):
    print(user_letter + " found at index 3")
    count_matching_chr = count_matching_chr + 1
if (user_word[4] == user_letter):
    print(user_letter + " found at index 4")
    count_matching_chr = count_matching_chr + 1

if(count_matching_chr > 0):
    print(str(count_matching_chr) + " instances of " + user_letter + " in " + user_word)
else:
    print("No instances of " + user_letter + " found in " + user_word)


"""My code progression at each part"""
"""For documentation purposes only"""
"""Part 1. Prompting for Inputs - 20 Points"""
"""
user_word: str = input("Enter a 5-character word: ")
user_letter: str = input("Enter a single character: ")
print("Searching for " + user_letter + " in " + user_word)
"""

"""Part 2. Checking Indices for Matches - 20 Points"""
"""
if (user_word[0] == user_letter):
    print(user_letter + " found at index 0")
if (user_word[1] == user_letter):
    print(user_letter + " found at index 1")
if (user_word[2] == user_letter):
    print(user_letter + " found at index 2")
if (user_word[3] == user_letter):
    print(user_letter + " found at index 3")
if (user_word[4] == user_letter):
    print(user_letter + " found at index 4")
"""

"""Part 3. Counting Matching Indices - 30 Points"""
"""
count_matching_chr: int = 0
if (user_word[0] == user_letter):
    print(user_letter + " found at index 0")
    count_matching_chr = count_matching_chr + 1
if (user_word[1] == user_letter):
    print(user_letter + " found at index 1")
    count_matching_chr = count_matching_chr + 1
if (user_word[2] == user_letter):
    print(user_letter + " found at index 2")
    count_matching_chr = count_matching_chr + 1
if (user_word[3] == user_letter):
    print(user_letter + " found at index 3")
    count_matching_chr = count_matching_chr + 1
if (user_word[4] == user_letter):
    print(user_letter + " found at index 4")
    count_matching_chr = count_matching_chr + 1

if(count_matching_chr > 0):
    print(str(count_matching_chr) + " instances of " + user_letter + " in " + user_word)
else:
    print("No instances of " + user_letter + " found in " + user_word)
"""

"""Part 4. Exiting Early for Invalid Inputs - 10 points"""
""" I just changed the Part 1 section
user_word: str = input("Enter a 5-character word: ")

if (len(user_word) != 5):
    print("Error: Word must contain 5 characters")
    exit()

user_letter: str = input("Enter a single character: ")

if (len(user_letter) != 1):
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + user_letter + " in " + user_word
"""