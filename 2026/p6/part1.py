import itertools as it
from collections import deque
from collections.abc import Callable


def solve(lines: list[str]):
    grid = [list(line.strip()) for line in lines]
    N, M = len(grid), len(grid[0])

    starting = next(
        (i, j) for i, j in it.product(range(N), range(M)) if grid[i][j] == "S"
    )

    counts = bfs(grid, starting)

    ans = 0
    for i, line in enumerate(grid):
        for j, char in enumerate(line):
            if char != "*":
                continue

            for ai, aj in adjacent_cells(
                counts, i, j, key=lambda count: count is not None
            ):
                count = counts[ai][aj]
                assert count is not None
                ans = (ans << 1) + count % 2

    print(ans)


def bfs(grid: list[list[str]], starting: tuple[int, int]):
    counts: list[list[int | None]] = [
        [None for _ in range(len(grid[0]))] for _ in range(len(grid))
    ]
    counts[starting[0]][starting[1]] = 0

    frontier = deque([starting])

    while frontier:
        i, j = frontier.popleft()

        for ai, aj in adjacent_cells(grid, i, j, lambda ch: ch == "#"):
            if counts[ai][aj] is None:
                current = counts[i][j]
                assert current is not None
                counts[ai][aj] = current + 1
                frontier.append((ai, aj))

    return counts


def adjacent_cells[T](
    grid: list[list[T]], i: int, j: int, key: Callable[[T], bool] | None = None
):
    adjacent_indices = [
        (i - 1, j),
        (i + 1, j),
        (i, j - 1),
        (i, j + 1),
    ]

    for ni, nj in adjacent_indices:
        if (
            ni in range(len(grid))
            and nj in range(len(grid[0]))
            and (key is None or key(grid[ni][nj]))
        ):
            yield ni, nj
