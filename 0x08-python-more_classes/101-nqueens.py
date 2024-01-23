#!/usr/binenv python3
import sys

def is_attacking(queen1, queen2):
    return queen1[0] == queen2[0] or queen1[1] ==2[1] or abs(queen1[0] - queen2[0]) == abs(queen1[1] - queen2[1])

def n_queens(n, row=0, queens=[]):
    if row == n:
        print(queens)
        return
    for col in range(n):
        if all((queen[0] != row or queen[1] != col) and not is_attacking((row, col), queen) for queen in queens):
            n_queens(n, row + 1, queens + [(row, col)])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N", file=sys.stderr)
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number", file=sys.stderr)
        sys.exit(1)
    if n < 4:
        print("N must be at least 4", file=sys.stderr)
        sys.exit(1)
    n_queens(n)