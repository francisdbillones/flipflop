import string


def solve(lines: list[str]):
    passwords = [line.strip() for line in lines]

    print(
        max(
            sum(strength(pw + c) for pw in passwords)
            for c in string.ascii_lowercase + string.ascii_uppercase + string.digits
        )
    )


def strength(pw: str) -> int:
    lower = any(c in string.ascii_lowercase for c in pw)
    upper = any(c in string.ascii_uppercase for c in pw)
    digit = any(c in string.digits for c in pw)

    score = lower + upper + digit + longest_consecutive_subsequence(pw) ** 2

    if "7" in pw and all(digit not in pw for digit in "012345689"):
        score += 7

    if any(s in pw for s in ("blue", "red", "green")):
        score *= 3

    return score * len(pw)


def longest_consecutive_subsequence(pw: str) -> int:
    if len(pw) == 1:
        return 0

    max_len = 0
    current_seq = 1

    for i, c in zip(range(1, len(pw)), pw[1:]):
        if pw[i - 1] == c:
            current_seq += 1
        else:
            max_len = max(max_len, current_seq)
            current_seq = 1
    max_len = max(max_len, current_seq)

    if max_len >= 3:
        return max_len
    else:
        return 0
