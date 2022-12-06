from load import convert_to_list


def six_one():
    lines = convert_to_list("inputs/6.txt")
    total = 0
    start_of_packet_marker = []
    for character in lines[0]:
        if character in start_of_packet_marker:
            while character in start_of_packet_marker:
                start_of_packet_marker.pop(0)

        start_of_packet_marker.append(character)
        total += 1

        if len(start_of_packet_marker) == 4:
            break

    return total


def six_two():
    lines = convert_to_list("inputs/6.txt")
    total = 0
    start_of_packet_marker = []
    for character in lines[0]:
        if character in start_of_packet_marker:
            while character in start_of_packet_marker:
                start_of_packet_marker.pop(0)

        start_of_packet_marker.append(character)
        total += 1

        if len(start_of_packet_marker) == 14:
            break

    return total
