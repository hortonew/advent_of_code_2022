import itertools
import string

from load import convert_to_list


def get_item_match(list_1: str, list_2: str) -> str:
    for character in list_1:
        if character in list_2:
            return character

    raise ValueError


def get_item_match_with_three(list_1: str, list_2: str, list_3: str):
    for c_1, c_2, c_3 in itertools.product(list_1, list_2, list_3):
        if c_1 == c_2 == c_3:
            return c_1
    raise ValueError


def get_item_priority(item: str) -> int:
    if item.isupper():
        return string.ascii_uppercase.index(item) + 27
    else:
        return string.ascii_lowercase.index(item) + 1


def three_one():
    lines = convert_to_list("inputs/3.txt")
    total = 0
    for rucksack in lines:
        half = len(rucksack) // 2
        list_1 = rucksack[:half]
        list_2 = rucksack[half:]
        common = get_item_match(list_1, list_2)
        priority = get_item_priority(common)
        total += priority
    return total


def three_two():
    lines = convert_to_list("inputs/3.txt")
    total = 0
    for i in range(0, len(lines), 3):
        group = lines[i : i + 3]
        common = get_item_match_with_three(group[0], group[1], group[2])
        priority = get_item_priority(common)
        total += priority
    return total
