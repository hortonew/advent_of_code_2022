from load import convert_to_list


def get_stacks():
    """
        [V] [G]             [H]
    [Z] [H] [Z]         [T] [S]
    [P] [D] [F]         [B] [V] [Q]
    [B] [M] [V] [N]     [F] [D] [N]
    [Q] [Q] [D] [F]     [Z] [Z] [P] [M]
    [M] [Z] [R] [D] [Q] [V] [T] [F] [R]
    [D] [L] [H] [G] [F] [Q] [M] [G] [W]
    [N] [C] [Q] [H] [N] [D] [Q] [M] [B]
     1   2   3   4   5   6   7   8   9
    """
    return [
        ["N", "D", "M", "Q", "B", "P", "Z"],
        ["C", "L", "Z", "Q", "M", "D", "H", "V"],
        ["Q", "H", "R", "D", "V", "F", "Z", "G"],
        ["H", "G", "D", "F", "N"],
        ["N", "F", "Q"],
        ["D", "Q", "V", "Z", "F", "B", "T"],
        ["Q", "M", "T", "Z", "D", "V", "S", "H"],
        ["M", "G", "F", "P", "N", "Q"],
        ["B", "W", "R", "M"],
    ]


def five_one():
    lines = convert_to_list("inputs/5.txt")
    stacks = get_stacks()
    for instruction in lines:
        instruction_move = int(instruction.split(" from ")[0].removeprefix("move "))
        instruction_from = int(instruction.split("from ")[1].split(" to ")[0]) - 1
        instruction_to = int(instruction.split(" to ")[1]) - 1

        for _ in range(instruction_move):
            stacks[instruction_to].append(stacks[instruction_from].pop(-1))

    # Return the top most item in each stack, combined as a string
    return "".join([stack[-1] for stack in stacks])


def five_two():
    lines = convert_to_list("inputs/5.txt")
    stacks = get_stacks()
    for instruction in lines:
        instruction_move = int(instruction.split(" from ")[0].removeprefix("move "))
        instruction_from = int(instruction.split("from ")[1].split(" to ")[0]) - 1
        instruction_to = int(instruction.split(" to ")[1]) - 1

        # pop the list, reverse it, append the reversed list to new stack
        combined_items = [stacks[instruction_from].pop(-1) for _ in range(instruction_move)]
        combined_items.reverse()
        for item in combined_items:
            stacks[instruction_to].append(item)

    # Return the top most item in each stack, combined as a string
    return "".join([stack[-1] for stack in stacks])
