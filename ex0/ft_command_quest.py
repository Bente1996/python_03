#!/usr/bin/env python3

import sys

def ft_command_quest(argv: list) -> None:
    print(f"Program name: {argv[0]}")
    print(f"Arguments received: {len(argv) - 1}")
    i = 1
    while i < len(argv):
        print(f"Argument {i}: {argv[i]}")
        i += 1
    print(f"Total arguments: {len(argv)}")

if __name__ == "__main__":
    print("=== Command Quest ===")
    ft_command_quest(sys.argv)
