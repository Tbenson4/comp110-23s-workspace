"""Challenge Question 04 - Dict Function Writing"""

def zip(strings: list[str], integers: list[int]) -> dict[str, int]:
    """Function takes two lists of equal length and returns a dictionary where the values correspond to the keys. If the input lists are different lengths or empty, the funciton will return an empty dictionary."""
    if len(strings) != len(integers) or len(strings) == 0:
        return {}
    i: int = 0
    dictionary: dict[str, int] = {}
    while i < len(integers):
        dictionary[strings[i]] = integers[i]
        i += 1
    return dictionary


