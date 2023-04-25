"""EX09 - River Simulation Parts I and II."""

__author__: str = "730480987"


class Fish: 
    def __init__(self, age: int = 0):
        """Initialize a class to represent the fish."""
        self.age = age
    
    def one_day(self):
        """One day for fish"""
        self.age += 1