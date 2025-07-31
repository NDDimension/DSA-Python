"""
"Rotate the given matrix by 90 degrees clockwise"

=> Given [1 2 3]       to =>  [7 4 1]
             [4 5 6]                [8 5 2]
             [7 8 9]                [9 6 3]

=> Brute Force:

    - Iterate and place columns to rows
    - For rows find pattern and do appropriate. [ 0th row -> n-1 pos , ith row -> n-1-i pos]

=> Time Complexity : O(n x n)
=> Space Complexity : O(n x n)

=> Optimal Approach :

    - Transpose + Reverse rows

=> Time Complexity : O(n x n)
=> Space Complexity : O(1)



"""


def rotate_by_90Brute(matrix):
    n = len(matrix)
    ans = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            ans[j][n - 1 - i] = matrix[i][j]

    return ans


def rotate_by_90Optimal(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()

    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(str(x) for x in row))


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_matrix = rotate_by_90Optimal(matrix)
print_matrix(new_matrix)
