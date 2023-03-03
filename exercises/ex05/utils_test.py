"""Unit tests for utils functions"""

___author___ = "730566852"

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import concat
from exercises.ex05.utils import sub


# Tests for only_evens


def test_only_evens_empty() -> None:  # check if list in empty [edge case]
    assert only_evens([]) == []


def test_only_evens_only_odd() -> None:  # check if list only contains odd elements [use case]
    test_list = [1.0, 3.0, 5.0]
    assert only_evens(test_list) == []


def test_only_evens_with_neg() -> None:  # check if list includes negatives [use case]
    test_list = [-2.0, -1.0, 3, 4]
    assert only_evens(test_list) == [-2.0, 4]


# Tests for concat


def test_concat_with_empty_lists() -> None:  # check if functions with empty lists [edge case]
    test_list1 = []
    test_list2 = []
    assert concat(test_list1, test_list2) == []


def test_concat_with_one_empty_list() -> None:  # check if function works with one empty list [edge case]
    test_list1 = []
    test_list2 = [1.0, 2.0, 3.0]
    assert concat(test_list1, test_list2) == [1.0, 2.0, 3.0]


def test_concat_with_neg() -> None:  # negatives in integer list [use case]
    test_list1 = [1.0, 2.0]
    test_list2 = [-2.0, -1.0, 0]
    assert concat(test_list1, test_list2) == [1.0, 2.0, -2.0, -1.0, 0]


def test_concat_with_many() -> None:  # larger list [use case]
    test_list1 = [1.0, 2.0, 3.0, 5.0, 100.0]
    test_list2 = [1.0, 1.0, 0.0]
    assert concat(test_list1, test_list2) == [1.0, 2.0, 3.0, 5.0, 100.0, 1.0, 1.0, 0.0]



# Tests for sub


def test_sub_same_range() -> None:  # range is 0 [edge case]
    test_list = [1, 2, 3, 4, 5]
    assert sub(test_list, 2, 2) == []


def test_sub_large_range() -> None:  # whole range [use case]
    test_list = [1, 2, 3, 4, 5]
    assert sub(test_list, 0, 5) == [1, 2, 3, 4, 5]


def test_sub_neg_() -> None:  # list has negative numbers [use case]
    test_list = [-1, -2, 0, 2, 3]
    assert sub(test_list, 0, 3) == [-1, -2, 0]