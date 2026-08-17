import itertools as it
from collections import deque


def solve(lines: list[str]):
    grid = [line.strip() for line in lines]

    N, M = len(grid), len(grid[0])

    start = next((i, j) for i, j in it.product(range(N), range(M)) if grid[i][j] == "S")
    end = next((i, j) for i, j in it.product(range(N), range(M)) if grid[i][j] == "E")

    print(shortest(grid, start, end))


def shortest(
    grid: list[list[str]], start: tuple[int, int], end: tuple[int, int]
) -> int:

    frontier = deque([start])
    visited = set()

    shortest_dist = {start: 0}

    while frontier:
        i, j = frontier.popleft()

        if end == (i, j):
            break

        for ai, aj in adjacent_cells(grid, (i, j)):
            shortest_dist[ai, aj] = min(
                shortest_dist.get((ai, aj), float("inf")), shortest_dist[i, j] + 1
            )
            if (ai, aj) not in visited:
                frontier.append((ai, aj))
                visited.add((ai, aj))

    return shortest_dist[end]


def adjacent_cells(grid: list[list[str]], pos: tuple[int, int]):
    DELTAS = (
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
    )

    for delta in DELTAS:
        if (
            valid_pos(grid, new := apply_delta(pos, delta))
            and cell_at(grid, new) != "#"
        ):
            yield new

        k = 1
        while (
            valid_pos(grid, new := apply_delta(pos, delta, multiplier=k))
            and cell_at(grid, new) != "#"
        ):
            k += 1

        if k > 2:
            yield apply_delta(pos, delta, multiplier=k - 1)


def apply_delta(pos: tuple[int, int], delta: tuple[int, int], multiplier: int = 1):
    i, j = pos
    di, dj = delta

    return (i + di * multiplier, j + dj * multiplier)


def valid_pos(grid: list[list[str]], pos: tuple[int, int]):
    N, M = len(grid), len(grid[0])
    i, j = pos

    return 0 <= i < N and 0 <= j < M


def cell_at(grid: list[list[str]], pos: tuple[int, int]):
    i, j = pos
    return grid[i][j]
