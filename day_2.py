from load import convert_to_list


def get_one_round_score(opponent: str, you: str) -> int:
    if opponent == you:
        return 3
    elif (opponent == "A" and you == "B") or (opponent == "B" and you == "C") or (opponent == "C" and you == "A"):
        return 6

    return 0


def two_one():
    lines = convert_to_list("inputs/2.txt")
    choice_values = {"X": 1, "Y": 2, "Z": 3}
    normalize = {"X": "A", "Y": "B", "Z": "C"}

    total = 0
    for game in lines:
        # input
        guide = game.split(" ")
        opponent = guide[0]
        you = guide[1]

        total = total + choice_values[you] + get_one_round_score(opponent, normalize[you])

    return total


def get_choice(opponent: str, strat: str) -> str:
    # lose
    if strat == "X":
        if opponent == "A":
            return "Z"
        elif opponent == "B":
            return "X"
        return "Y"
    # draw
    elif strat == "Y":
        if opponent == "A":
            return "X"
        elif opponent == "B":
            return "Y"
        return "Z"
    # win
    else:
        if opponent == "A":
            return "Y"
        elif opponent == "B":
            return "Z"
        return "X"


def two_two():
    lines = convert_to_list("inputs/2.txt")
    choice_values = {"X": 1, "Y": 2, "Z": 3}
    normalize = {"X": "A", "Y": "B", "Z": "C"}

    total = 0
    for game in lines:
        # input
        guide = game.split(" ")
        opponent = guide[0]
        strat = guide[1]

        # lose, draw, win = x, y, z
        # choice
        you = get_choice(opponent, strat)
        total = total + choice_values[you] + get_one_round_score(opponent, normalize[you])

    return total
