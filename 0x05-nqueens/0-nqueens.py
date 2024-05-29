#!/usr/bin/python3
import sys
"""
solves the N queens puzzle
"""

def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col].
    
    Parameters:
    board (list): The current state of the board.
    row (int): The row index where the queen is to be placed.
    col (int): The column index where the queen is to be placed.
    
    Returns:
    bool: True if it's safe to place the queen, False otherwise.
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens_util(board, row, n, solutions):
    """
    Utilize backtracking to solve the N-Queens problem.
    
    Parameters:
    board (list): The current state of the board.
    row (int): The current row index to place the queen.
    n (int): The size of the board (n x n).
    solutions (list): A list to store the solutions.
    """
    if row == n:
        solution = [[i, board[i]] for i in range(n)]
        solutions.append(solution)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens_util(board, row + 1, n, solutions)

def solve_nqueens(n):
    """
    Solve the N-Queens problem for a board of size n x n.
    
    Parameters:
    n (int): The size of the board (n x n).
    
    Returns:
    list: A list of solutions, each solution is a list of [row, col] pairs.
    """
    board = [-1] * n
    solutions = []
    solve_nqueens_util(board, 0, n, solutions)
    return solutions

def main():
    """
    Main function to handle command line arguments and solve the N-Queens problem.
    """
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

    solutions = solve_nqueens(n)
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()