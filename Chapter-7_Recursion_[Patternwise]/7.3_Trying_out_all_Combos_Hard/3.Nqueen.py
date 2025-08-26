"""
"N Queen"

=> The N-Queens problem asks you to place N queens on an N x N chessboard so that no two queens attack each other.
    Queens attack horizontally, vertically, and diagonally.
     Return all distinct solutions to the problem. Each solution contains a board configuration represented as a list of strings.

=> Example:
Input: n = 4

Output: [
 [".Q..",
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",
  "Q...",
  "...Q",
  ".Q.."]
]

Time Complexity : O(n!) backtracking calls + O(n²) per solution stored.
Space Complexity : O(n²)
"""


def solveNQueens(n):
    res = []
    board = [["."] * n for _ in range(n)]

    cols = set()
    pos_diag = set()  # (row + col)
    neg_diag = set()  # (row - col)

    def backtrack(row):
        if row == n:
            # Convert board to list of strings
            solution = ["".join(r) for r in board]
            res.append(solution)
            return

        for col in range(n):
            if col in cols or (row + col) in pos_diag or (row - col) in neg_diag:
                continue

            # Place queen
            board[row][col] = "Q"
            cols.add(col)
            pos_diag.add(row + col)
            neg_diag.add(row - col)

            backtrack(row + 1)

            # Backtrack
            board[row][col] = "."
            cols.remove(col)
            pos_diag.remove(row + col)
            neg_diag.remove(row - col)

    backtrack(0)
    return res


solveNQueens(4)
