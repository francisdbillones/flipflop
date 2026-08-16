import itertools as it


def solve(lines: list[str]):
    lines = [line.strip() for line in lines]

    rules = {}

    for line in lines:
        stoats = line.split()
        first, second, *new = stoats
        rules[(first, second)] = new
        rules[(second, first)] = new

    stoats = ["A", "B"]
    for _ in range(7):
        new_stoats = []

        for first, second in it.pairwise(stoats):
            new_stoats.append(first)
            if babies := rules.get((first, second)):
                new_stoats.extend(babies)
                # print(f"{first} and {second} made {babies}")
        new_stoats.append(stoats[-1])

        stoats = new_stoats
        # print("".join(stoats))

    print(len(stoats))
