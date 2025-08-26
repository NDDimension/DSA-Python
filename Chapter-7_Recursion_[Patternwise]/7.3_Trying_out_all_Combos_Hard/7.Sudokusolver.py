"""
"Sudoku Solver"

=> Given a 9x9 incomplete sudoku, solve it such that it becomes valid sudoku. Valid sudoku has the following properties.

    1. All the rows should be filled with numbers(1 - 9) exactly once.

    2. All the columns should be filled with numbers(1 - 9) exactly once.

    3. Each 3x3 submatrix should be filled with numbers(1 - 9) exactly once.

Note: Character '.' indicates empty cell.

Time Complexity : O(9(n ^ 2))
Space Complexity : O(1)
"""


def isValid(board, row, col, char):
    """
    Check for valid to place on
    """

    for i in range(9):
        # Check row and col
        if board[row][i] == char or board[i][col] == char:
            return False

        # Check 3x3 subgrid
        subgrid_row = 3 * (row // 3) + i // 3
        subgrid_col = 3 * (col // 3) + i % 3
        if board[subgrid_row][subgrid_col] == char:
            return False

    return True


def solveSudoku(board):
    """
    Solve with backtrack
    """
    for row in range(9):
        for col in range(9):
            if board[row][col] == ".":
                for char in "123456789":
                    if isValid(board, row, col, char):
                        board[row][col] = char
                        if solveSudoku(board):
                            return True
                        board[row][col] = "."  # backtrack

                return False  # no valid num
    return True  # solved


def printBoard(board):
    for row in board:
        print(" ".join(row))


board = [
    ["9", "5", "7", ".", "1", "3", ".", "8", "4"],
    ["4", "8", "3", ".", "5", "7", "1", ".", "6"],
    [".", "1", "2", ".", "4", "9", "5", "3", "7"],
    ["1", "7", ".", "3", ".", "4", "9", ".", "2"],
    ["5", ".", "4", "9", "7", ".", "3", "6", "."],
    ["3", ".", "9", "5", ".", "8", "7", ".", "1"],
    ["8", "4", "5", "7", "9", ".", "6", "1", "3"],
    [".", "9", "1", ".", "3", "6", ".", "7", "5"],
    ["7", ".", "6", "1", "8", "5", "4", ".", "9"],
]

if solveSudoku(board):
    print("Sudoku Solved:\n")
    printBoard(board)
else:
    print("No solution exists.")
