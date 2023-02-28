"""EX04 - 'List' Utility Functions"""

__author__: str = "730480987"

def all (list: list[int], num: int) -> bool:
    index: int = 0
    while index < len(list):
        if list[index] != num:
            return False
        index += 1
    return True

def max (input: list[int]) -> int:
    num = 0
    if len(input) == 0: 
        raise ValueError("max() arg is an empty list")
    index: int = 0
    while index < len(input): 
        if input[index] > num:
            num = input[index]
        index += 1
    return num

def is_equal (list: list[int], num: list[int]) -> bool:
    index: int = 0
    while index < len(list):
        if list[index] != num[index]:
            return False
        index += 1  
    return True