"""Unit tests for the functions defined in utils.py."""

__author__: str = "730480987"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens() -> None: 
    """Test the only_evens function with edge case and two use cases."""
    # Edge case: empty list
    assert only_evens([]) == []
    # Use case 1: list with even and odd numbers
    assert only_evens([1, 2, 3, 4, 5]) == [2, 4]
    # Use case 2: list with only odd numbers
    assert only_evens([1, 3, 5, 7]) == []


def test_sub() -> None:
    """Test the sub function with edge case and two use cases."""
    # Edge case: empty list
    assert sub([], 0, 0) == []
    # Use case 1: slice within bounds
    assert sub([1, 2, 3, 4, 5], 4) == [2, 4]
    # Use case 2: slice starting from negative index
    assert sub([1, 2, 3, 4, 5], -2, 5) == [4, 5]


def test_concat() -> None:
    """Test the concat funcon with edge case and two use cases."""
    # Edge case: empty lists
    assert concat([], []) == []
    # Use case 1: non-empty lists
    assert concat([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    # Use case 2: one empty list
    assert concat([1, 2, 3], []) == [1, 2, 3]  