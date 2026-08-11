import string


def solve(lines: list[str]):
    cut = lines[:-400-1]
    left_leaf = ''.join(cut).count('|-o')
    right_leaf = ''.join(cut).count('o-|')

    print(left_leaf + right_leaf)


def main():
    with open("sample_input.txt") as reader:
        sample_lines = reader.readlines()

    with open("input.txt") as reader:
        lines = reader.readlines()

    print("Sample: ")
    solve(sample_lines)

    print("Actual: ")
    solve(lines)


if __name__ == "__main__":
    main()
