"""EX01 - Chardle - A cute step toward Worlde."""

__author__ = "730480987"

name: str = input("Enter a 5-character word: ")
if len(name) != 5: 
    print("Error: Word must contain 5 characters")
    exit()

letter: str = input("Enter a single character: ")
if len(letter) != 1:
    print("Error: Character must be a single characer: ")
    exit()

letter==name
print("Searching for "  f"{letter} "  "in " f"{name}")

if letter==name[0]:
    print(f"{letter} is found at index 0")
if letter==name[1]:
    print(f"{letter} is found at index 1")
if letter==name[2]:
    print(f"{letter} is found at index 2")
if letter==name[3]:
    print(f"{letter} is found at index 3")
if letter==name[4]:
    print(f"{letter} is found at index 4")
