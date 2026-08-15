from di import real, sample


@sample(grid_size=10)
@real(grid_size=30)
def solve(lines: list[str], grid_size: int):
    lines = [line.strip() for line in lines]

    instructions, _, *points = lines

    points = [(int(x), int(y)) for x, y in (line.split(",") for line in points)]

    snake_i, snake_j = 0, 0
    ans = 0
    for move in instructions[: len(instructions) // 2 + 1]:
        if points[ans] == (snake_i, snake_j):
            ans += 1
            # print(f'Ate a sushi at {points[ans - 1]}')

        DELTA = {
            "^": (0, 1),
            "v": (0, -1),
            "<": (-1, 0),
            ">": (1, 0),
        }

        di, dj = DELTA[move]
        snake_i, snake_j = snake_i + di, snake_j + dj

    print(ans)
