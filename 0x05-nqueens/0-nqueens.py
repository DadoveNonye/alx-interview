#!/usr/bin/python3
import sys
"""
solves the N queens puzzle
"""

def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen at board[row][col].

    Args:
        board (list): The current state of the board.
        row (int): The row index to check.
        col (int): The column index to check.
        N (int): The size of the board (N x N).

    Returns:
        bool: True if it's safe to place the queen, False otherwise.
    """
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens_util(board, col, N, solutions):
    """
    Utilize backtracking to solve the N queens problem.

    Args:
        board (list): The current state of the board.
        col (int): The current column index to place the queen.
        N (int): The size of the board (N x N).
        solutions (list): A list to store all the valid solutions.

    Returns:
        bool: True if a solution is found, False otherwise.
    """
    if col >= N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return True

    res = False
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            res = solve_nqueens_util(board, col + 1, N, solutions) or res
            board[i][col] = 0

    return res

def solve_nqueens(N):
    """
    Solve the N queens problem and print all solutions.

    Args:
        N (int): The size of the board (N x N).
    """
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_nqueens_util(board, 0, N, solutions)
    for solution in solutions:
        print(solution)

def main():
    """
    Main function to handle command-line arguments and initiate solving.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)

if __name__ == "__main__":
    main()
