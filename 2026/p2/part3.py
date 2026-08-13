def solve(lines: list[str]):
    line, *_ = lines
    line = line.strip()

    segments = [0 for _ in range(100)]

    cursor = 0

    for ch1, ch2 in zip(line, reversed(line)):
        if ch1 != ch2:
            ch = ch1
            cursor = apply(cursor, ch)
            cursor = apply(cursor, ch)
        segments[cursor] += 1

    max_ = max(segments)
    max_i = next(i for i in range(100) if segments[i] == max_)

    print((max_i + 1) * max_)


def apply(cursor, ch):
    if ch == "<":
        cursor -= 1
    else:
        cursor += 1

    if cursor == -1:
        cursor = 99
    if cursor == 100:
        cursor = 0
    return cursor
