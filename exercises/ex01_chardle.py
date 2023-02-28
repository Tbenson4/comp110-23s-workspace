"""EX01 - Chardle - A cute step toward Worlde."""

__author__ = "730480987"

name: str = input("Enter a 5-character word:")
if len(name) != 5: 
    print("Error: Word must contain 5 characters")
    exit()

letter: str = input("Enter a single character:")
if len(letter) != 1:
    print("Error: Character must be a single characer:")
    exit()
print("Searching for "  f"{letter} "  "in " f"{name}")
upDate = 0
if letter == name[0]:
    print(f"{letter} found at index 0")
    upDate += 1
if letter == name[1]:
    print(f"{letter} found at index 1")
    upDate += 1
if letter == name[2]:
    print(f"{letter} found at index 2")
    upDate += 1
if letter == name[3]:
    print (f"{letter} found at index 3")
    upDate += 1
if letter == name[4]:
    print(f"{letter} found at index 4")
    upDate += 1
if letter == name[4]:
    print(f"{letter} found at index 4")
    upDate += 1
    
upDate2 = str(upDate)
if letter != str(upDate):
    print("No instances of " + f"{letter} found in " f"{name}")
    print(upDate2 + " instance of " + f"{letter} found in " f"{name}")
    print(upDate2 + " instances of " + f"{letter} found in " f"{name}")