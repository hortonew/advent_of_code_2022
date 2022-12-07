from load import convert_to_list


def get_tree_from_commands(commands: list[str]):
    numbers = [str(s) for s in list(range(10))]
    tree = {}
    cwd: list[str] = []
    for command in commands:
        if command.startswith("$ cd"):
            if ".." in command:
                cwd = cwd[:-1]
            else:
                dir_name = command.split("cd ")[1]
                cwd.append(dir_name)

            # determine dict
            path = "".join(cwd)
            if path not in tree:
                tree[path] = {"size": 0}

        elif command.startswith("$ ls"):
            pass
        elif command.startswith("dir "):
            pass
        elif command[0] in numbers:
            file_total = int(command.split(" ")[0])
            for i in range(len(cwd)):
                tree["".join(cwd[: len(cwd) - i])]["size"] += file_total

    return tree


def seven_one():
    lines = convert_to_list("inputs/7.txt")
    tree = get_tree_from_commands(lines)
    return sum(v["size"] for v in tree.values() if v["size"] < 100_000)


def seven_two():
    lines = convert_to_list("inputs/7.txt")
    tree = get_tree_from_commands(lines)

    potential = {}
    unused = 70000000 - tree["/"]["size"]
    for k, v in tree.items():
        if v["size"] + unused > 30_000_000:
            potential[k] = v

    lowest = 30_000_000
    for k, v in potential.items():
        lowest = min(lowest, v["size"])

    return lowest
