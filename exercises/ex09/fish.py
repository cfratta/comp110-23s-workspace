"""File to define Fish class"""

class Fish:
    
    age: int

    def __init__(self):
        self.age = 0
        return None
    
    def one_day(self):
        """After one day, increase fish's age"""
        self.age += 1
        return None