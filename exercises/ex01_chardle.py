""""EX01 - Chardle - A cute step toward Worlde."""

__author__ = "730480987"

name: str = input("Enter a 5-character word: ")
if len(name) != 5: 
    print("Error: Word must contain 5 characters")
    exit()
letter: str = input("Enter a single character: ")
if len(letter) != 1:
    print("Error: Character must be a single characer: ")
    exit()
print ("Searching for e in hello")
if letter==name[1]:
    print(f"{letter} is found at index 1")
    print("1 instance of e found in hello")

print("Searching for e in heels")
if letter==name[1]:
    print(f"{letter} is found at index 1")
if letter==name[2]: 
    print(f"{letter} is found at index 2")
    print("2 instances of e found in heels")

print("Searching for s in heels")
if letter==name[4]:
    print("s is found at index 4")

print("No instances of d found in heels")
