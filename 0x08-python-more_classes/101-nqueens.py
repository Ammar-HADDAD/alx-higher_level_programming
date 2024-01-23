#!/usr/bin/python3
import sys

def is_safe(board, row, col, n):
    # Check if a queen can be placed at board[row][col]
    for i in range(col):
        if board[i] == row or board[i] - i == row - col or board[i] + i == row + col:
            return False
    return True

def solve_nqueens_util(board, col, n, solutions):
    if col == n:
        solutions.append(board[:])
        return
    for row in range(n):
        if is_safe(board, row, col, n):
            board[col] = row
            solve_nqueens_util(board, col + 1, n, solutions)

def solve_nqueens(n):
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [-1] * n
    solutions = []
    solve_nqueens_util(board, 0, n, solutions)
    return solutions

def print_solutions(solutions):
    for solution in solutions:
        print([[i, solution[i]] for i in range(len(solution))])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    
    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(n)
    print_solutions(solutions)
