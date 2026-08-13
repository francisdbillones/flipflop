def solve(lines: list[str]):
    line, *_ = lines
    line = line.strip()

    cursor_a, cursor_b = 0, 0
    ans = 0

    for ch1, ch2 in zip(line, reversed(line)):
        cursor_a = apply(cursor_a, ch1)
        cursor_b = apply(cursor_b, ch2)

        if cursor_a == cursor_b:
            ans += 1

    print(ans)


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
