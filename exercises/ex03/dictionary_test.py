"""Dictionary Test."""

__author__ = "730735896"

from exercises.ex03.dictionary import invert
from exercises.ex03.dictionary import favorite_color
from exercises.ex03.dictionary import count
from exercises.ex03.dictionary import bin_len


def test_invert_normal() -> None:
    """Tests normal functioning of invert"""
    my_dictionary = {"a": "b", "c": "d"}
    assert invert(my_dictionary) == {"b": "a", "d": "c"}


def test_invert_one() -> None:
    """Tests functioning of invert with onle one key and value"""
    my_dictionary = {"a": "b"}
    assert invert(my_dictionary) == {"b": "a"}


def test_invert_empty() -> None:
    """Tests functioning of invert when dict is empty"""
    my_dictionary = {}
    assert invert(my_dictionary) == {}


def test_count_normal() -> None:
    """Tests normal functioning of count"""
    my_list = ["apple", "banana", "orange", "apple"]
    assert count(my_list) == {"apple": 2, "banana": 1, "orange": 1}


def test_count_unique() -> None:
    """Tests functioning of count when each key has a value of 1"""
    my_list = ["red", "yellow", "blue"]
    assert count(my_list) == {"red": 1, "yellow": 1, "blue": 1}


def test_count_empty() -> None:
    """Tests functioning of count when list is empty"""
    my_list = []
    assert count(my_list) == {}


def test_favorite_color_normal() -> None:
    """Tests normal functioning of favorite color"""
    my_dict = {
        "Ryan": "Blue",
        "Jude": "Red",
        "Matt": "Red",
        "Sheldon": "Green",
    }
    assert favorite_color(my_dict) == "Red"


def test_favorite_color_tie() -> None:
    """Tests functioning of favorite color when two colors have the same value"""
    my_dict = {
        "Ryan": "Blue",
        "Jude": "Red",
        "Matt": "Red",
        "Sheldon": "Green",
        "Alex": "Green",
    }
    assert favorite_color(my_dict) == "Red"


def test_favorite_color_empty() -> None:
    """Tests functioning of favorite color when dict is empty"""
    my_dict = {}
    assert favorite_color(my_dict) == ""


def test_bin_len_normal() -> None:
    """Tests normal functioning of bin len"""
    my_list = ["fish", "cat", "whale"]
    assert bin_len(my_list) == {4: {"fish"}, 3: {"cat"}, 5: {"whale"}}


def test_bin_len_multiple() -> None:
    """Tests functioning of bin len with repeated keys"""
    my_list = ["fish", "fish", "cat", "whale"]
    assert bin_len(my_list) == {4: {"fish"}, 3: {"cat"}, 5: {"whale"}}


def test_bin_len_empty() -> None:
    """Tests functioning of bin len with an empty list"""
    my_list = []
    assert bin_len(my_list) == {}


from exercises.ex03.dictionary import invert, favorite_color, count, bin_len
