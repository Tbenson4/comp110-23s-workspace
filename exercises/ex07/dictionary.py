"""EX07 - Dictionary Functions."""

__author__ = "730480987"


def invert(d: dict[str, str]) -> dict[str, str]:
    """Returns inverted list of values."""
    if not isinstance(d, dict):
        raise TypeError("Input must be a dictionary")
    
    inverted = {}
    for k, v in d.items():
        if v in inverted:
            raise KeyError("Error message of your choice here!")
        inverted[v] = k
    return inverted


def favorite_color(colors: dict[str, str]) -> str:
    """Returns most frequent color."""
    color_counts = {}
    for color in colors.values():
        if color not in color_counts: 
            color_counts[color] = 0
        color_counts[color] += 1
    most_common_color = None
    for color in colors.values():
        if most_common_color is None or color_counts[color] > color_counts[most_common_color]:
            most_common_color = color
    return most_common_color


def count(values: list[str]) -> dict[str, int]:
    """Returns the count of frequencies of each item."""
    result = {}
    for value in values:
        if value in result:
            result[value] += 1
        else: 
            result[value] = 1
    return result
