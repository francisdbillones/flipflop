def solve(lines: list[str]):
    leaves = [line for line in lines if "o-|" in line or "|-o" in line]
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
