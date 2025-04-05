"""Dictionary."""

__author__ = "730735896"


def invert(d: dict[str, str]) -> dict[str, str]:
    y: dict = {}
    for key in d:
        value = d[key]
        if value in y:
            raise KeyError("Duplicate Value Found")
        y[value] = key
    return y


def count(a: list[str]) -> dict[str, int]:
    new_dict: dict = {}
    for item in a:
        if item in new_dict:
            new_dict[item] += 1
        else:
            new_dict[item] = 1
    return new_dict


def favorite_color(b: dict[str, str]) -> str:
    result = {}
    for z in b:
        color = b[z]
        if color in result:
            result[color] += 1
        else:
            result[color] = 1
    most_color = ""
    most_count = 0
    for color in result:
        if result[color] > most_count:
            most_count = result[color]
            most_color = color
    return most_color


def bin_len(f: list[str]) -> dict[int, set[str]]:
    result = {}
    for word in f:
        length = len(word)
        if length not in result:
            result[length] = {word}
        else:
            result[length] = set(result[length])
            result[length] = result[length] | {word}
    return result
