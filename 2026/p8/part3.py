import itertools as it
from collections import defaultdict


def solve(lines: list[str]):
    lines = [line.strip() for line in lines]

    rules = {}

    for line in lines:
        first, second, *babies = line.split()

        rules[(first, second)] = [
            pair for pair in it.pairwise((first, *babies, second))
        ]
        rules[(second, first)] = [
            pair for pair in it.pairwise((second, *babies, first))
        ]

    pair_counts = defaultdict(lambda: 0)
    pair_counts[("A", "B")] = 1

    for _ in range(21):
        new_pair_counts = defaultdict(lambda: 0)

        for pair, count in pair_counts.items():
            for new_pair in rules[pair]:
                new_pair_counts[new_pair] += count

        pair_counts = new_pair_counts

    print(sum(pair_counts.values()) + 1)
