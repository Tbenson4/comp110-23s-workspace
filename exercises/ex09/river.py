"""EX09 - River Simulation Parts I and II."""

__author__: str = "730480987"


from exercises.ex09.bear import Bear
from exercises.ex09.fish import Fish


class River:
    def __init__(self, num_bears: int, num_fish: int):
        """Initialize a class to represent the river."""
        self.day = 0
        self.bears=[Bear() for _ in range(num_bears)]
        self.fish=[Fish() for _ in range(num_fish)]
    
    def view_river(self) -> None:
        """Veiwing bear and fish population in the river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
    
    def one_river_day(self) -> None:
        """Initialized river in one day."""
        for bear in self.bears:
            bear.one_day()
        for fish in self.fish:
            fish.one_day()
        self.check_ages()
    
    def one_river_week(self) -> None:
        """Initialized river in one week."""
        for _ in range(7):
            self.one_river_day()
        self.day += 7
    
    def check_ages(self):
        """As animal's age, they should be removed from the River."""
        self.fish = [fish for fish in self.fish if fish.age <= 3]
        surviving_bears = [bear for bear in self.bears if bear.age <= 5]
        self.bears = surviving_bears
    
    def bears_eating(self):
        """Number of fish being removed from the river due to Bear predation."""
        num_fish = len(self.fish)
        num_bears = len(self.bears)
    
        if num_fish < 5:
            num_bears_to_eat = num_fish // 2
            num_bears_to_skip = num_bears - num_bears_to_eat
        else:
            num_bears_to_eat = num_bears
            num_bears_to_skip = 0
    
        bears_eaten = 0
        for bear in self.bears:
            if bears_eaten < num_bears_to_eat:
                if len(self.fish) >= 3:
                    self.remove_fish(3)
                    bear.eat(3)
                    bears_eaten += 1
            elif bears_eaten < num_bears_to_eat + num_bears_to_skip:
                bears_eaten += 1
            else:
                break
    
    def check_hunger(self):
        """Hunger status of bears."""
        surviving_bears = []
        for bear in self.bears:
            if bear.hunger_score < 0: 
                print(f"A bear starved to death on self {self.day}!")
            else:
                surviving_bears.append(bear)
        self.bears = surviving_bears
    
    def repopulate_bears(self):
        """Repopulated the bear population."""
        new_bears = []
        num_bears = len(self.bears)
        for i in range(num_bears // 2):
            new_bear = Bear()
            new_bears.append(new_bear)
        self.bears.extend(new_bears)

    def repopulate_fish(self):
        """Repopulated fish."""
        num_fish = len(self.fish)
        num_new_fish = (num_fish // 2) * 4
        for _ in range(num_new_fish):
            self.fish.append(Fish())
    
    def remove_fish(self, num_fish: int = 1):
        """Remove frontmost fish from river."""
        for _ in range(num_fish):
            if len(self.fish) > 0:
                self.fish.pop(1)