"""File to define Bear class."""


class Bear:
    """Define Bear class wiht age, hunger_score, and methods."""

    age: int
    hunger_score: int

    def __init__(self):
        """Define Bear."""
        self.age = 0
        self.hunger_score: 0
        return None
    
    def one_day(self):
        """After one day, increase Bear's age."""
        self.age += 1
        return None
    
    def eat(self, num_fish: int):
        """Increase the bear's hunger score by num_fish."""
        self.hunger_score += num_fish
        return None