from collections import deque

from di import real, sample


@sample(grid_size=10)
@real(grid_size=30)
def solve(lines: list[str], grid_size: int):
    lines = [line.strip() for line in lines]

    instructions, _, *points = lines

    points = [(int(x), int(y)) for x, y in (line.split(",") for line in points)]

    snake_i, snake_j = 0, 0
    ans = 0
    segments_deque = deque()
    segments_set = set()
    for i, move in enumerate(instructions):
        # print(move)
        segments_deque.append((snake_i, snake_j))
        segments_set.add((snake_i, snake_j))

        DELTA = {
            "^": (0, 1),
            "v": (0, -1),
            "<": (-1, 0),
            ">": (1, 0),
        }

        di, dj = DELTA[move]
        snake_i, snake_j = snake_i + di, snake_j + dj

        if points[ans] == (snake_i, snake_j):
            ans += 1
        elif segments_deque:
            popped = segments_deque.popleft()
            segments_set.remove(popped)

        if (snake_i, snake_j) in segments_set:
            print(ans + 1)
            return

    print(ans + 1)
