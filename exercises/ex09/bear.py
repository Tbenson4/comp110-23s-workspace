"""EX09 - River Simulation Parts I and II."""

__author__: str = "730480987"


class Bear: 
    def __init__(self, age: int = 0, hunger_score: int = 0):
        """Initialize a class to represent the bears living by the river."""
        self.age = 0
        self.hunger_score = 0
    
    def one_day(self): 
        """One day survival."""
        self.age += 1 
        self.hunger_score -= 1
    
    def eat(self, num_fish: int):
        """Number of fish being eaten."""
        self.hunger_score += num_fish