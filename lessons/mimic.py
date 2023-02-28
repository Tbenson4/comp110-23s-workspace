"Practice Writing Functions"

def mimic_letter(my_words: str, letter_idx: int) -> str:
    """"Outputs the characters of my_words at index_idx"""
    if letter_idx >= len(my_words):
        return("Index is too high")
#If we made it here, that means the letter_idx is valid
    return my_words[letter_idx]


