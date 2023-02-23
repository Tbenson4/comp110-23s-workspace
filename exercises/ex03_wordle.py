"""EX03 - Structured Wordle"""

__author__: str = "730480987"

GREEN_BOX: str = "\U0001F7E9"
WHITE_BOX: str = "\U00002B1C"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(word:str, letter:str) -> bool:
    """"Returns true if single character is found at any index"""
    assert len(letter) == 1
    j: int = 0
    found = False
    while j < len(word):
        if word[j] == letter: 
            found = True
        else:  
            found = False
        j += 1 
    return found 

def emojified(guess: str, secret: str) -> str:
    """Test for green, yellow, or white box codification"""
    assert len(guess) == len(secret)
    i: int = 0
    results: str = ""
    while i < len(secret):
        if contains_char(secret, guess[i]):
            if guess[i] == secret[i]:
                results += GREEN_BOX
            else: 
                results += YELLOW_BOX
        else: 
            results += WHITE_BOX  
        i += 1 
    return results

def input_guess(expected_length: int) -> str:
    """Test for expected length of guess"""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length: 
        guess = str(input(f"That wasn't {expected_length} chars! Try again: "))
    return guess

def main() -> None: 
    """"The entrypoint of the program and main game loop."""
# Define game state variabes
secret = "codes"
num_turns = 6 
turn = 1
won = False

#Game loop
while turn <= num_turns and not won:
    print(f"=== Turn {turn}/{num_turns} ===")
    guess = input_guess(len(secret))
    result = emojified(guess, secret)
    print(result)
    if guess == secret: 
        won = True
    turn += 1

#End of game
if won: 
    print(f"You won in {turn-1}/{num_turns} turns!")
else:
    print(F"X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()