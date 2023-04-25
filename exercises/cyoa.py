"""EX06 - Choose Your Own Adventure."""

__author__: str = "730480987"

points: int = 0
player: str = ""
NAME_CONSTANT: str = "\U00002B1C"


def greet() -> None:
    """Enter the player's name."""
    global player 
    player = input("What is your name? ")
    print(f"Welcome {player}! Lets go on an adventure.")


def option_menu() -> int:
    """Pick one option to begin the adventure."""
    print("What would you like to do next?")
    print("1. Explore the forest")
    print("2. Investigate the haunted hause")
    print("3. End the adventure")
    choice = int(input("Enter your choice (1-3): "))
    return choice


def explore_forest(points) -> int: 
    """Explore the forest and try to find the treasure of love."""
    print("You enter the forest and start exploring...")
    # generate a random number between 1 and 10
    rand_num: int = int(input("Enter a number between 1 - 10: "))
    if rand_num <= 5: 
        print(f"{NAME_CONSTANT} You found the treasure of love! +20 points")
        points += 20
    else: 
        print("You did not find the treasure chest")
        points += 10
    return points


def investigate_house(points) -> int: 
    """Investigate the haunted house, but you must keep quiet."""
    print("You arrive at the haunted house and start investigating. +15 points")
    points += 15
    return points


def main() -> None:
    """By the end of the adventure, the player can continue to keep playing or end the game with the points they earned."""
    global points
    greet()
    playing: bool = True
    while playing is True:
        choice = option_menu()
        if choice == 1:
            points = explore_forest(points)
        elif choice == 2:
            points = investigate_house(points)
        elif choice == 3:
            print(f"Goodbye {player}! You accumulated {points} adventure points.")
            return None
        else: 
            print("Invalid choice. Please try again.")
        game: str = input("If you want to continue playing, enter 1, if you want to end the adventure, enter 2: ")   
        if game == '2':
            print(f"Goodbye {player}! You accumulated {points} adventure points.")
            playing = False


if __name__ == "__main__":
    main()