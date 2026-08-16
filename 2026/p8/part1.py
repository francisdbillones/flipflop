from collections import defaultdict


def solve(lines: list[str]):
    lines = [line.strip() for line in lines]

    rules = {}

    for line in lines:
        orig, *new = line.split()
        if orig not in rules:
            rules[orig] = new

    counts = defaultdict(lambda: 0)
    counts["A"] = 1
    counts["B"] = 1

    for _ in range(7):
        new_counts = defaultdict(lambda: 0)
        for group, count in counts.items():
            for new in rules[group]:
                new_counts[new] += count
        counts = new_counts

    print(sum(counts.values()))
