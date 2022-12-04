from typing import Set

from load import convert_to_list


def convert_range_to_set(r: str) -> Set:
    split = r.split("-")
    return set(range(int(split[0]), int(split[1]) + 1))


def any_overlap(s1: Set, s2: Set) -> bool:
    return any(s1 & s2)


def four_one():
    lines = convert_to_list("inputs/4.txt")
    total = 0
    for line in lines:
        ranges = line.split(",")
        s1: Set = convert_range_to_set(ranges[0])
        s2: Set = convert_range_to_set(ranges[1])
        if s1.issubset(s2) or s2.issubset(s1):
            total += 1

    return total


def four_two():
    lines = convert_to_list("inputs/4.txt")
    total = 0
    for line in lines:
        ranges = line.split(",")
        s1: Set = convert_range_to_set(ranges[0])
        s2: Set = convert_range_to_set(ranges[1])
        if any_overlap(s1, s2):
            total += 1

    return total
