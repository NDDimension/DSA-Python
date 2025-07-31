"""
"Find the given Target in 2D Array
"""

# Naive : Iterate and look for it
# TC : O(n x m)


def FindTarget(arr, target):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == target:
                return True
    return False


arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
target = 8
print(FindTarget(arr, target))

# Better Approach : Binary + Linear
# TC : O(n) + O(log m)


def bs(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return True

        elif target > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return False


def FindTarget_Better(matrix, target):
    n = len(matrix)
    m = len(matrix[0])

    for i in range(n):
        if matrix[i][0] <= target <= matrix[i][m - 1]:
            return bs(matrix[i], target)

    return False


FindTarget_Better(arr, target)

# Optimal : Binary Search
# TC : O(log(n x m))


def FindTarget_Optimal(matrix, target):
    n, m = len(matrix), len(matrix[0])
    low = 0
    high = n * m - 1

    while low <= high:
        mid = (low + high) // 2
        row = mid // m
        col = mid % m

        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False


FindTarget_Optimal(arr, target)
