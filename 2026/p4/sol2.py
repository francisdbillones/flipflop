import string


def solve(lines: list[str]):
    cut = lines[3:-2]
    ans = 0

    leaves = [line for line in lines if 'o-|' in line or '|-o' in line] 
    path = leaves[::-1]

    ans = 0
    while True:
        new_path = []
        for leaf in path: 
            if not new_path or leaf == new_path[-1]:
                new_path.append(leaf)
            else:
                new_path[-1] = leaf
        del new_path[-1]
        ans += 1

        if not new_path:
            break
        path = new_path

    print(ans)


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
