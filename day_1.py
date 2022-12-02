from load import convert_to_list


def one_one():
    lines = convert_to_list("inputs/1.txt")

    highest_total = 0
    total_by_elf = 0
    for calories in lines:
        if calories:
            total_by_elf += int(calories)

        else:
            if total_by_elf > highest_total:
                highest_total = total_by_elf

            total_by_elf = 0

    return highest_total


def one_two():
    lines = convert_to_list("inputs/1.txt")

    totals = []
    total_by_elf = 0
    for calories in lines:
        if calories:
            total_by_elf += int(calories)
        else:
            totals.append(total_by_elf)
            total_by_elf = 0

    totals.sort(reverse=True)
    return sum(totals[:3])
