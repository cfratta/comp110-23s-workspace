"""EX03 - Structured Wordle"""

__author__ = "730566852"

def main() -> None:
    """The entrypoint of the program and main game loop."""
    SECRET: str = "codes"
    track_turns: int = 1
    user_won: bool = False

    while track_turns < 7 and user_won == False:  # check if user has guessed correct word, or didn't but still have tries left
        print(f"=== Turn {track_turns}/6 ===")
        user_guess = input_guess(len(SECRET))
        print(emojified(user_guess, SECRET))

        if user_guess == SECRET:  # user guessed correct word (and didn't run out of turns)
            user_won = True
            print(f"You won in {track_turns}/6 turns!")
        if user_guess != SECRET and user_won == False:  # user didn't guess correct word but still have turns left to try
            track_turns = track_turns + 1
   
    if user_won == False: # user didn't guess correct word and out of turns -- user lost
        print("X/6 - Sorry, try again tomorrow!")   
    
def contains_char(search_str: str, check_char: str) -> bool:
    """Check (True or False) if character is in string"""
    assert len(check_char) == 1
    idx: int = 0
    result: bool = False
    
    while idx < len(search_str): #go through each character in the word to check for character
        if search_str[idx] == check_char:
            result = True
        idx = idx + 1
    return result

def emojified(guess: str, secret: str) -> str:
    """Given two strings of equal length, use contains_char to compare strings and return a string of emojies like Wordle"""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emoji_guess: str = ""
    idx: int = 0

    while idx < len(secret):
        if guess[idx] == secret[idx]:  # correct letter, correct spot
            emoji_guess = emoji_guess + GREEN_BOX
            idx = idx + 1
        elif contains_char(secret, guess[idx]):  # correct letter, incorrect spot
            emoji_guess = emoji_guess + YELLOW_BOX
            idx = idx + 1
        else:  # incorrect letter
            emoji_guess = emoji_guess + WHITE_BOX
            idx = idx + 1
    return emoji_guess

def input_guess(expected_len: int) -> str:
    """Check if the user's input word length is expected. Re-prompt until user word length is the expected length."""
    user_guess: str = input(f"Enter a {expected_len} character word: ")
    
    while len(user_guess) != expected_len:  # user input length is either longer or shorter than expected
        user_guess = input(f"That wasn't {expected_len} chars! Try again: ")
    return user_guess  # user input word length is equal to the expected length

if __name__ == "__main__":
    main()