"""
"Word Search"

=> You are given an m x n grid of characters board and a string word. Return true if word exists in the grid.
    The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally
    or vertically neighboring. The same letter cell may not be used more than once.

=> Example :
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED"
Output: True

Time Complexity : O(m * n * 4^len(word))
Space Complexity : O(len(word))
"""


def exist(board, word):
    rows, cols = len(board), len(board[0])

    def dfs(i, j, index):
        if index == len(word):
            return True

        if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != word[index]:
            return False

        temp = board[i][j]
        board[i][j] = "$"  # visited

        # All 4 directions
        found = (
            dfs(i + 1, j, index + 1)
            or dfs(i - 1, j, index + 1)
            or dfs(i, j + 1, index + 1)
            or dfs(i, j - 1, index + 1)
        )

        board[i][j] = temp  # backtrack
        return found

    for i in range(rows):
        for j in range(cols):
            if dfs(i, j, 0):
                return True

    return False


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"

output = exist(board, word)
print(output)
