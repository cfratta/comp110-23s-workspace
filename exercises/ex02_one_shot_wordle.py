"""EX02 - One-Shot Wordle - Loops!"""

__author__ = "730566852"

SECRET: str = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
guess: str = input(f"What is your {len(SECRET)}-letter guess? ")  # person guesses the word
i: int = 0
emoji_guess: str = ""


while len(guess) != len(SECRET):  # word length is too short or too long
    guess = input(f"That was not {len(SECRET)} letters! Try again: ")

while i < len(SECRET):  # check each letter of guess for matches
    if guess[i] == SECRET[i]:  # guess letter is correct and in the right spot compared to SECRET
        emoji_guess = emoji_guess + GREEN_BOX
    else:  # check for correct letter, incorrect spot or incorrect letter
        chr_exist: bool = False
        i_exist: int = 0
        while chr_exist is not True and i_exist < len(SECRET):
            if guess[i] == SECRET[i_exist]:
                chr_exist = True
            else:
                i_exist = i_exist + 1
        if chr_exist is True:  # correct letter, incorrect spot
            emoji_guess = emoji_guess + YELLOW_BOX
        else:  # incorrect letter
            emoji_guess = emoji_guess + WHITE_BOX
    i = i + 1

if guess == SECRET:  # correct guess of word SECRET
    print(emoji_guess)
    print("Woo! You got it!")
else:  # guess word is incorrect
    print(emoji_guess)
    print("Not quite. Play again soon!")