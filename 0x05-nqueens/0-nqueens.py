#!/usr/bin/python3
"""N queens task"""
import sys

def print_solution(queens):
    """Print the board in the required format."""
    solution = []
    for i in range(len(queens)):
        solution.append([i, queens[i]])
    print(solution)

def is_safe(queens, n, row, col):
    """Check if it's safe to place a queen at row, col."""
    for i in range(col):
        if queens[i] == row or \
           queens[i] - i == row - col or \
           queens[i] + i == row + col:
            return False
    return True

def solve_nqueens(queens, col, n):
    """Use backtracking to find all solutions."""
    if col == n:
        print_solution(queens)
        return

    for i in range(n):
        if is_safe(queens, n, i, col):
            queens[col] = i
            solve_nqueens(queens, col + 1, n)
            queens[col] = -1

def check_input(args):
    """Check the command-line arguments."""
    if len(args) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(args[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n

def main():
    """Main function to run the N-Queens solver."""
    n = check_input(sys.argv)
    queens = [-1 for _ in range(n)]
    solve_nqueens(queens, 0, n)

if __name__ == "__main__":
    main()