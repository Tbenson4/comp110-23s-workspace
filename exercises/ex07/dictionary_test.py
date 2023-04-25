"""Unit tests for the functions defined in dictionary.py."""

__author__: str = "730480987"

from exercises.ex07.dictionary import invert, favorite_color, count
import pytest


def test_invert_empty() -> None: 
    """Test the invert function with empty dictionary."""
    # Edge case: empty dictionary
    assert invert(dict) == ({}) == {}


def test_invert_unique() -> None: 
    """Test the favorite_color function with edge case and two use cases."""
    # Use case 1: unique keys and values
    assert invert(dict) == ({'a': 'z', 'b': 'y', 'c': 'x'}) == {'z': 'a', 'y': 'b', 'x': 'c'}
    # Use case 2: edge case to test for raising key error for same keys


def test_invert_edge() -> None:
    """Edge case to test for raising key error for same keys."""
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)


def test_favorite_color_empty() -> None:
    """Test the favorite_color function with empty dictionary."""
    # Edge case: empty dictionary
    assert favorite_color({}) is None


def test_favorite_color_unique() -> None: 
    """Test the favorite_color function with different colors."""
    # Use case 1: unique colors
    assert favorite_color({'Jim': 'red', 'Steve': 'green', 'Jessica': 'blue'}) == 'red'


def test_favorite_color_multiple() -> None: 
    """Test the favorite_color function with the same multiple colors."""
    # Use case 2: multiple popular colors
    assert favorite_color({'Marc': 'yellow', 'Ezri': 'blue', 'Kris': 'blue'}) == 'blue'


def test_count_empty() -> None:
    """Test the count function with empty dictionary."""
    # Edge case: empty dicitonary
    assert count([]) == {}


def test_count_unique() -> None:    
    """Test the count function with unique values."""
    # Use case 1: unique values
    assert count(['apple', 'banana', 'orange']) == {'apple': 1, 'banana': 1, 'orange': 1}


def test_count_non_unique() -> None:       
    """Test the count function with non-unique values."""
    # Use case 2: non-unique values 
    assert count(['apple', 'banana', 'apple', 'orange', 'banana', 'apple']) == {'apple': 3, 'banana': 2, 'orange': 1}
    