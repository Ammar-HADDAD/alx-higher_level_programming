#!/usr/bin/python3
import sys

def is_valid(board, row, col):
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(0, col + 1)):
        if board[i][j] == 1:
            return False

    return True

def solve(board, row):
    n = len(board)
    if row == n:
        print(board)
        return

    for col in range(n):
        if is_valid(board, row, col):
            board[row][col] = 1
            solve(board, row + 1)
            board[row][col] = 0

def nqueens(n):
    if not isinstance(n, int) or n < 4:
        print("N must be a number")
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]
    solve(board, 0)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    n = int(sys.argv[1])
    nqueens(n)