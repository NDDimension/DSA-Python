"""
"Median of the Row Wise Sorted Matrix"

=>  Given a matrix we need to return the median after sorting the whole matrix row wise.
"""


# Brute Force : 2D -> 1D then find the median
# TC : O(n x m) + O(n x m) x O(log(n x m))
# SC : O(n x m)


def median(matrix):
    temp = []
    for row in matrix:
        for val in row:
            temp.append(val)
    temp.sort()
    n = len(temp)
    return temp[n // 2] if n % 2 != 0 else (temp[n // 2] + temp[n // 2 - 1]) // 2


matrix = [[6, 5], [3, 4]]
print(median(matrix))

# Optimal Approach : using Binary Search


def upperBound(matrix, target):
    low, high, ans = 0, len(matrix) - 1, len(matrix)

    while low <= high:
        mid = (low + high) // 2
        if matrix[mid] > target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans


def countSmallEquals(matrix, mid):
    n, m = len(matrix), len(matrix[0])
    count = 0

    for i in range(n):
        count += upperBound(matrix[i], mid)
    return count


def median_op(matrix):
    n, m = len(matrix), len(matrix[0])
    low, high = float("inf"), float("-inf")

    for i in range(n):
        low = min(low, matrix[i][0])
        high = max(high, matrix[i][m - 1])

    required = (n * m) // 2
    while low <= high:
        mid = (low + high) // 2
        smallEqual = countSmallEquals(matrix, mid)
        if smallEqual <= required:
            low = mid + 1
        else:
            high = mid - 1
    return low


matrix = [[1, 2, 3, 4, 5], [8, 9, 11, 12, 13], [21, 23, 25, 27, 29]]

median_op(matrix)
