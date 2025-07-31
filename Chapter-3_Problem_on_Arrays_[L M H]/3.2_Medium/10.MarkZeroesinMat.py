"""
" Set Matriz Zeros"

=> Given [1  1  1],
              [1 0 1],
              [1  1  1]

=> Mark the whole row and column to 0s if you find 0 i.e.
[1 0 1]
[0 0 0]
[1 0 1]

=> Brute Force:

    - Iterate over and mark the points to -1
    - Again iterate change the marked to 0s

=> Time Complexity : O(n x m) x O(n + m) + O(n x m)

=> Better Approach :

    - Use single array for row and column
    - if encounter 0 mark them as 1 in those singular array
    - re iterate and change the marked rows and column 1s to 0s

=> Time Complexity : O(n x m) + O(n x m)
=> Space Complexity : O(n) + O(m)

=> Optimal Approach :

    - Same as better just shift those singular arrays inside the matrix
    - Mark leaving the 0th row and columns
    - Then at last mark those

=> Time Complexity : O(2 x n x m)
=> Space Complexity : O(1)


"""


def set_zeros(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    def markRows(i):
        for j in range(cols):
            if matrix[i][j] != 0:
                matrix[i][j] = -99999

    def markCols(j):
        for i in range(rows):
            if matrix[i][j] != 0:
                matrix[i][j] = -99999

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                markRows(i)
                markCols(j)

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == -99999:
                matrix[i][j] = 0

    return matrix


def set_zeros_better(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    row = [0] * rows
    col = [0] * cols

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                row[i] = 1
                col[j] = 1

    for i in range(rows):
        for j in range(cols):
            if row[i] or col[j]:
                matrix[i][j] = 0

    return matrix


def set_zeros_optimal(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    col0 = 1

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                if j != 0:
                    matrix[0][j] = 0
                else:
                    col0 = 0

    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] != 0:
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

    if matrix[0][0] == 0:
        for j in range(cols):
            matrix[0][j] = 0

    if col0 == 0:
        for i in range(rows):
            matrix[i][0] = 0

    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(str(x) for x in row))


matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
new_matrix = set_zeros_optimal(matrix)
print_matrix(new_matrix)
