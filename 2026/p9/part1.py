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
            shortest_dist[ai, aj] = shortest_dist[i, j] + 1
            if (ai, aj) not in visited:
                frontier.append((ai, aj))
                visited.add((ai, aj))

    return shortest_dist[end]


def adjacent_cells(grid: list[list[str]], pos: tuple[int, int]):
    N, M = len(grid), len(grid[0])
    i, j = pos

    for ni, nj in (
        (i - 1, j),
        (i + 1, j),
        (i, j - 1),
        (i, j + 1),
    ):
        if 0 <= ni < N and 0 <= nj <= M:
            cell = grid[ni][nj]
            if cell != "#":
                yield (ni, nj)
