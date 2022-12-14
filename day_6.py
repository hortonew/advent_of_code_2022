from load import convert_to_list


def get_total_including_marker(size: int) -> int:
    lines = convert_to_list("inputs/6.txt")
    total = 0
    marker: list[str] = []
    for character in lines[0]:
        while character in marker:
            marker.pop(0)

        marker.append(character)
        total += 1

        if len(marker) == size:
            break

    return total


def six_one():
    return get_total_including_marker(4)


def six_two():
    return get_total_including_marker(14)
