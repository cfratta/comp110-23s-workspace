"""File to define River class."""

__author__ = "730566852"

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """Define River with day, bears, fish, and methods."""

    day: int  # what day of river's lifecycle I'm modeling
    bears: list[Bear]  # river's bears population
    fish: list[Fish]  # river's fish population

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """If Fish's age > 3 or a Bear's age is > 5, remove Fish or Bear."""
        surviving_bears: list[Bear] = []
        surviving_fish: list[Fish] = []
        for x in self.bears:
            if x.age <= 5:
                surviving_bears.append(x)
        for y in self.fish:
            if y.age <= 3:
                surviving_fish.append(y)
        self.bears = surviving_bears
        self.fish = surviving_fish
        return None

    def bears_eating(self):
        """If there are at least 5 Fish in the River, Bear will eat 3 Fish."""
        for x in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                x.eat(3)
        return None
    
    def check_hunger(self):
        """If Bear's hunger score < 0, the Bear starved. Remove from river."""
        surviving_bears: list[Bear] = []
        for x in self.bears:
            if x.hunger_score < 0:
                surviving_bears.append(x)
        self.bears = surviving_bears
        return None
        
    def repopulate_fish(self):
        """For each pair of Fish, add four new Fish."""
        n: int = (len(self.fish) // 2) * 4
        for x in range(0, n):
            self.fish.append(Fish())
        return None
    
    def repopulate_bears(self):
        """For each pair of Bears, add one new Bear."""
        n: int = len(self.bears) // 2
        for x in range(0, n):
            self.bears.append(Bear())
        return None
    
    def view_river(self):
        """Print a summary of the Fish and Bear population."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
        
    def one_river_week(self):
        """Simulate one week of life in the river."""
        while self.day < 7:
            self.one_river_day
            self.day += 1
        return None
    
    def remove_fish(self, amount: int):
        """Remove 'amount' of Fish from River."""
        for x in range(0, amount):
            self.fish.pop(x)
        return None