import string


def solve(lines: list[str]):
    cut = lines[:-400-1]
    left_leaf = ''.join(cut).count('|-o')
    right_leaf = ''.join(cut).count('o-|')

    print(left_leaf + right_leaf)
