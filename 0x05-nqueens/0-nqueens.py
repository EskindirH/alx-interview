#!/usr/bin/python3
import sys


def print_usage_and_exit(message):
    """Prints an error message and exits the program with status 1."""
    print(message)
    sys.exit(1)


def is_safe(board, row, col, n):
    """
    Checks if placing a queen at position (row, col) is safe.
    It checks if no other queen can attack this position.
    """
    for i in range(row):
        # Check same column
        if board[i] == col:
            return False
        # Check diagonals
        if abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_nqueens(board, row, n, solutions):
    """
    Recursively solves the N-Queens problem by placing queens row by row.
    Adds each valid solution to the 'solutions' list.
    """
    if row == n:
        solutions.append(board[:])
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_nqueens(board, row + 1, n, solutions)


def print_solutions(solutions, n):
    """
    Prints each solution in the format:
    [[row, col], [row, col], ...] for all the solutions found.
    """
    for solution in solutions:
        result = []
        for row in range(n):
            result.append([row, solution[row]])
        print(result)


def nqueens(n):
    """
    Initializes the board and solutions list, then solves the N-Queens problem.
    """
    board = [-1] * n
    solutions = []
    solve_nqueens(board, 0, n, solutions)
    print_solutions(solutions, n)


if __name__ == "__main__":
    # Check the number of arguments
    if len(sys.argv) != 2:
        print_usage_and_exit("Usage: nqueens N")

    # Check if N is an integer
    try:
        N = int(sys.argv[1])
    except ValueError:
        print_usage_and_exit("N must be a number")

    # Check if N is at least 4
    if N < 4:
        print_usage_and_exit("N must be at least 4")

    # Solve the N-Queens problem
    nqueens(N)
