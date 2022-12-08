import copy
import math

from load import convert_to_list


def separate_trees_into_rows_and_cols(lines: list[str]) -> dict:
    trees = {"cols": {i: "" for i in range(len(lines[0]))}, "rows": dict(enumerate(lines))}

    # add entries into columns
    for column in range(len(lines[0])):
        # loop over rows and add each value into the corresponding cols
        for row in lines:
            trees["cols"][column] += row[column]

    return trees


def interior_tree_can_be_seen(trees: dict, row: int, col: int):
    # check row
    r = trees["rows"][row]
    subset: list[int] = []
    for idx, tree in enumerate(r):
        if int(tree) < int(r[col]) or idx == col:
            subset.append(0)
        else:
            subset.append(1)

        # If we hit our tree or are at the end, check if we can see it
        if idx in [col, len(r) - 1]:
            if sum(subset) == 0:
                # print(f"Row match: Interior {row=}, {col=} is visible.")
                return True
            else:
                subset = []

    # check col
    c = trees["cols"][col]
    col_subset: list[int] = []
    for idx, tree in enumerate(c):
        if int(tree) < int(c[row]) or idx == row:
            col_subset.append(0)
        else:
            col_subset.append(1)

        if idx in [row, len(c) - 1]:
            if sum(col_subset) == 0:
                # print(f"Col match: Interior {row=}, {col=} is visible.")
                return True
            else:
                col_subset = []

    return False


def eight_one():
    lines = convert_to_list("inputs/8.txt")
    trees = separate_trees_into_rows_and_cols(lines)

    total = 0
    # for each distinct item, check if it can be seen
    for row_idx, row in enumerate(lines):
        for col_idx, col in enumerate(row):
            # print(f"{row}, {row_idx=}, {col_idx=}, {col}")
            if row_idx == 0 or col_idx == 0 or col_idx == len(row) - 1 or row_idx == len(lines) - 1:
                # print("Edge can be seen")
                total += 1

            # check if it can be seen in the row
            elif interior_tree_can_be_seen(trees, row_idx, col_idx):
                total += 1

    return total


def append_count(arg0, arg1, values):
    count = 0
    if arg0:
        for tree in arg0:
            count += 1

            if tree >= arg1:
                break
    values.append(count)


def scenic_score(trees: dict, row: int, col: int):
    values: list[int] = []

    r = trees["rows"][row]
    c = trees["cols"][col]

    current_item = r[col]

    left = list(copy.deepcopy(r[:col]))
    left.reverse()
    right = r[col + 1 :]  # noqa
    up = list(copy.deepcopy(c[:row]))
    up.reverse()
    down = c[row + 1 :]  # noqa

    append_count(left, current_item, values)
    append_count(right, current_item, values)
    append_count(up, current_item, values)
    append_count(down, current_item, values)
    return math.prod(values) if values else 0


def eight_two():
    lines = convert_to_list("inputs/8.txt")
    trees = separate_trees_into_rows_and_cols(lines)

    total = 0
    # for each distinct item, check if it can be seen
    for row_idx, row in enumerate(lines):
        for col_idx, _ in enumerate(row):
            total = max(total, scenic_score(trees, row_idx, col_idx))

    return total
