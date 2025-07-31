"""
"Find Target in 2D Matrix - II"

=> Here we are given with a matrix with rows sorted ; find the target coordinates in the matrix.
"""

# Better Approach:
# TC : O(N x log M)
# SC : O(1)


def BS(matrix, target):
    low = 0
    high = len(matrix) - 1
    while low <= high:
        mid = low + high
        if matrix[mid] == target:
            return mid
        elif matrix[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def findTarget(matrix, target):
    n = len(matrix)
    m = len(matrix[0])

    for i in range(n):
        index = BS(matrix[i], target)
        if index != -1:
            return [i, index]
    return [-1, -1]


matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30],
]
target = 14
print(findTarget(matrix, target))

# Optimal Approach
# TC : O(N + M)
# SC : O(1)


def findTarget_OP(matrix, target):
    n = len(matrix)
    m = len(matrix[0])

    row = 0
    col = m - 1

    while row < n and col >= 0:
        if matrix[row][col] == target:
            return [row, col]
        elif matrix[row][col] < target:
            row += 1
        else:
            col -= 1

    return [-1, -1]


findTarget_OP(matrix, target)
