"""EX09 - River Simulation Parts I and II."""

__author__: str = "730480987"

from exercises.ex09.river import River


# view the initial state of the river
my_river = River(num_fish = 10, num_bears = 2)
my_river.view_river()

# simulate one week of the river
my_river.one_river_week()