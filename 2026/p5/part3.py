def solve(lines: list[str]):
    grid = [list(line.strip()) for line in lines]

    best = distinct_streets(grid)

    other = {">": "^<v", "<": "^>v", "^": "><v", "v": "><^"}

    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            orig_c = grid[i][j]
            for other_c in other[grid[i][j]]:
                grid[i][j] = other_c
                best = max(best, distinct_streets(grid))
            grid[i][j] = orig_c

    print(best)


def distinct_streets(grid: list[list[str]]):
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

    deltas = {
        ">": (0, 1),
        "<": (0, -1),
        "^": (-1, 0),
        "v": (1, 0),
    }

    right_turn = {">": "v", "v": "<", "<": "^", "^": ">"}

    i, j = 0, 0

    ans = 0
    illegal_right_turns_left = 3
    while True:
        ch = grid[i][j]
        if visited[i][j]:
            if i in (0, len(grid) - 1) or j in (0, len(grid[0]) - 1):
                break
            if illegal_right_turns_left:
                ch = right_turn[ch]
                illegal_right_turns_left -= 1
            else:
                break

        ans += not visited[i][j]
        visited[i][j] = True

        di, dj = deltas[ch]
        i, j = i + di, j + dj

    return ans
