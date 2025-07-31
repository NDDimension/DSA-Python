"""
"Find Row with Maximum 1s"

=> Given a matrix with sorted rows find the row with max 1s.
"""


# Naive approach : iterate and count 1s in each.
# TC : O(n x m )
def findRowWithMax(matrix):
    index = -1
    maxCount = -1

    n = len(matrix)
    m = len(matrix[0])

    for i in range(n):
        maxRow = 0
        for j in range(m):
            maxRow += matrix[i][j]

        if maxRow > maxCount:
            maxCount = maxRow
            index = i

    return index


matrix = [
    [0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1],
]

print(f"ROW -> {findRowWithMax(matrix)}")

# Optimal Approach : Binary Search
# TC : O(n x log m)


def lower_bound(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] >= target:
            high = mid - 1
        else:
            low = mid + 1

        return low


def findRowWithMax_BS(matrix):
    n = len(matrix)
    m = len(matrix[0])

    index = -1
    maxCount = 0

    for i in range(n):
        lb = lower_bound(matrix[i], 1)
        count_1s = m - lb

        if count_1s > maxCount:
            maxCount = count_1s
            index = i

    return index


findRowWithMax_BS(matrix)
