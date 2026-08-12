def solve(lines: list[str]):
    grid = [line.strip() for line in lines]

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

    print(ans)
