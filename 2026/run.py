#!/usr/bin/env python3
import argparse
import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

INPUT_FILENAMES = {
    "sample": "sample_input.txt",
    "real": "input.txt",
}


def load_solve(problem: str, part: int):
    module_path = ROOT / problem / f"part{part}.py"
    if not module_path.exists():
        raise FileNotFoundError(f"no such file: {module_path}")

    spec = importlib.util.spec_from_file_location(f"{problem}_part{part}", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.solve


def main():
    parser = argparse.ArgumentParser(description="Run a solve() for a given problem/part/input.")
    parser.add_argument("problem", help='problem name, e.g. "p1", "p4"')
    parser.add_argument(
        "part",
        type=int,
        nargs="?",
        choices=(1, 2, 3),
        help="part number; if omitted, runs all parts that exist",
    )
    parser.add_argument(
        "input_type",
        nargs="?",
        choices=("sample", "real"),
        help="which input file to use; if omitted, runs both",
    )
    args = parser.parse_args()

    if args.part:
        parts = (args.part,)
    else:
        parts = tuple(
            part for part in (1, 2, 3)
            if (ROOT / args.problem / f"part{part}.py").exists()
        )

    if args.input_type:
        input_types = (args.input_type,)
    else:
        input_types = tuple(
            input_type for input_type in ("sample", "real")
            if (ROOT / args.problem / INPUT_FILENAMES[input_type]).exists()
        )
        if not input_types:
            raise FileNotFoundError(
                f"neither sample_input.txt nor input.txt exists in {ROOT / args.problem}"
            )

    for part in parts:
        solve = load_solve(args.problem, part)
        for input_type in input_types:
            input_path = ROOT / args.problem / INPUT_FILENAMES[input_type]
            with open(input_path) as reader:
                lines = reader.readlines()

            print(f"part {part} / {input_type}:")
            solve(lines)


if __name__ == "__main__":
    main()
