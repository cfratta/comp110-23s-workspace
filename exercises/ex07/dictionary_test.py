"""Unit tests for Dictionary."""

___author___ = "730566852"

import pytest

from exercises.ex07.dictionary import invert
from exercises.ex07.dictionary import favorite_color
from exercises.ex07.dictionary import count

# Tests for invert.

def test_invert_empty() -> None:
    """Check if dict in empty [edge case]."""
    assert invert([]) == {}  # ASK QUESTION: IS BRACKET APPROPRIATE? OR CURLY BRACES FOR BOTH?


def test_invert_idential_key_value_pair() -> None:
    """Check if key and value are the same [use case]."""
    test_dict = {"sally": "sally"}
    assert invert(test_dict) == {"sally": "sally"}


def test_invert_key_error() -> None:
    """Check if list includes negatives [use case]."""
    test_dict = {"C. P E.": "Bach", "J. S.": "Bach"}
    assert invert(test_dict) == KeyError('Key already in dictionary!')  # ASK QUESTION: HOW TO TEST FOR KEYERROR BEING THROWN CORRECTLY?

# Tests for favorite_color.

def test_favorite_color_empty() -> None:
    """Check if input is empty [edge case]."""
    assert favorite_color([]) == ""

def test_favorite_color_all() -> None:
    """Check if each value is the same/same favorite color."""
    test_dict = {"Huey": "White", "Dewey": "White", "Louie": "White"}
    assert favorite_color(test_dict) == "None"

def test_favorite_color_tie() -> None:
    """Check if there is a tie for the favorite color."""
    test_dict = {"Peter": "Red", "James": "Red", "John": "Blue", "Mattew": "Blue"}
    assert favorite_color(test_dict) == "None"

# Tests for count.

def test_count_empty() -> None:
    """Check if input is empty."""
    assert count([]) == {}

def test_count_same() -> None:
    """Check if list has identical values"""
    test_list = ["blue", "blue", "blue"]
    assert count(test_list) == {"blue": 3}

def test_count_all_diff() -> None:
    """Check if list has all different elements"""
    test_list = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    assert count(test_list) == {"red": 1, "orange": 1, "yellow": 1, "green": 1, "blue": 1, "indigo": 1, "violet": 1}