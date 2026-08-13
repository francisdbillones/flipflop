def solve(lines: list[str]):
    line, *_ = lines

    segments = [0 for _ in range(100)]
    cursor = 0

    for ch in line:
        if ch == "<":
            cursor -= 1
        else:
            cursor += 1

        if cursor == -1:
            cursor = 99
        if cursor == 100:
            cursor = 0

        segments[cursor] += 1

    max_ = max(segments)
    max_i = next(i for i in range(100) if segments[i] == max_)
    print((max_i + 1) * max_)
