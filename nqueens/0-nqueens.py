#!/usr/bin/python3
"""Solve the N queens puzzle and print every possible solution."""
import sys


def is_safe(queens, row, col):
    """Return True if a queen at (row, col) is not attacked by the others."""
    for r, c in enumerate(queens):
        if c == col or abs(r - row) == abs(c - col):
            return False
    return True


def solve(n, row, queens):
    """Place queens row by row with backtracking and print each solution."""
    if row == n:
        print([[r, c] for r, c in enumerate(queens)])
        return
    for col in range(n):
        if is_safe(queens, row, col):
            queens.append(col)
            solve(n, row + 1, queens)
            queens.pop()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    solve(n, 0, [])
