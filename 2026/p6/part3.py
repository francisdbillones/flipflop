import itertools as it
import string

from collections import deque


def solve(lines: list[str]):
    grid = [list(line.strip()) for line in lines]
    N, M = len(grid), len(grid[0])

    bluetooth = {}

    for i in range(N):
        for j in range(M):
            if grid[i][j] in string.ascii_letters:
                bluetooth[grid[i][j]] = i, j

    starting = next((i, j) for i, j in it.product(range(N), range(M)) if grid[i][j] == 'S') 

    counts = bfs(grid, starting)

    ans = 0
    for i, line in enumerate(grid):
        for j, char in enumerate(line):
            if char != '*': continue

            for ai, aj in adjacent_cells(counts, i, j, key=lambda count: count is not None):
                count = counts[ai][aj]
                ans = (ans << 1) + count % 2

    print(ans)


def bfs(grid: list[list[str]], starting: tuple[int, int]):
    N, M = len(grid), len(grid[0])
    counts = [[None for _ in range(len(grid[0]))] for _ in range(len(grid))]
    counts[starting[0]][starting[1]] = 0
    
    outputs = {}
    for i in range(N):
        for j in range(M):
            if grid[i][j] in string.ascii_uppercase:
                outputs[grid[i][j]] = i, j

    frontier = deque([starting])

    while frontier:
        i, j = frontier.popleft()

        for ai, aj in adjacent_cells(grid, i, j, lambda ch: ch in '#3' + string.ascii_lowercase):
            if grid[ai][aj] in string.ascii_lowercase:
                oi, oj = outputs[grid[ai][aj].upper()]
                if not is_prime(count_gear_group(grid, (oi, oj))):
                    for oai, oaj in adjacent_cells(grid, oi, oj, lambda ch: ch in '#3'):
                        counts[oai][oaj] = counts[i][j] + 1
                        frontier.append((oai, oaj))
            elif counts[ai][aj] is None:
                counts[ai][aj] = counts[i][j] + 1 
                frontier.append((ai, aj))


    return counts


def count_gear_group(grid: list[list[str]], source: tuple[int, int]):
    N, M = len(grid), len(grid[0])

    ans = 0
    frontier = deque([source])
    seen = set((source,)) 
    while frontier:
        i, j = frontier.popleft()
        for ai, aj in adjacent_cells(grid, i, j, lambda ch: ch == '3'):
            if (ai, aj) not in seen:
                frontier.append((ai, aj))
                seen.add((ai, aj))
                ans += 1

    return ans


def is_prime(n: int):
    return not any(n % i == 0 for i in range(2, n))


def adjacent_cells(grid: list[list[str]], i: int, j: int, key=None): 
    adjacent_indices = [
            (i - 1, j),
            (i + 1, j),
            (i, j - 1),
            (i, j + 1),
    ]

    for i, j in adjacent_indices:
        if i in range(0, len(grid)) and j in range(0, len(grid[0])):
            if key is None or key(grid[i][j]):
                yield i, j 
