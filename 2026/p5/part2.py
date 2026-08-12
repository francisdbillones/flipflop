def solve(lines: list[str]):
    grid = [list(line.strip()) for line in lines]

    best = distinct_streets(grid) 

    other = {
            '>': '^<v',
            '<': '^>v',
            '^': '><v',
            'v': '><^'
    }

    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            orig_c = grid[i][j]
            for other_c in other[grid[i][j]]:
                grid[i][j] = other_c
                best = max(best, distinct_streets(grid))
            grid[i][j] = orig_c

    print(best)


def distinct_streets(grid: list[str]):
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

    deltas = {
            '>': (0, 1),
            '<': (0, -1),
            '^': (-1, 0),
            'v': (1, 0),
    }

    i, j = 0, 0

    ans = 0
    while not visited[i][j]:
        visited[i][j] = True
        ans += 1

        di, dj = deltas[grid[i][j]]

        i, j = i + di, j + dj

    return ans
