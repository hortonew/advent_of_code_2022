def convert_to_list(path: str):
    with open(path, "r") as f:
        return f.read().splitlines()
