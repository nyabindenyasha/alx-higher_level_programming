#!/usr/bin/python3
""" N queens """
import sys


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


def check(board, row, col):
    """ check the cells in the board.
        Args:
            board: (list) chess board.
            row: (int) current row index.
            col: (int) current col index.
        Return:
            (bool) True if it's a valid position,
                   False if doesn't.
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


def recursion(board, col):
    """ Perfome the recursion.
        Args:
            board: (list) chess board.
            col: (int) current col index.
        Returns:
            (bool) True of False.
    """

    if col >= N:
        result = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    result.append([i, j])

        if result != []:
            print(result)

    for i in range(N):
        if check(board, i, col):
            board[i][col] = 1
            if recursion(board, col + 1) is True:
                return True
            board[i][col] = 0
    return False


def solve():
    """ intial function to solve the problem.
        Args:
            None.
        Returns:
            None.
    """
    board = [[0 for i in range(N)] for j in range(N)]

    r = recursion(board, 0)


if __name__ == "__main__":
    solve()
