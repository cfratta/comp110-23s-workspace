"""File to define Fish class."""


class Fish:
    """Define Fish class wtih age and methods."""

    age: int

    def __init__(self):
        """Define Fish."""
        self.age = 0
        return None
    
    def one_day(self):
        """After one day, increase fish's age."""
        self.age += 1
        return None