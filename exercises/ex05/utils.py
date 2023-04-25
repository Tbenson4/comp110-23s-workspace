"""EX05 - 'list' Utility Functions"""

__author__: str = "730480987"

def only_evens(given_list: list[int]) -> list[int]:
    """Returns even number."""
    results: list[int] = list()
    num: int = 0
    while (num < len(given_list)):
        if given_list[num] % 2 == 0:
            results.append(given_list[num])
        num += 1 
    return results


def concat(given_list: list[int], num: list[int]) -> list[int]:
    """Returns new list of all elements."""
    results: list[int] = []
    for number in given_list:
        results.append(number)
    for number in num:
        results.append(number)
    return results


def sub(a_list, start, end): 
    """Returns number from index."""
    if len(a_list) == 0 or start >= len(a_list) or end <= 0:
        return []
    elif start < 0:
        start = 0
    elif end > len(a_list):
        end = len(a_list)
    return a_list[start:end]