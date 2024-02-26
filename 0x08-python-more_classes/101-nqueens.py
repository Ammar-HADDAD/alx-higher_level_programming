#!/usr/bin/python3
"""
    101-nqueens.py - Place N non-attacking queens on an N×N chessboard
    Calc N queens problem
    Args: n - number of queens on an NxN chessboard
"""
import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)
if sys.argv[1].isdigit() is False:
    print("N must be a number")
    exit(1)
n = int(sys.argv[1])
if n < 4:
    print("N must be at least 4")
    exit(1)
result = []
for r in range(n):
    for c in range(n):
        continue