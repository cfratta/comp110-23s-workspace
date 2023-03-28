"""EX06 - Choose Your Own Adventure!"""

__author__ = "730566852"

import random

player: str = ""  # player name
decision: str = ""  # to play, or not to play?
max_correct: int = 0  # player chooses difficulty
correct: int = 0  # correct guess streak
points: int = 5  # points used as "lives"
play: bool = True # in order to exit game
coin: str = "" # determine coin flip
COIN_EMOJI: str = "\U0001FA99"
STARS_EMOJI: str = "\U0001F30C"
EARNED: str = "\U0001F496"
LOST: str = "\U0001F494"


def main() -> None:
    global play
    # Opening
    greet()
    while play:
        if decision == "what are you hiding":
            what_are_you_hiding()
        if decision == "yes":

            # Enter game loop
            if max_correct == 0:
                print(f"So, let Us explain how this game works: each time you guess a coin toss correctly, you gain one life! Each time you guess a coin incorrectly, you lose a life. If you get a certain number of coin guesses correct in a row (you pick!), you win! If you run out of lives . . . well . . .")
                correct_streak(int(input(f"Choose your difficulty! Please enter how many coins you have to guess in a row to win. (Easy: 2, Medium: 3, Hard: 4+): ")))

            while points > 0 and max_correct > correct:
                coin_flip()
                guess(input(f"Heads or tails?: "))
            
                if points == 0:  # ran out of lives
                    print(f"Sorry, {player}, your ran out of lives on this task has now expired. Try passing this test another time.")
                    play = False
                if correct == max_correct:  # won game
                    print(f"Congratulations, {player}! You have won the game. Enjoy peace of mind until the next test.")
                    play = False

        if decision == "no":
            no()



def greet() -> None:
    """Greet player (ask for their name) and introduce game"""
    global player
    global decision
    print(f"Coin Flip Game!")
    player = input(f"Please enter your name: ")
    # COIN goes here
    print(f"Welcome, {player}, to a simpler world. In order to survive this next test of humanity, WE put you do a random test: How many coins flips can you guess correctly in a row? {COIN_EMOJI} \n Seems cruel? Depends on how you look at it.")
    decision = input(f"Want to play? Type 'yes', 'no', or 'what are you hiding': ")


def what_are_you_hiding() -> None:
    """Should user types 'what are you hiding' in Greet procedure, loop again"""
    global decision
    global points
    
    points += 1
    print(f"O {player}, you thought that mysteries of the universe would be revealed to you? {STARS_EMOJI} Yet, WE have nothing to hide. Come, now, just play the game. \n However, you curiosity has rewarded you and you have earned a bonus life . . .")
    decision = input(f"Type 'yes' to continue or 'no' to quit: ")


def no() -> None:
    """If user types 'no' in Greet procedure, exit game"""
    global play
    print(f"So, be it. But you shall come across this test again and you will not be able to say no. Until then.")
    play = False


def correct_streak(user_input: int) -> int:
    """User decides how many coins to guess in a row to win"""
    global max_correct
    global points
    if user_input < 2:
        points -= 1
        user_input = int(input(f"Oi, {player}, don't think you can outsmart Us like that. We have accordingly removed one of your lives {LOST}, leaving you with a total of {points} lives. \n What difficulty do you pick, greater than 1?: "))
    max_correct = user_input
    return max_correct


def coin_flip() -> str:
    """Flips coin"""
    global coin    
    side: int = random.randint(0, 1)

    if side == 0:
        coin = "tails"
    if side == 1:
        coin = "heads"
    return coin


def guess(user_input: str) -> str:
    """User guesses heads or tails"""

    global points
    global correct
    global coin

    if user_input == coin:
        points += 1
        correct += 1
        print(f"Correct guess, {player}! The coin toss was {coin}. Earned an extra life (total: {points})! {EARNED}")
    elif user_input != coin:
        points -= 1
        correct = 0
        print(f"Incorrect guess, {player}. The coin toss was {coin}. Lost a life (total left: {points}) and reset count streak to zero. {LOST} ")
    return user_input


if __name__ == "__main__":
    main()