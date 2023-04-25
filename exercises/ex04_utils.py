"""EX04 - 'List' Utility Functions."""

__author__: str = "730480987"


def all(list: list[int], num: int) -> bool:
    """Returns True if list matches specified number."""
    index: int = 0
    if len(list) == 0: 
        return False
    while index < len(list):
        if list[index] != num:
            return False
        index += 1
    return True


def max(input: list[int]) -> int:
    """Returns the max number."""
    num = -1
    if len(input) == 0: 
        raise ValueError("max() arg is an empty list")
    index: int = 0
    while index < len(input): 
        if input[index] > num:
            num = input[index]
        index += 1
    return num


def is_equal(list: list[int], num: list[int]) -> bool:
    """Finds if the index match the correct number."""
    index: int = 0
    if len(num) != len(list): 
        return False
    while index < len(list):
        if list[index] != num[index]:
            return False
        index += 1  
    return True