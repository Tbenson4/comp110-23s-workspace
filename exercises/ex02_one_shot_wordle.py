"""EX02 - One Shot Worldle - Loops."""

__author__ = "730480987"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
words: str = ""
i: int = 0 
found: bool = False

SECRET: str = "python"
Guess: str = input("What is your 6-letter guess? ")

while len(Guess) != 6:
    Guess = str(input("That was not 6 letters! Try again: "))
while i < len(SECRET):
    if SECRET[i] == Guess[i]:
        words += GREEN_BOX
    else: 
        j: int = 0
        found = False
        while j < len(SECRET):
            if SECRET[j] == Guess[i]: 
                words += YELLOW_BOX
                found = True
            j += 1 
        if found == False:
            words += WHITE_BOX 
    i += 1
print(words) 
if SECRET == Guess:
    print("Woo! You got it!")
else: 
    print("Not quite. Try again soon!")